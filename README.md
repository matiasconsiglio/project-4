# ΠΛΤΤ Sessions

This events blog style, for the Full Stack Project from Code Institute, consists in showing and allowing the users to see different events produced by ΠΛΤΤ at Rex Malmo Bar. Each event is shown in the principal page with a flyer. This flyer shows the location, different DJs that will play in future events or already played, dates and times. The user is able to click and see different media and information from each event, including: photos, videos, guest dj, bibliography, social media and an embedded Soundcloud set with the music played in the event. Also the user is able to register and login in the site, this will allow them to like and comment on each event. Finally the user will be able to update personal comments or delete them.

[Here is the live version of my project](https://project-3-exam-results.herokuapp.com/)***

![Welcome image](/assets/readme-images/first-run.png)

## User Stories, Project Goals, Agile Methodology and Diagram for UX

### Project Goals

- Create a full Stack project based on an Event Blog Style application.

- External User's goal:
    - User wants to see what's going on at ΠΛΤΤ Sessions in Rex Malmo Bar, also be able to like and comment on different events.

- Site owner's goals:
    - ΠΛΤΤ wants to have a platform to show to the users media from the different events, connect with them and generate discussion in the community.

- Potential features to include:
    - Create different events.
    - Like and view likes from different events.
    - Comment events.
    - Follow Social Media from different Djs
    - Include photos, videos and audio from the events.
    - See different comments with the time/date of the comment as well as the author.

### User Stories 

1. Manage Events:
    - As an Admin I can create, read, update and delete events so that I can manage my event site.

2. Create Drafts:
    - As an Admin I can create draft events so that I can finish uploading the content later.

3. Approve Comments.
    - As a an Admin I can approve or disapprove comments so that I can filter out objectionable comments.

4. Site Pagination:
    - As a Site User I can view a paginated list of events so that I can easily select a post to view.

5. View Event List:
    - As a Site User I can view a list of events so that I can select one to watch and read.

6. View Likes:
    - As a Site User / Admin I can view the number of likes in each event so that I can see which one is more popular.

7. View Comments:
    - As a Site User / Admin I can view comments on an individual event so that I can read the conversation.

8. Open an Event:
    - As a Site User I can click on an event so that I can see all the information and media from it.

9. Account Registration:
    - As a Site User I can register an account so that I can comment and like different events.

10. Comment on an Event:
    - As a Site User I can comment on an event so that I can interact with it.

11. Edit and Delete Comments:
    - As a Site User I can choose to manipulate my comment so that I can edit it or delete it.

12. Like and Unlike Events:
    - As a Site User I can like or unlike an event so that I can interact with the content.

13. Social Media:
    - As a Site User I can interact with the event social media so that I can follow the different DJs and/or organisers.

14. View Media from Events:
    - As a Site User I can see and/or listen to different media from the event so that I can understand and feel how the event was.

15. Contact Form:
    - As a Site User I can contact the admin for further questions about different sessions.

    In the following link the Agile methodology is shown including epics and acceptance criteria.

### [Agile Methodology used to accomplish the goals from the project via User Stories](https://github.com/matiasconsiglio/project-4/projects/1)

### Diagram for UX design and mock-up

![Diagram for Ux Design](/assets/readme-images/diagram.png)

- All the special pages for login, register, logout and update comment should share the same navbar and footer as the main view.

![Home and Sessions view mock-up](/assets/readme-images/mockup-1.png)

- Home and Sessions view mock-up.

![Session details mock-up](/assets/readme-images/mockup-2.png)

- Session details mock-up

![Session details plus comments mock-up](/assets/readme-images/mockup-3.png)

- Session details plus comments mock-up.

![Contact form mock-up](/assets/readme-images/mockup-4.png)

- Contact form mock-up.

## Features

### Existing Features Tested Manually and Messages for User

-  Welcomes the user to the events blog "ΠΛΤΤ Sessions".

    - Has a Logo with a link to the home page.
    - Has a register and login option for the user in the navbar.
    - Has a Home link to the home page.
    - Shows the different events that have already happened and the ones to come.
    - Shows the different likes each event has.
    - Allows the user to click on "Session #number" to go inside each event and see different information and media from it.
    - Show the social media from ΠΛΤΤ Sessions for users to be able to reach and follow.
    - In case the user is logged in, the navbar won't show register and login, instead will show the option Logout.
    - For resubmission, contact (model) was added to the project, now the user can contact the admin without needing to be logged in neither registered.

![First blog approach](/assets/readme-images/first-run.png)

First blog approach.

- Register for User.

    - Special design page that allows the user to register to ΠΛΤΤ Sessions.
    - Explanation to the user in case they already have and account, button option to go to sign in page.
    - Username, password and password confirmation required.
    - User email input as optional.
    - Sign up button for confirmation.
    - Messages shown in case the name of the user already exists.
    - Navbar and footer keeps the style of the welcome page.
    - Link that allows you to go to the sign in page in case you already have an account created.
    - Message for successfull registration.

 
![Registration](/assets/readme-images/register.png)

Register page with link to sign in page.


![User already exist](/assets/readme-images/user-exists.png)

User message already exist.


![Successful registration](/assets/readme-images/successfull-registration.png)

Successful registration.


- Login for User.

    - Special design page that allows the user to Login to ΠΛΤΤ Sessions.
    - User and Password required
    - Remember me checkbox
    - Sign in button
    - Message shown in case the username or password is incorrect.
    - Navbar and footer keeps the style of the welcome page.
    - Link that allows you to go to the register page in case you don't have an account created.
    - Message for successfull login.

![Login](/assets/readme-images/login.png)

Login Page with message and link for register.


![Incorrect login](/assets/readme-images/incorrect-login.png)

Incorrect login. 


![Successfull login](/assets/readme-images/successfull-login.png)

Successfull login. 


- Logout

    - Logout message asking the user if it is sure they want to logout.
    - Sign out button.
    - Navbar and footer keeps the style of welcome page.
    - Once Sign Out is clicked the user is redirected to the home page.
    - Message for successfull logout.


![Logout](/assets/readme-images/logout.png)

Sign out confirmation page.


![Home](/assets/readme-images/logout-message.png)

Redirect to home after sign out with message.


- Event

    - Number of likes and comments.
    - Possibility to see comments from different users.
    - Navbar and footer keeps the style of the welcome page.
    - Flyer of the event.

    - Depending on the event, the post can have:
        - None, one or more guest Djs.
        - Bio of different guest Djs.
        - Social Media from guest Djs.
        - Photos and embedded videos from Youtube and sound from Soundcloud.
        - ΠΛΤΤ media including photos, videos or/and audio.

    - For all events if the user is logged in:
        - Possibility to comment and wait for approval from Admin of the comment.
        - If the user already commented and the comment was approved; possibility of updating and/or deleting the same user comment.
        - Like the event.
 
![Event post intro plus like option](/assets/readme-images/session2-1.png)

Session first view liked by the user and message.


![Home page with like](/assets/readme-images/home-dislike.png)

Session first view disliked by the user and message.


![Event guest dj video and audio](/assets/readme-images/session2-2.png)

Guest Dj media.


![Matt media 1](/assets/readme-images/mattmedia1.png)

ΠΛΤΤ media.


![Matt media 2](/assets/readme-images/mattmedia2.png)

ΠΛΤΤ media.


![Logged in comment view](/assets/readme-images/loggedin-comment-view.png)

Logged-in comment view plus comments made by the logged in user.


![Logged in commented waiting for approval](/assets/readme-images/comment-view-waiting-approval.png)

Logged-in comment sent waiting for approval and message.


![Logged in comments view](/assets/readme-images/loggedin-comment-approved.png)

Logged-in comment section after approval.


![Logged out comment view](/assets/readme-images/logged-out-comment-view.png)

Logged-out comment section.


- Update comment.
    - Only available for logged in users and for updating their own users comment.
    - Sends you to another page to update and send your new comment, after update the user is sent to the home page.
    - New comment needs approval.
    - Old comment after update dissapears.
    - Message to user "waiting for approval" after update.


![Update comment view](/assets/readme-images/update-comment.png)

Update comment view.


![Update comment waiting for approval](/assets/readme-images/update-comment-waiting-approval.png)

Update comment waiting for approval.


![Update comment view after approval](/assets/readme-images/update-comment-approved.png)

Update comment view after approval.


![Different user logged in comments view](/assets/readme-images/different-user-logged-comment-view.png)

Different user logged in comments view.

  
- Delete comment.
   - Only available for logged in users and for deleting their own comments.
   - Pop-up message with back and delete confirmation option.

![Delete in comments view](/assets/readme-images/delete-comment.png)

Delete in comments view logged in as author.


![Delete pop-up message confirmation](/assets/readme-images/delete-comment-pop-up.png)

Delete pop-up message confirmation.


![View after choosing back deleting](/assets/readme-images/delete-comment-back.png)

View after choosing back deleting.


![View after deleting comment](/assets/readme-images/deleted-comment.png)

View after deleting comment.


![Delete option view for different user than author](/assets/readme-images/delete-comment-other-user-logged-in.png)

Delete option view for different user than author of comment.


- Responsive on all device sizes and has interactive elements.

    - Web, Ipad Air and Iphone 12 pro.

![Welcome image](/assets/readme-images/first-run.png)

Web.


![Ipad Air view](/assets/readme-images/ipad-air.png)

Ipad.


![Iphone 12 pro view](/assets/readme-images/iphone-12-pro.png)

Iphone 12 pro.


![Navbar open menu](/assets/readme-images/iphone-12-pro-open-menu.png)

Navbar open menu.

- Admin Back-end

    - Allows the admin to do CRUD in the back-end of the site. with special effect in Comments and Events("Posts")

![Admin image](/assets/readme-images/admin.png)

Admin image.


![Admin Comments section](/assets/readme-images/admin-comment.png)

Admin Comments section.


![Admin Events section](/assets/readme-images/admin-event.png)

Admin Events section.


![Admin Events edit section](/assets/readme-images/admin-event-edit.png)


Admin Events edit section.

![Database schema](/assets/readme-images/database-schema.png)

- The Comment model is connected with the post attribute as a foreign key to the Model Post, so there is a direct relation for each session to have exclusive comments, if the session is deleted, also the comments from that session will be deleted. The new model for resubmission consists in a Contact model for Contact form that will allow any user, no need of being logged in, to contact the admin, with name, subject, email, and body text as requirement. This form will be submitted to the back end.


## Features Left to Implement

- Allow the user to change the password.
- Allow the user to recover the password.
- Updated comment message "waiting to be approved".


### Bugs

- If a Logged-in User comments a posta and after that the Admin approves the comment, then the user refreshes the page, the message "comment waiting for approval" will still be there instead of the possibility to create a new comment. For this the user needs to go home and then back to the event page to be able to comment again.

- After final deployment, css was not being shown. First problem was that "X_FRAME_OPTIONS = 'SAMEORIGIN'" was writen with "``" instead. Second problem was that in base.html "<link rel="stylesheet" type="text/css" href=" {% static 'css/style.css' %} ">" was written like <link rel="stylesheet" type="text/css" href=" {% static '/css/style.css' %} "> instead. Bug Fixed.


## Deployment

- The site was deployed to heroku.com using Code Institute's mock terminal for Heroku. For this it is needed to install Django and supporting libraries, create a new blank Django project and app, set the project to use cloudinary and PostgreSQL and deploy to heroku.

1. In Git terminal: 'pip3 install 'django<4' gunicorn'
2. 'pip3 install dj_database_url psycopg2'command for database and conection of PostgreSQL
3. 'pip3 install dj3-cloudinary-storage' command for installing cloudinary for keeping photos online.
4. 'pip3 freeze --local > requirements.txt' command needed for deployment in heroku.
5. 'django-admin startproject subtevents .' command to create a neww django project with its name.
6. 'python4 manage.py startapp events' for command creating the app.
7. In subtevents, in settings.py, in installed apps add 'events'.
8. 'python3 manage.py migrate' command for migrating changes and adding them to database.
9. Deploying in heroku, create new app.
10. In resources search for postgress to add database.
11. In settings reveal config vars.
12. Copy string from DATABASE_URL
13. In git at the same level as manage.py create env.py.
14. In env.py we store secret environment variables.
15. env.py should be inside .gitignore
16. in env.py import os and create "os.environ["DATABASE_URL] = string from DATABASE_URL"
17. Add secret key "os.environ["SECRET_KEY"] = Secret key"
18. In heroku config vars add SECRET_KEY.
19. Reference env.py in settings.py
20. In settings.py change SECRET_KEY to "SECRET_KEY = os.environ.get('SECRET_KEY')"
21. In settings.py add new section "DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}" 
22. run "python3 manage.py migrate" Now the database is connected to heroku.
23. For cloudinary set up Cloudinary Visit the Cloudinary website.
24. Click on the Sign Up For Free button
25. Provide your name, email address and choose a password
26. For Primary interest, you can choose Programmable Media for image and video API
27. Optional: edit your assigned cloud name to something more memorable
28. Click Create Account
29. Verify your email and you will be brought to the dashboard.
30. In cloudinary dashboard copy environment variable without "CLOUDINARY_URL=.
31. In env.py add 'os.environ["CLOUDINARY_URL"] = "environmentvariable"'.
32. Add same variable in heroku.
33. Add in heroku config vars "DISABLE_COLLECTSTATIC = 1" (removed at final deployment) for correct deployment.
34. In settings.py in installed apps we add cloudinary. First one in the top of django staticfiles and the other one in the bottom:
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'events',
]

