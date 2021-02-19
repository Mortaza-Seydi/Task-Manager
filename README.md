# Kanban Task Manager
## Manage your teams, projects and tasks

### How To Run:
#### This projects use SQLlite database, so you can easily run it on your local machine. do this steps:

  1- `pip install -r requirements.txt`  or  `pip install Django~=3.1.6`

  2- `python manage.py makemigrations`

  3- `python manage.py migrate`

  4- `python manage.py runserver`

# Photos

### Login
* You can sign in or sign up 

![login](preview/login.png)

### Projects or Teams
* Create your teams or projects and add it's members from registered users.
* This project is available for members.
* The creator user will be admin.

![projects](preview/projects.png)

### Tasks
* Admin user can add task and assign it to members and himself. 
* Members can see the deadline of tasks in calender and task details.
* Only admin can drag tasks in calender to change it's deadline.
* Other members can drag their tasks in task board to change status. 

![tasks](preview/tasks.png)


### Report
* User can see status or all his projects and his status in all projects.

![report](preview/report.png)
