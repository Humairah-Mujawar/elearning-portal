# eLearning-portal
eLearning portal built using Python with Django

# Steps to Run
1. Download project
2. Go to project folder, and then subfolder "elearning-portal". In settings.py, make two changes as below and save:<br/>
  i. Uncomment line with code
   ``` ALLOWED_HOSTS = [] ``` <br>
   ii. Comment line with code
   ``` ALLOWED_HOSTS = ['elearning-portal-production.up.railway.app'] ```
4. Open Terminal and navigate to project path
5. Type command
   ``` python manage.py runserver ```
6. The Terminal will give a URL, copy and paste it in browser to open app. <br/>
For example: ```Starting development server at http://127.0.0.1:8000/ ```
