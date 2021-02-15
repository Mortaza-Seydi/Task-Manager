# Kanban Task Manager
### manage your teams, projects and tasks

### How To Run:
##### This projects use SQLlite database, so you can easily run it on your local machine
1- `pip install -r requirements.txt`

2- `python manage.py makemigrations`

3- `python manage.py migrate`

4- `python manage.py runserver`

## Photos

#### you can signIn or SignUp 

![login](preview/login.png)

#### in this page you can create your teams or projects and add it's members from registered users. this project is available for other members.

![projects](preview/projects.png)

#### in this page admin user (creator of project or team) can add task and assign it to members and himself. you can see the deadline of tasks in calender and task details. notice only admin can drag tasks in calender to change it's deadline. other members can drag their tasks in task board to change their status. 

![tasks](preview/tasks.png)

#### in this page user can see status or all his projects and his status in all projects.

![report](preview/report.png)
