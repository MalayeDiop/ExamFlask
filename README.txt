Mon projet StageTracker est une application web développée pour aider les étudiants à gérer leurs stages. 
Elle permet aux utilisateurs de s’inscrire, se connecter, et ensuite gérer leurs stages. L'application offre 
la possibilité d'ajouter des stages, de modifier des informations relatives à un stage, de rechercher un stage 
par entreprise, et de visualiser la liste complète des stages d'un utilisateur connecté.

Les routes que j'ai utilisé: 
- la route par défaut '/' redirige les utilisateurs vers la page du dashboard. Si un utilisateur n'est pas connecté, 
il est redirigé vers la page de connexion.
- la route '/register' permet aux nouveaux utilisateurs de créer un compte en soumettant leur nom d'utilisateur et 
un mot de passe. Une fois l'inscription réussie, l'utilisateur est redirigé vers la page de connexion pour se connecter.
Si l'utilisateur est déjà connecté, il peut accéder à la page du tableau de bord où il verra la liste de tous ses stages 
personnels. La page de tableau de bord offre aussi une fonction de recherche pour filtrer les stages par entreprise.
- la route '/stage/add' permet d'ajouter un nouveau stage. Cette page contient un formulaire où l'utilisateur doit remplir 
les informations relatives à un stage. 
Une fois le formulaire soumis, le stage est enregistré dans la base de données.
- la route '/stage/edit/<int:id>' permet de modifier un stage existant.

La fonction url_for permet de générer dynamiquement des URLs (comme fait dans le cours). Par exemple url_for('dashboard').

La fonction flash est utilisée pour afficher des messages temporaires à l'utilisateur après des actions comme l'ajout ou 
la modification d'un stage.

L'authentification des utilisateurs est gérée grâce à Flask-Login. La fonction login_user est utilisée pour connecter un
utilisateur, la fonction logout_user permet de déconnecter l'utilisateur et de le rediriger vers la page de connexion.

D'ailleurs pour se connecter sur l'application, voici les coordonnées:
nom: malaye
mdp: malaye12
ou même vous pouvez créer un compte d'utilisateur pour vous connecter.

Le décorateur login_required est appliqué sur les routes qui nécessitent que l'utilisateur soit authentifié.

La méthode request.form permet de récupérer les données soumises via les formulaires dans les pages d'inscription,
de connexion, d'ajout et de modification de stage. Par exemple, lorsque l'utilisateur soumet un formulaire d'ajout de 
stage, request.form['entreprise'] permet de récupérer la valeur de l'entreprise que l'utilisateur a entrée.


Bon en quelques ligne voici ce à quoi consiste mon projet. J'espère que j'ai été assez clair.
Aythieu BREUKHHHHHH.

Mouhamadou Lamine Laye DIOP - L3 GLRS