35. Connect django with cloudinary as follow:

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
 
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

36. We need to tell django where our templates will be store, in settings.py under BASE_DIR:
 
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
 
37. we change DIRS in TEMPLATES in settings.py:

'DIRS': [TEMPLATES_DIR],

38. ADD heroku host name into allowed hosts in settings.py:
 
ALLOWED_HOSTS = ['subtevents.herokuapp.com', 'localhost']

39. Create 3 directories in the top level. Media, Static and Templates.
40. Create procfile "web: gunicorn subtevents.wsgi".
41. Git add ., git commit, git push.
42. In heroku dashboard, in the deploy tab, click on github, search the correct project repository, connect with it and finally deploy the branch.
43. Work in the project.
44. For final deployment in settings.py "DEBUG = False" and "X_FRAME_OPTIONS = ‘SAMEORIGIN’".
45. Erase DISABLE_COLLECSTATIC in heroku config vars.
46. In heroku deploy tab, manual deploy, deploy branch. 


## PEP8 and HTML, CSS validators and lighthouse

### PEP8

- events/admin.py
![PEP8 events admin.py](/assets/readme-images/pep8-adminpy.png)

- events/apps.py
![PEP8 events apps.py](/assets/readme-images/pep8-appspy.png)

- events/forms.py
![PEP8 events forms.py](/assets/readme-images/pep8-formspy.png)

