+++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++

# PROJECT 10: Create a secure RESTful API using Django REST

+++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++

## Context

Creation of a Representational State Tranfer (REST) ​​API allowing users to create various projects.
These projects can have multiple collaborators and project related issues can be flagged and commented on.

## Installation


### 1 - Installation of Python3, the virtual environment tool, the package manager and sqlite3 (on Linux UBUNTU)

    $ sudo apt-get install python3 python3-venv python3-pip sqlite3


### 2 - Setting up the virtual environment "env"

    1 - Access to the project directory:
            
            cd /softdesk example

    2 - Creation of the virtual environment:
            
            $ python3 -m venv env


### 3 - Opening the virtual environment and adding modules

            $ source env/bin/activate
            
            (env) $ pip install -r requirements.txt
            

### 4 - Modification of the file literview / literview / settings_example.py

    1 - Rename the settings_example.py file to settings.py

    2 - Modify the variable 'SECRET_KEY' in order to add a security key
        "django-insecure- (+ 50 random characters with uppercase,
        lowercase, numbers and special characters) "


## Using the program


### 1 - Launch

    1 - activation of the virtual environment in the home directory:

        source env/bin/activate

    2 - access to the softdesk directory:

        cd /softdesk

    3 - Launching the Django server

        ./manage.py runserver


### 2 - Using the API

    In order to test this API, 4 fictitious users are registered with some projects,
    problems and comments in the "db.sqlite3" database made available in the repository:

        - admin
        - arnaud
        - eric
        - claude

        the password for users: P@ssword1

    Access to the admin page is possible:

        Example on a local installation: http://127.0.0.1:8000/admin

        user: admin
        password: P@ssword1

    This allows full access (read and write) to the database tables.

    Command for creating an administrator:

        ./manage.py createsuperuser

    To have an initial database:

        1 - Stop the Django server by performing the combination:
                
                 control + c

        2 - Delete the "db.sqlite3" file

        3 - migrate to the new base

                ./manage.py makemigrations => This creates a file in softdesk/projects/migrations

                ./manage.py migrate => Creation of tables in the "db.sqlite" file (created directly)
              
### 3 - Using queries

    Several methods exist to perform queries, example:

        - With POSTMAN software (Used for the documentation of this API)

                Installation on Linux UBUNTU:

                sudo snap install postman

        - With the command line software cURL:

            Installation on Linux UBUNTU:

                sudo snap install curl

            Example of the 'GET projects' request

                curl --location --request GET 'http://127.0.0.1:8000/projects' \
                --header 'Authorization: Bearer "TOKEN 'access' "'

### 4 - List of requests

    Detailed documentation is available at: ''

    - POST signup: http://127.0.0.1:8000/signup/

        Registration of a user to the API.
        Fields to use: username, password, password2, first_name, last_name, email

    - POST: http://127.0.0.1:8000/login/

        Connection of a user to the API.
        Fields to use: username, password
        Return: TOKEN 'access' key (To be used for requests with authentication, valid for 1 hour)
                 TOKEN 'refresh' key (To be used for refresh and logout requests)
                 
    - POST: http://127.0.0.1:8000/login/refresh/

        Retrieving another pair of TOKEN keys without reconnecting
        Fields to use: refresh
        Return: TOKEN 'access' key (To be used for requests with authentication, valid for 1 hour)
                 TOKEN 'refresh' key (To be used for refresh and logout requests)

    - PUT: http://127.0.0.1:8000/change_password/{user_id}

        Authentication required
        Allows the password to be changed
        Fields to use: old_password, password, password2

    - GET: http://127.0.0.1:8000/users/

        Authentication required
        Provides access to the list of API users

    - POST: http://127.0.0.1:8000/logout/
        Authentication required
        Allows you to blacklist the TOKEN refresh key to prohibit its use
        Fields to use: refresh

    - GET: http://127.0.0.1:8000/projects/

        Authentication required
        Access to the list of projects to which the user is linked.

    - POST: http://127.0.0.1:8000/projects/

        Authentication required
        Creation of a project
        Fields to use: title, description, project_type

    - GET: http://127.0.0.1:8000/projects/{project_id}

        Authentication required, user contributing to the project
        Access to project details
    
    - PUT: http://127.0.0.1:8000/projects/{project_id}

        Authentication required, user author of the project
        Modification of the project
        Fields to use: title, description, project_type

    - DELETE: http://127.0.0.1:8000/projects/{project_id}

        Authentication required, user author of the project
        Deleting the project

    - GET: http://127.0.0.1:8000/projects/{project_id}/users/
        
        Authentication required, user contributing to the project
        Access to the list of project contributors

    - POST: http://127.0.0.1:8000/projects/{project_id}/users/

        Authentication required, user author of the project
        Adding a contributor to the project
        Fields to use: user_id, role

    - DELETE: http://127.0.0.1:8000/projects/{project_id}/users/{user_id}

        Authentication required, user author of the project
        Removing a contributor from the project
     
    - GET: http://127.0.0.1:8000/projects/{project_id}/issues/

        Authentication required, user contributing to the project
        Access to the list of project problems

    - POST: http://127.0.0.1:8000/projects/{project_id}/issues/

        Authentication required, user contributing to the project
        Adding a problem to the project
        Fields to use: title, description, tag, priority, status, assignee_user_id

    - PUT: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}

        Authentication required, user responsible for posted problem
        Adding a problem to the project
        Fields to use: title, description, tag, priority, status, assignee_user_id
    
    - DELETE: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}

        Authentication required, user responsible for posted problem
        Removing a problem from the project

    - GET: http://127.0.0.1:8000/projects/{project_id}/issues/{{issue_id}/comments

        Authentication required, user contributing to the project
        Access to the list of comments on the problem

    - POST: http://127.0.0.1:8000/projects/{project_id}/issues/{{issue_id}/comments

        Authentication required, user contributing to the project
        Adding a comment to the problem
        Fields to use: description

    - GET: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{comment_id}

        Authentication required, user contributing to the project
        Access to the details of the comment to the problem

    - PUT: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{comment_id}

        Authentication required, user commenting
        Editing a comment to the problem
        Fields to use: description

    - DELETE: http://127.0.0.1:8000/projects/{project_id}/issues/{issue_id}/comments/{comment_id}

        Authentication required, user commenting
        Deleting a comment to the problem


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# PROJET 10 : Créez une API sécurisée RESTful en utilisant Django REST

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## Contexte

