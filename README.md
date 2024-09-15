Project management app similar to kanban board built using ReactJS and Django REST Framework
This is the DRF repo 
Backend Repo: https://github.com/sachinbn96/React-project-management-kanban

Frontend deployed using vercel at: https://react-project-management-kanban.vercel.app/
Backend deplyed using railway deployed at: https://drf-project-management-kanban-production.up.railway.app/admin

Local front end setup:
1. npm install
2. npm run dev

Local backend Setup:
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py runserver

Change backend_url to localhost in the constants.js file when running both locally
