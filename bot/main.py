# To run python script type command- python file_name.py (in this case python main.py) don't forget to give the right location of your file
# (Use sublime editor to open all files except GOT.mp3 or see the instruction on repo itself)

from bs4 import BeautifulSoup           # not a part of the python lib need to install explicitely  (check your respective OS instructoion to install BeautifulSoup)
import requests                         # not a part of the python lib need to install explicitely  (check your respective OS instructoion to install requests)
import pygame as pg                     # not a part of the python lib need to install explicitely  (check your respective OS instructoion to install pygame)
import warnings                         # part of the python lib no need to install explicitely
import sched                            # part of the python lib no need to install explicitely
import time                             # part of the python lib no need to install explicitely
import sys
sys.setrecursionlimit(2000)             # this is to increase the maximum iteration depth in python module

# Opening and reading the initialize.txt in buffer mode
total_course = 0
i =0
url = None;
time_intervel = None;
hul_dictionary = {}

with open('initialize.txt','r') as init:
    for line in init:
        if not line.rstrip():
            continue
        if(i == 0):
            total_course = line
            print("Total Course Provided: " + total_course)
        if(i == int(total_course) + 1):
            url = line
        if(i == int(total_course) + 2):
            time_intervel = line
        if(i >0 and i<= int(total_course)):
            key = None
            value = None
            tmp_counter = 0
            for word in line.split():
                if(tmp_counter == 0):
                    key = word
                if(tmp_counter != 0):
                    value = word
                tmp_counter = tmp_counter +1
            hul_dictionary[key] = value
        i = i+1

s = sched.scheduler(time.time, time.sleep)                            # this is the object for system scheduler

def play_music(music_file, volume=0.8):                               # this is our play music function, it will take file as a input
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''                     
    freq = 44100     # audio CD quality                                         # setting up the mixer
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("{} is Playing, Hurry Up!".format(music_file))                    # console message if music is start playing
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))     # if file not found
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)                                                          # check if playback has finished

def main_function(sc):                                                          # our main function
    print("Our Bot/Script is running")
    for course in hul_dictionary:                                               # traverse the dictionary for each key (course code in our case)
        payload = {'EntryNumber': course}                                       # passing the post parameter to server

        with warnings.catch_warnings():                                         # here I'm suppressing unwanted warnings to avoid unwanted confusion
            warnings.simplefilter("ignore")
            r = requests.post(url, data=payload, verify=False)                  # POST with form-encoded data
            
        if(r.status_code == 200):
            # Open a file in write mode
            fo = open("tmp_response_file.txt", "w")
            str = r.text
            fo.write(str)
            # Close opend file
            fo.close()

            text = open("tmp_response_file.txt")
            soup = BeautifulSoup(text.read().lower(), "html.parser")
            max_rows = 0
            for table in soup.findAll('table'):
                number_of_rows = len(table.findAll(lambda tag: tag.name == 'tr' and tag.findParent('table') == table))
                if number_of_rows > max_rows:
                    max_rows = number_of_rows
            student_registered = 0
            student_registered = max_rows-1
                                                                                    # pick a MP3 music file you have in the working folder
            music_file = "GOT.mp3"                                                  # otherwise give the full file path
            # optional volume 0 to 1.0
            volume = 0.8
            limit = int(hul_dictionary[course])
            if(student_registered < limit):
                print('############# ', course, 'is avaliable to add, Hurry Up') 
                play_music(music_file, volume)
        else:
            print("Oh Shit!!! Something wrong with your url or network connection")
    s.enter(time_intervel, 1, main_function (sc))                                 # here I added timer in sec, so this script 
                                                                                  # runs in specified time intervel to check updates in IIT database for course avaliability
s.enter(time_intervel, 1, main_function (s))                                      # and will start playing GOT ringtone as a notification if a course is avilable to add
s.run()