- events/models.py
![PEP8 events models.py](/assets/readme-images/pep8-modelspy.png)

- events/urls.py
![PEP8 events urls.py](/assets/readme-images/pep8-urlspy.png)

- events/views.py
![PEP8 events views.py](/assets/readme-images/pep8-views.png)

- subtevents/asgy.py
![PEP8 subtevents asgy.py](/assets/readme-images/pep8-asgi.png)

- subtevents/settings.py
![PEP8 subtevents settings.py](/assets/readme-images/pep8-settingspy.png)

- subtevents/urls.py
![PEP8 subtevents urls.py](/assets/readme-images/pep8-urls2py.png)

- subtevents/wsgi.py
![PEP8 subtevents wsgi.py](/assets/readme-images/pep8-wsgipy.png)

- manage.py
![PEP8 manage.py](/assets/readme-images/pep8-managepy.png)

### W3C CSS

- CSS
![W3C CSS Validator](/assets/readme-images/w3c-css.png)

### W3C HTML

- HTML
![W3C HTML Validator](/assets/readme-images/html-validator.png)

- Lighthouse
![Developers lighthouse](/assets/readme-images/lighthouse.png)


## Dependencies, frameworks, languages and django packages used

- Code Institute template used for ability to deploy the program correctly in Heroku.
- HTML and Bootsrap, CSS, DJANGO, PYTHON, Javascript and Jquery.
- Config Vars: Key = PORT, value = 8000 improve compatibility with various Python libraries in heroku. 
- Gunicorn for heroku server, Crispy forms for comments section, Allauth for user registration and Login/Loggout, Summernote for admin text editor for the events content, Psycopg2 connect PostgreSQL with Python, Cloudinary for saving media in the cloud. Dj_database_url for DATABASE_URL environment variable to configure your Django application.
- Git for coding commit and pushing to Github, Github for project code repository store, Heroku python deployment to web, PostgreSQL database.

## Credits

- All code was done by the student with the support of Code Institute classes, following "I think there I blog" project construction adaptation for ΠΛΤΤ Sessions.

- Comment model was managed and built by the help of the student mentor and Pedro Cristo Portafolio project 4 from Code Institute. 

- All Media content was done and uploaded by the student.

- Code Institute and heroku for deployment terminal.