Création d'une API REST (Representational State Tranfer) permettant aux utilisateurs de créer divers projets.
Ces projets peuvent avoir plusieurs collaborateurs et des problèmes liés aux projets peuvent être signalés et commentés.  

## Installation


### 1 - Installation de Python3, l'outil d'environnement virtuel,  le gestionnaire de paquets et sqlite3 (sur Linux UBUNTU)

    $ sudo apt-get install python3 python3-venv python3-pip sqlite3


### 2 - Mise en place de l'environnement virtuel "env"

    1 - Accès au répertoire du projet :
            
            exemple cd /softdesk

    2 - Création de l'environnement virtuel :
            
            $ python3 -m venv env


### 3 - Ouverture de l'environnement virtuel et ajout des modules

            $ source env/bin/activate
            
            (env) $ pip install -r requirements.txt
            

### 4 - Modification du fichier litreview/litreview/settings_exemple.py

    1 - Renomer le fichier settings_exemple.py en settings.py

    2 - Modifier la variable 'SECRET_KEY' afin d'ajouter une clé de sécurité
        "django-insecure-( + 50 caractères aléatoires avec majuscule,
        minuscule, chiffres et caractères spéciaux )"


## Utilisation du programme


### 1 - Lancement

    1 - activation de l'environnement virtuel dans le répertoire de base:

        source env/bin/activate

    2 - accès au répertoire softdesk:

        cd softdesk/

    3 - Lancement du serveur Django

        ./manage.py runserver


### 2 - Utilisation de l'API

    Afin de tester cette API, 4 utilisateurs fictifs sont enregistrés avec quelques projets,
    problèmes et commentaires dans la base de donnée "db.sqlite3" mise à disposition dans le repository : 

        - admin
        - arnaud
        - eric
        - claude

        le mot de passe pour les utilisateurs : P@ssword1

    Un accès à la page admin est possible :

        Exemple sur une installation locale : http://127.0.0.1:8000/admin

        utilisateur : admin    
        password : P@ssword1

    Cela permet un accès complet (lecture et écriture) aux tables de la base de données.

    Commande pour la création d'un administrateur :

        ./manage.py createsuperuser

    Pour avoir une base de donnée initiale:

        1 - Arrêter le serveur Django en effectuant la combinaison :
                
                 control + c 

        2 - Supprimer le fichier "db.sqlite3"

        3 - effectuer la migration vers la nouvelle base

                ./manage.py makemigrations => Cela crée un fichier dans softdesk/projects/migrations 

                ./manage.py migrate => Création des tables dans le fichier "db.sqlite" (crée directement)
              
###  3 - Utilisation des requêtes

    Plusieurs méthodes existe pour effectuer des requêtes, exemple :

        - Avec le logiciel POSTMAN (Utilisé pour la documentation de cet API)

                Installation sur Linux UBUNTU :

                sudo snap install postman

        - Avec le logiciel en ligne de commande cURL :

            Installation sur Linux UBUNTU :

                sudo snap install curl

            Exemple de la requête 'GET projects'

                curl --location --request GET 'http://127.0.0.1:8000/projects' \
                --header 'Authorization: Bearer "TOKEN 'access' "'

