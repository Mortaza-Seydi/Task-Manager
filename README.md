# Kanban Task Manager
### manage your teams, projects and tasks

### How To Run:
#### This projects use SQLlite database, so you can easily run it on your local machine
1- `pip install -r requirements.txt`

2- `python manage.py makemigrations`

3- `python manage.py migrate`

4- `python manage.py runserver`

# Photos

## You can sign in or sign up 

![login](preview/login.png)

## In this page you can create your teams or projects and add it's members from registered users. This project is available for other members.

![projects](preview/projects.png)

## In this page admin user (creator of project or team) can add task and assign it to members and himself. You can see the deadline of tasks in calender and task details. Notice only admin can drag tasks in calender to change it's deadline. Other members can drag their tasks in task board to change their status. 

![tasks](preview/tasks.png)

## In this page user can see status or all his projects and his status in all projects.

![report](preview/report.png)
