# Kanban Task Manager
### Manage your teams, projects and tasks

### How To Run:
#### This project use SQLite database, so you can easily run it on your local machine. do this steps:

  1- `pip install -r requirements.txt`  or  `pip install Django~=3.1.6`

  2- `python manage.py makemigrations`

  3- `python manage.py migrate`

  4- `python manage.py runserver`

# Photos & Features

### Login
* You can sign in or sign up 

![login](preview/login.png)

### Projects or Teams
* Create your teams or projects and add its members from registered users.
* This project is available for members.
* The creator user will be the admin of project or team.

![projects](preview/projects.png)

### Tasks
* Admin user can add a task and assign it to members and himself. 
* Members can see the start time and end time of a task by clicking on it.
* Members can drag and drop their own tasks to change its status.
* Only admin can add/remove the task to/from "Done", "Blocked" and "Deleted".

![tasks](preview/tasks.png)

### Calendar
* Deadline of tasks will be shown in the calendar.
* Only Admin can drag and drop tasks in the calendar to change its deadline.

![calendar](preview/calendar.png)

### Report
* User can see status or all his projects and his status in all projects.

![report](preview/report.png)