###  4 - Liste des requêtes   

    La documentation détaillé est disponible sur : '' 

    - POST signup : http://127.0.0.1:8000/signup/ 

        Inscription d'un utilisateur à l'API. 
        Champs à utiliser : username, password, password2, first_name, last_name, email

    - POST : http://127.0.0.1:8000/login/

        Connexion d'un utilisateur à l'API. 
        Champs à utiliser : username, password
        Retour : Clé TOKEN 'access' (A utiliser pour les requêtes avec authentification, valable 1 heure)
                 Clé TOKEN 'refresh' (A utiliser pour les requêtes refresh et logout)
                 
    - POST : http://127.0.0.1:8000/login/refresh/

        Récupération d'une autre paire de clé TOKEN sans se reconnecter
        Champs à utiliser : refresh
        Retour : Clé TOKEN 'access' (A utiliser pour les requêtes avec authentification, valable 1 heure)
                 Clé TOKEN 'refresh' (A utiliser pour les requêtes refresh et logout)

    - PUT : http://127.0.0.1:8000/change_password/{id_de_l_utilisateur}

        Authentification requis
        Permet le changement du password
        Champs à utiliser : old_password, password, password2

    - GET : http://127.0.0.1:8000/users/

        Authentification requis
        Permet d'accéder à la liste des utilisateurs de l'API

    - POST : http://127.0.0.1:8000/logout/

        Authentification requis
        Permet de blacklister la clé TOKEN refresh pour interdire son utilisation
        Champs à utiliser : refresh

    - GET : http://127.0.0.1:8000/projects/

        Authentification requis
        Accès à la liste des projets auxquels l'utilisateur est lié.

    - POST : http://127.0.0.1:8000/projects/

        Authentification requis
        Création d'un projet
        Champs à utiliser : title, description, project_type

    - GET : http://127.0.0.1:8000/projects/{id_du_projet}

        Authentification requis, utilisateur contributeur du projet
        Accès aux détails d'un projet
    
    - PUT : http://127.0.0.1:8000/projects/{id_du_projet}

        Authentification requis, utilisateur auteur du projet
        Modification du projet
        Champs à utiliser : title, description, project_type

    - DELETE : http://127.0.0.1:8000/projects/{id_du_projet}

        Authentification requis, utilisateur auteur du projet
        Suppression du projet

    - GET : http://127.0.0.1:8000/projects/{id_du_projet}/users/
        
        Authentification requis, utilisateur contributeur du projet
        Accès à la liste des contributeurs du projet

    - POST : http://127.0.0.1:8000/projects/{id_du_projet}/users/

        Authentification requis, utilisateur auteur du projet
        Ajout d'un contributeur au projet
        Champs à utiliser : user_id, role

    - DELETE : http://127.0.0.1:8000/projects/{id_du_projet}/users/{id_du_contributeur}

        Authentification requis, utilisateur auteur du projet
        Suppression d'un contributeur au projet
     
    - GET : http://127.0.0.1:8000/projects/{id_du_projet}/issues/

        Authentification requis, utilisateur contributeur du projet
        Accès à la liste des problèmes du projet

    - POST : http://127.0.0.1:8000/projects/{id_du_projet}/issues/

        Authentification requis, utilisateur contributeur du projet
        Ajout d'un problème au projet
        Champs à utiliser : title, description, tag, priority, status, assignee_user_id

    - PUT : http://127.0.0.1:8000/projects/{id_du_projet}/issues/{id_du_problème}

        Authentification requis, utilisateur auteur du problème posté
        Ajout d'un problème au projet
        Champs à utiliser : title, description, tag, priority, status, assignee_user_id
    
    - DELETE : http://127.0.0.1:8000/projects/{id_du_projet}/issues/{id_du_problème}

        Authentification requis, utilisateur auteur du problème posté
        Suppression d'un problème au projet

    - GET : http://127.0.0.1:8000/projects/{id_du_projet}/issues/{id_du_problème}/comments/

        Authentification requis, utilisateur contributeur du projet
        Accès à la liste des commentaires du problème

    - POST : http://127.0.0.1:8000/projects/{id_du_projet}/issues/{id_du_problème}/comments/

        Authentification requis, utilisateur contributeur du projet
        Ajout d'un commentaire au problème
        Champs à utiliser : description

    - GET : http://127.0.0.1:8000/projects/{id_du_projet}/issues/{id_du_problème}/comments/{id_du_commentaire}

        Authentification requis, utilisateur contributeur du projet
        Accès au details du commentaire au problème

    - PUT : http://127.0.0.1:8000/projects/{id_du_projet}/issues/{id_du_problème}/comments/{id_du_commentaire}

        Authentification requis, utilisateur auteur du commentaire
        Modification d'un commentaire au problème
        Champs à utiliser : description

    - DELETE : http://127.0.0.1:8000/projects/{id_du_projet}/issues/{id_du_problème}/comments/{id_du_commentaire}

        Authentification requis, utilisateur auteur du commentaire
        Suppression d'un commentaire au problème
