# ΠΛΤΤ Sessions

This events blog style, for the Full Stack Project from Code Institue, consist in showing and allowing the users to see different events produced by ΠΛΤΤ at Rex Malmo Bar. Each event is shown in the principal page with a flyer. This flyer show the location, different djs that will play in future events or already played, dates and times. The user is able to click and see different media and informatiom from each event, including: photos, videos, guest dj, bibliography, social media and an embedded souncloud set with the music played in the event. Also the user is able to register and login in the site, this will allow them to like and comment each event. Finally the user will be able update personal comments or delete them.

[Here is the live version of my project](https://project-3-exam-results.herokuapp.com/)***

![Welcome image](/assets/readme-images/first-run.png)

## User Stories, Project Goals, Agile Metodology and Diagram for UX

### Project Goals

- Create a full Stack project based on an Event Blog Style application.

- External User's goal:
    - User wants to see what's going on at ΠΛΤΤ Sessions in Rex Malmo Bar, also be able to like and comment in different events.

- Site owner's goals:
    - ΠΛΤΤ wants to have a platform to show to the users media from the differents events, connect with them and generate discussion in the community.

- Potential features to include:
    - Create different events.
    - Like and view likes from different events.
    - Comment events.
    - Follow Social Media from different Djs
    - Include photos, videos and audio from the events.
    - See different comments with the time/date of the comment aswell as the author.

### User Stories 

1. Manage Events:
    - As a Admin I can create, read, update and delete events so that I can manage my event site.

2. Create Drafts:
    - As a Admin I can create draft events so that I can finish uploading the content later.

3. Approve Comments.
    - As a role I can approve or disapprove comments so that I can filter out objectionable comments.

4. Site Pagination:
    - As a Site User I can view a paginated list of events so that easily select a post to view.

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
    - As a Site User I can see and/or listen to different media from the event so that I can understand and feel how was the event.

### [Agile Metodology used to accomplish the goals from the project via User Stories](https://github.com/matiasconsiglio/project-4/projects/1)

### Diagram for UX design

![Diagram for Ux Design](/assets/readme-images/diagram.png)

- All the special pages for login, register, logout and update comment should share the same navbar and footer as the main view.

## Features

### Existing Features Tested Manually and Messages for User

-  Welcomes the user to the events blog "ΠΛΤΤ Sessions".

    - Has a Logo with link to the home page.
    - Has a register and login option for the user in the navbar.
    - Has a Home link to the home page.
    - Shows the differents events that already happened and the ones to come.
    - Shows the different likes each event has.
    - Allows the user to click in "Session #number" to go inside each event and see different information and media from it.
    - Show the social media from ΠΛΤΤ Sessions for users to be able to reach and follow.
    - In case the user is logged in, the navbar won't show register and login, instead will show the option Logout.

![First blog approach](/assets/readme-images/first-run.png)

First blog approach.


![Blog Logout](/assets/readme-images/first-run-logout.png)

Blog log out option and message.


- Register for User.

    - Special design page that allows the user to register to ΠΛΤΤ Sessions.
    - Explanation to the user in case they already have and account, button option to go to sign in page.
    - Username, password and password confirmation required.
    - User email input as optional.
    - Sign up button for confirmation.
    - Message shown in case name of user already exist.
    - Navbar and footer keeps the style of welcome page.
    - Link that allows you to go to the sign in page in case you already have an account created.

 
![Registration](/assets/readme-images/register.png)

Register page with link to sign in page.


![User already exist](/assets/readme-images/user-exist.png)

User already exist message.


- Login for User.

    - Special design page that allows the user to Login to ΠΛΤΤ Sessions.
    - User and Password required
    - Remember me checkbox
    - Sign in button
    - Message shown in case the username or password is incorrect.
    - Navbar and footer keeps the style of welcome page.
    - Link that allows you to go to the register page in case you don't have an account created.

![Login](/assets/readme-images/login.png)

Login Page with message and link for register.


![Incorrect login](/assets/readme-images/incorrect-login.png)

Incorrect loggin. 


- Logout

    - Logout message asking the user if its sure they want to logout.
    - Sign out button.
    - Navbar and footer keeps the style of welcome page.
    - Once Sign Out is clicked the user is redirected to the home page.


![Logout](/assets/readme-images/logout.png)

Sign out confirmation page.


![Home](/assets/readme-images/first-run.png)

Redirect to home after sign out.


- Event

    - Number of likes and comments.
    - Possibility to see comments from different users.
    - Navbar and footer keeps the style of welcome page.
    - Flyer of the event.

    - Depending on the event, the post can have:
        - None, one or more guest Dj.
        - Bio of different guest Dj.
        - Social Media from guest Dj.
        - Photos and embedded videos from Youtube and sound from Soundcloud.
        - ΠΛΤΤ media including photos, videos or/and audio.

    - For all events if user is logged in:
        - Posibility to comment and wait for approval from Admin of the comment.
        - If the user already commented and the comment was approved; posibility of updating and/or deleting the same user comment.
        - Like the event.
 
![Event post intro plus like option](/assets/readme-images/session2-1.png)

Event first view liked by user.


![Home page with like](/assets/readme-images/home-like.png)

Home page with like.


![Event guest dj video and audio](/assets/readme-images/session2-2.png)

Guest dj media.


![Matt media 1](/assets/readme-images/mattmedia1.png)

ΠΛΤΤ media.


![Matt media 2](/assets/readme-images/mattmedia2.png)

ΠΛΤΤ media.


![Matt media 3](/assets/readme-images/mattmedia3.png)

ΠΛΤΤ media.


![Logged in comment view](/assets/readme-images/loggedin-comment-view.png)

Logged in comment view.


![Logged in commented waiting for approval](/assets/readme-images/comment-view-waiting-approval.png)

Logged in comment sent waiting for approval.


![Logged in comments view](/assets/readme-images/loggedin-comment-approved.png)

Logged in comment section after approval.


![Logged out comment view](/assets/readme-images/logged-out-comment-view.png)

Logged out comment section.


- Update comment.
    - Only available for logged in user and for updating own user comment.
    - Sends you to another page to update and send your new comment
    - New comment needs approval.
    - Old comment gets deleted.

![Logged in comments view](/assets/readme-images/loggedin-comment-approved.png)

Logged in comment section after approval.


![Update comment view](/assets/readme-images/update-comment.png)

Update comment view.


![Update comment waiting for approval](/assets/readme-images/update-comment-waiting-approval.png)

Update comment waiting for approval.


![Update comment view after approval](/assets/readme-images/update-comment-approved.png)

Update comment view after approval.


![Different user logged in comments view](/assets/readme-images/different-user-logged-comment-view.png)

Different user logged in comments view.

  
- Delete comment.
   - Only available for logged in user and for deleting own user comment.
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

    - Web, ipad Air and Iphone 12 pro.

![Welcome image](/assets/readme-images/first-run.png)

Web.


![Ipda Air view](/assets/readme-images/ipad-air.png)

Ipad.


![Iphone 12 pro view](/assets/readme-images/iphone-12-pro.png)

Iphone 12 pro.


![Navbar open menu](/assets/readme-images/iphone-12-pro-open-menu.png)

Navbar open menu.


## Features Left to Implement

- Allow the user to change password.
- Allow the user to recover password.
- Updated comment message "waiting to be approved".


### Bugs

- If a Logged-in User comments a posta and after that the Admin approves the comment, then the user refresh the page, the message "comment waiting for approval" will still be there instead of the posibility to create a new comment. For this the user needs to go home and then back to the event page to be able to comment again.


## Deployment

- The site was deployed to heroku.com using Code Institute's mock terminal for Heroku.

    1. Each input in the run.py must end with "\n" so the input line for each input appears in heroku.
    2. All the dependencies installed through the Code Institute template and both gspread and google-auth in Github must be installed in heroku also for the program to work. For this in the terminal "pip3 freeze > requirements.txt" must be typed. Requirement.txt bus be correctly spelled because heroku while loading the program will search for the dependencies in this folder to install them and then after allowing the code to run.
    3. Git add . command plus git commit -m "Add requirements for deployment." and git push commands must be input to the terminal.
    4. Create an account in heroku.com
    5. Input name, last name, email address, student role, country in this case Sweden and Python as primary development language. Finally reCAPTCHA and create an account.
    6. Confirm account in email.
    7. Create password and Login.
    8. Accepts terms and services.
    9. Create the first app from heroku dashboard.
    10. Select a unique name for the app and region, in this case "Europe".
    11. App created.
    12. Go to the Settings tab.
    13. Go to Config Vars.
    14. Add 2: first one Key = CREDS and value will be all the information inside the file creds.json that includes private data saved in .gitignore. Second one Key = PORT, value = 8000. This one to improve compatibility with various Python Libraries.
    15. Add dependencies needed directly from heroku directly from "Add buildpack".
    16. First one needed is Python.
    17. Second one needed is "nodejs", which handles the mock terminal code provided.
    18. Python buildpack must be first in order in the list, second nodejs.
    19. In the Github terminal command: heroku login -i
    20. Command: email and password.
    21. Command: heroku apps.
    22. Command: heroku git:remote - project-3-exam-results
    23. Command: git add . && git commit -m "Deploy to heroku via CLI".
    24. Command: git push origin main
    25. Command: git push heroku main

## Dependencies

- Code Institute template used for ability to deploy the program correctly in Heroku.
- Gspread, Google API used to be able to communicate python in Github with google sheets. CREDS.json are the private credentials used so the program could connect with spreadsheets in a private gmail.com account in google drive.
- Config Vars: Key = PORT, value = 8000 improve compatibility with various Python libraries in heroku. 
- Python and nodejs, that handles the mock terminal code provided, added in Heroku via "buildpacks".

## Credits

- All code was done by the student with the support of Code Institute classes, love-sandwiches project and his mentor. 

- All Media content was done and uploaded by the student.

- Code Institute and heroku for deployment terminal.

