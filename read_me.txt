:::::::::: Warning :::::::::: Read the instruction carefully

To run python script type command- "python file_name.py", don't forget to give the right location of your file
Mandatory Changes: to check your course avaliability you just need to do 2/Two changes in attached main.py file

(1) Change 1: in line number 9 of main.py file just add your course code and maximum allowed limit for that course 
              example: let's say you want to check course CLL786 and maximum allowed limit for this course is 55 so our line 9 would be hul_dictionary = {'CLL786': '55'} in this case to add more courses use comma for sepration

(2) Change 2:  step 1 -> This is going to be tricky, first logout from your academica1.iitd account
               step 2 -> Then go to https://academics1.iitd.ac.in and login with your id and password
               step 3 -> After login successfull click on last option "List of Registered Students in a Course IInd semester 2016-2017"
               step 4 -> Now you will see a edit-box with label "Enter Course Code" and a button with label "Submit", so far everything is good
               step 5 -> Now for a course "HUL211" and click Submit button and wait for the list of registered students to display
               step 6 -> Last Step, now just copy the url of this page (page with list showing) this will be your unique url, put this url in line number 37 of given main.py file



OPTIONAL changes:

(1) to change the timer loop just edit line number 73 and 75, default value is 300 sec aka 5 min
(2) to change music file (must be mp3) put the music file in same folder as three other file and edit the line 64 of given main.py file



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Caution !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

AND LAST BUT NOT LEAST EVERY TIME YOU LOGIN OR LOGOUT, YOU HAVE TO UPDATE YOUR URL AS MENTION ABOVE IN MANDATORY CHANGE 2 AT LINE NUMBER 37 IN MAIN.PY FILE OTHERWISE YOU WILL GET SERVER ERROR SO MUST UPDATE YOUR URL AS DESCIBRD ABOVE

----------------------------------------------------------------------

Requirment:
 to run the script successfully you need to install 4 things python 2, BeautifulSoup, requests and pygame to see the instruction for your specific Operating System Goto these  link (given below), if you get stuck in something then just contact or may be you can do a quick google search for that particular error 
 (I have not tested these links they may work or may not work, if you stuck while installing these package just google that issue you will definetly get your answers if not then contact me)

----------------------------------------------------------------------

Common step to all OS to work behind proxy: set the environment variables for http_proxy and https_proxy

Windows: run in command window (open as admin access)
set http_proxy=http://username:password@10.10.78.22:3128 					// let's say in my case username- ch1130083, password- seriously and 
set https_proxy=https://username:password@10.10.78.22:3128				    //don't forget to change this number 22, 22(Btech), 62(MTech and dual) and 61(Phd)

Linux/OS X: run in terminal
export http_proxy=http://username:password@10.10.78.22:3128
export https_proxy=https://username:password@10.10.78.22:3128

You need to restart your PC after these 2 commands

----------------------------------------------------------------------

For windows:
(1) Python 2.* install: 
http://stackoverflow.com/questions/21372637/installing-python-2-7-on-windows-8 ( answer given by wclear)

(2) pip install:
http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows
https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation

(3) requests install:
http://docs.python-requests.org/en/master/user/install/
https://pypi.python.org/pypi/requests/

(4) BeautifulSoup install:
https://www.quora.com/What-is-the-step-by-step-procedure-to-install-Beautiful-Soup-In-Windows

(5) pygame install:
https://www.webucator.com/blog/2015/03/installing-the-windows-64-bit-version-of-pygame/
http://www.pygame.org/download.shtml
https://inventwithpython.com/pygame/chapter1.html

----------------------------------------------------------------------
For Linux and OSX:
(1) Python 2.* install: 
https://www.cyberciti.biz/faq/install-python-linux/ (linux)
http://docs.python-guide.org/en/latest/starting/install/osx/ (OSX)

(2) pip install:
http://ask.xmodulo.com/install-pip-linux.html (Linux)
pip will automatically get installed when you install python using brew (tested, OSX)

(3) requests install:
http://stackoverflow.com/questions/30362600/how-to-install-requests-module-in-python-3-4-instead-of-2-7  (Linux)
pip install requests (tested, OSX)

(4) BeautifulSoup install:
http://stackoverflow.com/questions/19957194/install-beautiful-soup-using-pip (Linux)
pip install bs4 (tested, OSX)

(5) pygame install:
https://inventwithpython.com/pygame/chapter1.html