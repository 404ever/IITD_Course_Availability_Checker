from bs4 import BeautifulSoup
import requests
import pygame as pg
import warnings
import sched
import time

hul_dictionary = {'HUL211': '156', 'HUL212': '78', 'HUL231': '78'}
s = sched.scheduler(time.time, time.sleep)

def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

def main_function(sc):
    for course in hul_dictionary:
        url = 'https://academics1.iitd.ac.in/Academics/index.php?page=ListCourse&secret=7b2bd33083d29c99557995553fd223bb701daa4a&uname=2013CH10083'
        payload = {'EntryNumber': course}

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # POST with form-encoded data
            r = requests.post(url, data=payload, verify=False)

        #status
        r.status_code

        # Open a file in write mode
        fo = open("output_res_file.txt", "w")
        str = r.text
        fo.write(str)
        # Close opend file
        fo.close()

        text = open("output_res_file.txt")
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
        # otherwise give the full file path
        # (try other sound file formats too)
        music_file = "GOT.mp3"
        # optional volume 0 to 1.0
        volume = 0.8
        print(hul_dictionary[course])
        limit = int(hul_dictionary[course])
        print(student_registered < limit)
        if(student_registered < limit):
            print('############# ', course, 'is avaliable to add, Hurry Up') 
            play_music(music_file, volume)
    s.enter(60, 1, main_function, (sc,))

s.enter(60, 1, main_function, (s,))
s.run()