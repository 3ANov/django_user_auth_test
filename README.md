Test project which show using django-registration, social-auth-app-django and built-in authentication system.

_For deployment:_
1) Clone or download this project from GitHub to folder  
   **ex:** `git clone https://github.com/3ANov/django_user_auth_test`  
   _Project will be cloned into folder:_ "**django_user_auth_test**"
2) Change working directory:  
   **ex:** `cd django_user_auth_test/`
3) Create virtual environment:  
   **ex:** `python3 -m venv ./venv`  
   _You must have 'venv' package installed_.
4) Activate virtual environment:  
   **ex:** `source venv/bin/activate` 
5) Install dependencies from **requirements.txt**:
   **ex:** `pip install -r requirements.txt`
6) Create the file **'.env'** in subfolder **'django_user_auth_test'**  
   _where are located files: **'settings.py, wsgi.py and etc.'**_  
   _**Use the file '.env-example' as an example**_
7) Applying migrations to your database
   **ex:**: `python manage.py migrate`
8) Run development server:  
   **ex:**: `python manage.py runserver`
   
The server uses port **'8000'** for connections.  
You can test this: `curl -I http://127.0.0.1:8000/accounts/login`

   
   