# ΠΛΤΤ Sessions

This events blog style, for the Full Stack Project from Code Institue, consist in showing and allowing the users to see different events produced by ΠΛΤΤ at Rex Malmo Bar. Each event is shown in the principal page with a flyer. This flyer show the location, different djs that will play in future events or already played, dates and times. The user is able to click and see different media and informatiom from each event, including: photos, videos, guest dj, bibliography, social media and an embedded souncloud set with the music played in the event. Also the user is able to register and login in the site, this will allow them to like and comment each event. Finally the user will be able update personal comments or delete them.

[Here is the live version of my project](https://project-3-exam-results.herokuapp.com/)***

![Welcome image](/assets/readme-images/first-run.png)

## User Stories, Project Goals and Agile Metodology

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

## Features

### Existing Features Tested Manually

- Responsive on all device sizes and has interactive elements.

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
![Blog Logout](/assets/readme-images/first-run-logout.png)

- Register for User.

    - Special design page that allows the user to register to ΠΛΤΤ Sessions.
    - Explanation to the user in case they already have and account, button option to go to sign in page.
    - Username, password and password confirmation required.
    - User email input as optional.
    - Sign up button for confirmation.
    - Message shown in case name of user already exist.
    - Navbar and footer keeps the style of welcome page.

 
![Registration](/assets/readme-images/register.png)
![User already exist](/assets/readme-images/user-exist.png)

- Login for User.

    - Special design page that allows the user to Login to ΠΛΤΤ Sessions.
    - User and Password required
    - Remember me checkbox
    - Sign in button
    - Message shown in case the username or password is incorrect.
    - Navbar and footer keeps the style of welcome page.

![Login](/assets/readme-images/login.png)
![Incorrect login](/assets/readme-images/incorrect-login.png)

- Logout

    - Logout message asking the user if its sure they want to logout.
    - Sign out button.
    - Navbar and footer keeps the style of welcome page.


![Logout](/assets/readme-images/logout.png)

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
 
![Event post intro](/assets/readme-images/session2-1.png)
![Event guest dj video and audio](/assets/readme-images/session2-2.png)
- Third Input: Name of first student.

    - Ask the user to input the name of the first student.
    - Ask the user to input the name of the student with just alphabetical characters. "space" is also allowed. Users can enter only First name, Only Last name or both together.
    - Program is not affected by uppercase or lowercase letters.
    - Shows the place for the input.
  
![Third Input: Name of first student](/assets/readme-images/third_input.png)
- Output from Third Input.

    - For this scenario the input was: Matias Castro
    - Output message for valid data.
    - Let the user know that the data is being updated in the grade and results worksheets.
    - Let the user know that the data was successfully updated to worksheets.

![Third Output: Valid student name and name saved to worksheets](/assets/readme-images/third_output.png)
![grade worksheet updated](/assets/readme-images/grade_updated_2.png)
![results worksheet updated](/assets/readme-images/results_updated.png)
- Fourth Input: Score for each question of the first student.

    - Ask the user to input the score for each question of the exam.
    - Ask the user to input the number of "scores" depending on how many questions the user initially input.
    - Explain how the input must be in this case 2 integers separated by comma. If the user input initially 3 questions the program will ask the user to input 3 different scores.
    - Each score must be between 0 and 100.
    - Shows the place for the input.
  
![Fourth Input: Score for each question of first student.](/assets/readme-images/fourth_input.png)
- Output from Fourth Input.

    - For this scenario the input was: score 1 = 55 points and score 2 = 65 points. So: 55,65
    - Output message for valid data.
    - Let the user know that the data is being updated in the grade worksheet.
    - Let the user know that the data was successfully updated to the worksheet.
    - Output result for current student "Matias Castro". Final grade of 61 points and the student passes because the final score is equal or higher than 60 points.
    - Let the user know that the data is being updated in the results worksheet.
    - Let the user know that the data was successfully updated to the worksheet.


![Fourth Output: Valid score per question, final grade, and pass result... Information saved to worksheets](/assets/readme-images/fourth_output.png)
![grade worksheet updated](/assets/readme-images/grade_updated_3.png)
![results worksheet updated](/assets/readme-images/results_updated_2.png)
- Loop Input

    - After grade and exam result for student one, the program will continue asking for all the students names and the scores they got in each one of the questions from the exam.

- Loop Output

    - As the program gives the output of the final grade and the pass result to the first student, it will continue to give the final grade and pass result for each student.
    - Final grade rounded with round() function.

![Loop Input Output: repeat process of input and output for every student.](/assets/readme-images/loop.png)
![Final grade worksheet updated](/assets/readme-images/final_grade.png)
![Final results worksheet updated](/assets/readme-images/final_results.png)

- Running the program again

    - If the user decides to run the program again. At the start of it, the program will clear all the worksheets and add specific titles for each one of them.

![Cleaned quantity worksheet](/assets/readme-images/quantity_initial.png)
![Cleaned grade worksheet](/assets/readme-images/grade_initial.png)
![Cleaned ponderation worksheet](/assets/readme-images/ponderation_initial.png)
![Cleaned results worksheet](/assets/readme-images/results_initial.png)

## Features Left to Implement

- Allow the user to download the google spreadsheets with all the input and output information.
- Combine quantity and ponderation worksheets together.
- Combine grades and results worksheets together.
- Asking for only First and Last name option as student name, both with uppercase in the first letter.

## User Experience (UX)

### User stories as first time visitor goals

- As a First Time Visitor, I want to easily understand the main purpose of the program.
- As a First Time Visitor, I want to be able to navigate throughout the program in an easy way and be able to understand the content.
- As a First Time Visitor, I want to be able to get information back from the program.

### Testing User Stories from User Experience (UX) Section

- As a First Time Visitor, I want to easily understand the main purpose of the program.

    - Users are greeted with a welcome message.
    - Users can have fast access to the instructions and purpose of the program.
    - Users are given examples of what the program does.

- As a First Time Visitor, I want to be able to navigate throughout the program in an easy way and be able to understand the content.

    - The program is giving information and explaining what it expects as input from the user through the whole process.
    - The program is giving feedback continuously through the program via Output for the user to understand what is happening and what comes next.

- As a First Time Visitor, I want to be able to get information back from the program.

    - The program after every input from the user gives an output with precise information for the user to keep a clear understanding of what is happening.

## Testing

- pep8online.com

  - No errors were returned when passing through the official pep8online.com validator.

![PEP8 Validator](/assets/readme-images/pep8online.png)

- Correct input

    - In the Existing Features section, it was shown how the program works and what to expect with correct input. Tested and every feature works properly. In terms of space this process will not be repeated since it was already done.

- Incorrect Input for quantity of students and questions: 

    - Input: not integer, more or less than 2 inputs, less than 1 student or 1 question including negatives.  

![Not integer error](/assets/readme-images/not_int_error_1.png)

![More or less than 2 inputs error](/assets/readme-images/not_2_input.png)

![Less than error](/assets/readme-images/less_than_1.png)

- Incorrect Input for % of each question of ponderation of total grade: 

    - Input: not integer, more or less inputs than quantity of question input, percentage higher than 100 or lower than 0, add of different % resulting different than 100%. 

![Not integer error](/assets/readme-images/ponderation_no_int.png)

![More or less inputs than quantity of question input](/assets/readme-images/ponderation_more_less_inputs.png)

![Percentage higher than 100 or lower than 0](/assets/readme-images/ponderation_outbounds.png)

![Percentage does not add 100](/assets/readme-images/ponderatio_no_100.png)

- Incorrect Input Student Name: 

    - Input: not integer, symbols not alphabetic.

![Student Name int](/assets/readme-images/name_student_int.png)

![Student Name symbol](/assets/readme-images/name_student_symbol.png)

- Incorrect Input for score of each question of the exam: 

    - Input: not integer, more or less inputs than quantity of question input, score higher than 100 or lower than 0.

![Not integer error](/assets/readme-images/score_not_int.png)

![More or less inputs than quantity of question input](/assets/readme-images/score_more_less_inputs.png)

![Score higher than 100 or lower than 0](/assets/readme-images/score_outbounds.png)

- All different scenarios are tested, program will show error to the user if any input is not correct, program will not fail.

### Different View by Device

- Web

![Introduction view web](/assets/readme-images/web.png)
- Ipad Air

![Introduction view ipad air](/assets/readme-images/ipad_air.png)
- Iphone 12 pro

![Introduction view iphone 12 pro](/assets/readme-images/iphone_12_pro.png)
### Bugs

- App won't work properly on smartphones.
- When the user input a negative % with a positive % that adds on 100% for the ponderation input the data was shown as valid. Bug fixed, problem in code line 273 "quantity_ponderation_int = [int(x) for x in ponderation_values]". Used "()" instead of "[]", function was created instead of list. Bug fixed with the help of the mentor.
- Name of student can be first name, last name or both together, no uppercase or lowercase restriction included.
- No more Bugs.

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

## Macro vision of program and work done

![Steps flowchart](/assets/readme-images/flowchart.png)

## Credits

- All code was done by the student with the support of Code Institute classes, love-sandwiches project and his mentor. 

- All Media content was done and uploaded by the student.

- Code Institute and heroku for deployment terminal.

