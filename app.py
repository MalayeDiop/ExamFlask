from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import create_app, db, bcrypt
from datetime import datetime
from app.models.user import User
from app.models.stage import Stage

app = create_app()

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Compte créé avec succès !", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("Identifiants invalides", "danger")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    q = request.args.get("q", "")
    if q:
        stages = Stage.query.filter(Stage.user_id == current_user.id, Stage.entreprise.ilike(f"%{q}%")).all()
    else:
        stages = Stage.query.filter_by(user_id=current_user.id).all()
    return render_template("liste_stages.html", stages=stages, query=q)

@app.route('/stage/add', methods=['GET', 'POST'])
@login_required
def ajouter_stage():
    if request.method == 'POST':
        debut = datetime.strptime(request.form['debut'], "%Y-%m-%d").date()
        fin_str = request.form.get('fin')
        fin = datetime.strptime(fin_str, "%Y-%m-%d").date() if fin_str else None

        stage = Stage(
            entreprise=request.form['entreprise'],
            poste=request.form['poste'],
            debut=debut,
            fin=fin,
            description=request.form['description'],
            user_id=current_user.id
        )
        db.session.add(stage)
        db.session.commit()
        flash("Stage ajouté avec succès !", "success")
        return redirect(url_for('dashboard'))
    return render_template('ajouter_stage.html')

@app.route('/stage/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def modifier_stage(id):
    stage = Stage.query.get_or_404(id)
    if stage.user_id != current_user.id:
        flash("Accès non autorisé", "danger")
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        stage.entreprise = request.form['entreprise']
        stage.poste = request.form['poste']
        stage.description = request.form['description']
        stage.debut = datetime.strptime(request.form['debut'], "%Y-%m-%d").date()
        fin_str = request.form.get('fin')
        stage.fin = datetime.strptime(fin_str, "%Y-%m-%d").date() if fin_str else None

        db.session.commit()
        flash("Stage modifié avec succès !", "success")
        return redirect(url_for('dashboard'))

    return render_template('modifier_stage.html', stage=stage)

if __name__ == '__main__':
    app.run(debug=True)
