# eLearning-portal
eLearning portal built using Python with Django

# Steps to Run
1. Download project
2. Go to project folder, and then subfolder "elearning-portal". In settings.py, make two changes as below and save:<br/>
  i. Uncomment line with code
   ```
    ALLOWED_HOSTS = []
   ```
   ii. Comment line with code
   ```
   ALLOWED_HOSTS = ['elearning-portal-production.up.railway.app']
   ```
4. Open Terminal and navigate to project path
5. Type command
   ```
   python manage.py runserver
   ```
