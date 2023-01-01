Ivy is a multi-user platform that allows users to keep track of the jobs they've applied to in an easily readable format. Users can sign up, log in, edit their profile, and on the homepage they can add job applications, which will have a status label, date of application, and link to each company.
Each company has a page that users can leave comments on giving their experience about the interview process/working there.


I'm going to try to build a function to automatically scan your email to check the status of jobs, and maybe even add new jobs you've applied to. This will work by checking for emails that say "thank you for applying to xxx" or emails with the keyword hackerrank or something like that.

Initial CSS of the homepage:
![ivy](https://user-images.githubusercontent.com/73012906/201748484-74e17269-4223-4ab4-a466-2aec0b4f5829.jpeg)


11/16/2022
I've web scraped a little over 1400 companies and added them to the database using python.
I've also updated the home page CSS
![image](https://user-images.githubusercontent.com/73012906/202124295-de817eec-ed1f-40bc-adf0-d5c281ac2706.png)


Installation and setup:
(Assuming you have latest version of python, pip and virtualenv installed)
1. Clone repo to designated directory, navigate into directory
2. create/activate virtual environment
3. run command to install dependencies: pip install -r requirements.txt
4. run command to start server: python manage.py runserver
5. navigate to localhost:8000 on your browser to see functioning project!



