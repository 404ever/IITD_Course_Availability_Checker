from bs4 import BeautifulSoup           # not a part of the python lib need to install explicitely  (check your respective OS instructoion to install BeautifulSoup)
import requests                         # not a part of the python lib need to install explicitely  (check your respective OS instructoion to install requests)
import pygame as pg                     # not a part of the python lib need to install explicitely  (check your respective OS instructoion to install pygame)
import warnings                         # part of the python lib no need to install explicitely
import sched                            # part of the python lib no need to install explicitely
import time                             # part of the python lib no need to install explicitely

hul_dictionary = {'HUL211': '156', 'CLL786': '55', 'HUL231': '78'}    # here add as many courses as you want to check their avaliability, they can be any course either DE, OC or HUL etc, 
                                                                      # just put course name as key and maximum allowed course limit as value for that key
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
    for course in hul_dictionary:                                               # traverse the dictionary for each key (course code in our case)
        url = 'https://academics1.iitd.ac.in/Academics/index.php?page=ListCourse&secret=351e0cd3dcbdfa6cd4e21e4776e4986c75fc47ae&uname=2013CH10083'    # Warning   ::::::::
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! you need to change this url, to get your unique url see instruction in readme file, feel free to contact/comment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
            print(student_registered)
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
    s.enter(60, 1, main_function, (sc,))                                            # here I added timer as 60 sec, so this script 
                                                                                    # runs in every 60 sec intervel to check updates in IIT database for course avaliability
s.enter(60, 1, main_function, (s,))                                                 # and will start playing GOT ringtone as a notification
s.run()


