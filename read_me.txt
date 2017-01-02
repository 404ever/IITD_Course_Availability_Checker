:::::::::: Warning :::::::::: Read the instruction carefull


Mandatory Changes: to check your course avaliability you just need to do 2/Two changes in attached main.py file

(1) Change 1: in line number 9 of main.py file just add your course code and maximum allowed limit for that course 
              example: let's say you want to check course CLL786 and maximum allowed limit for this course is 55 so our line 9 would be hul_dictionary = {'CLL786': '55'} in this case to add more courses use comma for sepration

(2) Change 2:  step 1 -> This is going to be tricky, first logout from your academica1.iitd account
               step 2 -> Then go to https://academics1.iitd.ac.in and login with your id and password
               step 3 -> After login successfull click on last option "List of Registered Students in a Course IInd semester 2016-2017"
               step 4 -> Now you will see a edit-box with label "Enter Course Code" and a button with label "Submit", so far everything is good
               step 5 -> Now for a course "HUL211" and click Submit button and wait for the list of registered students to display
               step 6 -> Last Step, now just copy the urlof this page (of page with list showing) this will be your unique url, put this url in line number 37 of given main.py file



OPTIONAL changes:

(1) to change the timer loop just edit line number 73 and 75, default value is 60 sec aka 1 min
(2) to change music file (must be mp3) put the music file in same folder as three other file and edit the line 64 of given main.py file



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Caution !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

AND LAST BUT NOT LEAST EVERY TIME YOU LOGIN OR LOGOUT, YOU HAVE TO UPDATE YOUR URL AS MENTION ABOVE IN MANDATORY CHANGE 2 AT LINE NUMBER 37 IN MAIN.PY FILE OTHERWISE YOU WILL GET SERVER ERROR SO MUST UPDATE YOUR URL AS DESCIBRD ABOVE