#!/usr/bin/env python3
import gpio as GPIO
import sounddevice as sd
import soundfile
import subprocess
import numpy as np
import os
import vlc
import time
import sys
from pydub import AudioSegment
from precise_runner import PreciseEngine, PreciseRunner
from vv.recognizer import Voice_Recognizer

from English.time.time import Tind
from English.what.what import SSD
from English.set_face_who.Add_Face import Recognizer
from English.money.yolov5.money import Money
from English.online_features.online_feature import Reader
#from English.change_language.change_language import CHLANG
from English.change_language.change_language_voice import CHLANG
from English.colors.colors import Color_detection
from play_audio import GTTSA
from config import *

#sys.path.insert(0, '/home/rock/Desktop/Hearsight/English/machine_voice/')
#from machine_voice import MachineVoices
#machineVoice_obj = MachineVoices()

os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")

time_obj = Tind()
what_obj = SSD()
face_obj = Recognizer()
mon_obj = Money()
color_obj = Color_detection()
online_feature_obj = Reader()
play_audio = GTTSA()
lang_obj = CHLANG()

cmd_rec = Voice_Recognizer()
choices = ["Yes_boss","Ready_To_Help","At_Your_Service","How_can_i_help?"]

GPIO.setup([450, 421, 447, 448, 502], GPIO.IN)

def greeting():
    greet = np.random.choice(choices)
    play_audio.play_machine_audio(f"{greet}.mp3")
    
#def handle_money_feature():
#    counts = 1
#    play_audio.play_machine_audio("press_feature_button.mp3")
#
#    while True:
#        input_state1 = GPIO.input(450)
#        input_state2 = GPIO.input(421)
#        input_state3 = GPIO.input(447)
#        input_state4 = GPIO.input(448)
#        
#        if input_state1:
#            counts = (counts + 1) % 2
#            play_audio.play_machine_audio("single.mp3" if counts == 0 else "multi.mp3")
#        
#        if input_state2:
#            counts = (counts - 1) % 2
#            play_audio.play_machine_audio("single.mp3" if counts == 0 else "multi.mp3")
#            
#        if input_state3 == True and counts == 0:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            mon_obj.pred()
#            break    
#        
#        if input_state3 == True and counts == 1:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            mon_obj.pred_1()
#            break
#    
#        if input_state4 == True:
#            play_audio.play_machine_audio("feature_exited.mp3")
#            break
#        
#    play_audio.play_machine_audio("Thank You.mp3")

#def handle_face_feature():
#    counts = 1
#    play_audio.play_machine_audio("press_feature_button.mp3")
#
#    while True:
#        input_state1 = GPIO.input(450)
#        input_state2 = GPIO.input(421)
#        input_state3 = GPIO.input(447)
#        input_state4 = GPIO.input(448)
#
#        if input_state1:
#            counts = (counts + 1) % 2
#            play_audio.play_machine_audio("Add_face.mp3" if counts == 0 else "delete face.mp3")
#
#        if input_state2:
#            counts = (counts - 1) % 2
#            play_audio.play_machine_audio("Add_face.mp3" if counts == 0 else "delete face.mp3")
#
#        if input_state3 == True and counts == 0:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#
#            while len(face_obj.persons) <= 200:
#                face_obj.add_person()
#                break
#            break
#
#        if input_state3 == True and counts == 1:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            face_obj.remove_person()
#            break
#
#        if input_state4 == True:
#            play_audio.play_machine_audio("feature_exited.mp3")
#            break
#
#    play_audio.play_machine_audio("Thank You.mp3")

#def handle_face_feature():
#    counts = -1
#    play_audio.play_machine_audio("press_feature_button.mp3")
#
#    while True:
#        input_state1 = GPIO.input(450)
#        input_state2 = GPIO.input(421)
#        input_state3 = GPIO.input(447)
#        input_state4 = GPIO.input(448)
#        
#        if input_state1:
#            counts = (counts + 1) % 3
##                self.play_audio.play_machine_audio("Add_face.mp3" if counts == 0 else "delete face.mp3")
#            play_audio.play_machine_audio("Add_face.mp3" if counts == 0 else "who_is_this.mp3" if counts == 1 else "delete face.mp3")
#        
#        if input_state2:
#            counts = (counts - 1) % 3
#            play_audio.play_machine_audio("Add_face.mp3" if counts == 0 else "who_is_this.mp3" if counts == 1 else "delete face.mp3")
#            
#        if input_state3 == True and counts == 0:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#                
##            while len(face_obj.persons) <= 200:
#            face_obj.add_person()
#            play_audio.play_machine_audio("Thank You.mp3")
##                break
##            break
#        
#        if input_state3 == True and counts == 1:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            face_obj.recognize()
#            play_audio.play_machine_audio("Thank You.mp3")
##                break
#        
#        if input_state3 == True and counts == 2:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            face_obj.remove_person()
#            play_audio.play_machine_audio("Thank You.mp3")
##                break
#    
#        if input_state4 == True:
#            play_audio.play_machine_audio("feature_exited.mp3")
#            play_audio.play_machine_audio("Thank You.mp3")
#            break
#        
##        self.play_audio.play_machine_audio("Thank You.mp3")
#
#def settings():
#        counts = -1
#        play_audio.play_machine_audio("press_feature_button.mp3")
#    
#        while True:
#            input_state1 = GPIO.input(450)
#            input_state2 = GPIO.input(421)
#            input_state3 = GPIO.input(447)
#            input_state4 = GPIO.input(448)
#            
#            if input_state1:
#                counts = (counts + 1) % 5  # Use % 5 since you have 5 cases
#                audio_files = [
#                    "change_language.mp3",
#                    "user_guide.mp3",
#                    "volume.mp3",
#                    "battery_percentage.mp3",
#                    "temperature.mp3"
#                ]
#                audio_file = audio_files[counts]
#                play_audio.play_machine_audio(audio_file)
#
#            if input_state2:
#                counts = (counts - 1) % 5  # Use % 5 since you have 5 cases
#                audio_files = [
#                    "change_language.mp3",
#                    "user_guide.mp3",
#                    "volume.mp3",
#                    "battery_percentage.mp3",
#                    "temperature.mp3"
#                ]
#                audio_file = audio_files[counts]
#                play_audio.play_machine_audio(audio_file)
#                
#            if input_state3 == True and counts == 0:
#                play_audio.play_machine_audio("feature_confirmed.mp3")
#                lang_obj.handle_lang()
#                play_audio.play_machine_audio("Thank You.mp3") 
##                break
#            
#            if input_state3 == True and counts == 1:
#                play_audio.play_machine_audio("feature_confirmed.mp3")
#                os.system("python /home/rock/Desktop/Hearsight/English/user_guide/user_guide.py")
#                play_audio.play_machine_audio("Thank You.mp3") 
##                break
#            
#            if input_state3 == True and counts == 2:
#                play_audio.play_machine_audio("feature_confirmed.mp3")
#                os.system("python /home/rock/Desktop/Hearsight/English/volume/volume.py")
#                play_audio.play_machine_audio("Thank You.mp3") 
##                break
#            
#            if input_state3 == True and counts == 3:
#                play_audio.play_machine_audio("feature_confirmed.mp3")
#                os.system("python /home/rock/Desktop/Hearsight/English/battery/battery_mean.py")
#                os.system("python /home/rock/Desktop/Hearsight/English/battery/battery_raw.py")
#                play_audio.play_machine_audio("Thank You.mp3") 
##                break
#            
#            if input_state3 == True and counts == 4:
#                play_audio.play_machine_audio("feature_confirmed.mp3")
#                os.system("python /home/rock/Desktop/Hearsight/English/temperature/temperature.py")
#                play_audio.play_machine_audio("Thank You.mp3") 
##                break
#                    
#            if input_state4 == True:
#                play_audio.play_machine_audio("feature_exited.mp3")
#                play_audio.play_machine_audio("Thank You.mp3")
#                break
            
#        play_audio.play_machine_audio("Thank You.mp3")

#def handle_read_features(feature_name):
#    counts = 0
#    play_audio.play_machine_audio("press_feature_button.mp3")
#
#    while True:
#        input_state1 = GPIO.input(450)
#        input_state2 = GPIO.input(421)
#        input_state3 = GPIO.input(447)
#        input_state4 = GPIO.input(448)
#
#        if input_state1:
#            counts = (counts + 1) % 2
#            play_audio.play_machine_audio(f"read_{feature_name}.mp3" if counts == 1 else f"delete_{feature_name}.mp3")
#
#        if input_state2:
#            counts = (counts - 1) % 2
#            play_audio.play_machine_audio(f"read_{feature_name}.mp3" if counts == 1 else f"delete_{feature_name}.mp3")
#
#        if input_state3 and counts == 1:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            online_feature_obj.play_audio(feature_name)
#            play_audio.play_machine_audio("Thank You.mp3")
#            break
#
#        if input_state3 and counts == 0:
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            online_feature_obj.remove_file(feature_name)
#            play_audio.play_machine_audio("Thank You.mp3")
#            break
#
#        if input_state4:
#            play_audio.play_machine_audio(f"exit_{feature_name}.mp3")
#            play_audio.play_machine_audio("Thank You.mp3")
#            break

#def hearsight_storage():
#    counts = 0
#    play_audio.play_machine_audio("press_feature_button.mp3")
#    
#    while True:
#        input_state1 = GPIO.input(450)
#        input_state2 = GPIO.input(421)
#        input_state3 = GPIO.input(447)
#        input_state4 = GPIO.input(448)
#    
#        if input_state1:
##                sleep(1)
#            counts = (counts + 1) % 2
#            play_audio.play_machine_audio("document.mp3" if counts == 1 else "media.mp3")
#
#        if input_state2:
##                sleep(1)
#            counts = (counts - 1) % 2
#            play_audio.play_machine_audio("document.mp3" if counts == 1 else "media.mp3")
#
#        if input_state3 and counts == 1:
##                sleep(1)
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            handle_document_features()
##                self.online_feature_obj.play_audio(feature_name)
##                self.play_audio.play_machine_audio("Thank You.mp3")
##                break
#
#        if input_state3 and counts == 0:
##                sleep(1)
#            play_audio.play_machine_audio("feature_confirmed.mp3")
#            handle_media_features()
##                self.online_feature_obj.remove_file(feature_name)
##                self.play_audio.play_machine_audio("Thank You.mp3")
##                break
#        
#        if input_state4:
##                sleep(1)
#            play_audio.play_machine_audio("feature_exited.mp3")
#            play_audio.play_machine_audio("Thank You.mp3")
#            break

def handle_document_features():
    counts = 0
    play_audio.play_machine_audio("press_feature_button.mp3")
    
    while True:
        input_state1 = GPIO.input(450)
        input_state2 = GPIO.input(421)
        input_state3 = GPIO.input(447)
        input_state4 = GPIO.input(448)
    
        if input_state1:
#                sleep(1)
            counts = (counts + 1) % 2
            play_audio.play_machine_audio("read_document.mp3" if counts == 1 else "delete_document.mp3")

        if input_state2:
#                sleep(1)
            counts = (counts - 1) % 2
            play_audio.play_machine_audio("read_document.mp3" if counts == 1 else "delete_document.mp3")

        if input_state3 and counts == 1:
#                sleep(1)
            feature_name = "document"
            play_audio.play_machine_audio("feature_confirmed.mp3")
            online_feature_obj.play_audio(feature_name)
            play_audio.play_machine_audio("Thank You.mp3")
            break

        if input_state3 and counts == 0:
#                sleep(1)
            feature_name = "document"
            play_audio.play_machine_audio("feature_confirmed.mp3")
            online_feature_obj.remove_file(feature_name)
            play_audio.play_machine_audio("Thank You.mp3")
            break
        
        if input_state4:
#                sleep(1)
            play_audio.play_machine_audio("exit_document.mp3")
            play_audio.play_machine_audio("Thank You.mp3")
            break
        
def handle_media_features():
    counts = 0
    play_audio.play_machine_audio("press_feature_button.mp3")
    
    while True:
        input_state1 = GPIO.input(450)
        input_state2 = GPIO.input(421)
        input_state3 = GPIO.input(447)
        input_state4 = GPIO.input(448)
    
        if input_state1:
#                sleep(1)
            counts = (counts + 1) % 2
            play_audio.play_machine_audio("read_media.mp3" if counts == 1 else "delete_media.mp3")

        if input_state2:
#                sleep(1)
            counts = (counts - 1) % 2
            play_audio.play_machine_audio("read_media.mp3" if counts == 1 else "delete_media.mp3")

        if input_state3 and counts == 1:
#                sleep(1)
            feature_name = "media"
            play_audio.play_machine_audio("feature_confirmed.mp3")
            online_feature_obj.play_audio(feature_name)
            play_audio.play_machine_audio("Thank You.mp3")
            break

        if input_state3 and counts == 0:
#                sleep(1)
            feature_name = "media"
            play_audio.play_machine_audio("feature_confirmed.mp3")
            online_feature_obj.remove_file(feature_name)
            play_audio.play_machine_audio("Thank You.mp3")
            break
        
        if input_state4:
#                sleep(1)
            play_audio.play_machine_audio("exit_media.mp3")
            play_audio.play_machine_audio("Thank You.mp3")
            break

def save_predict():
    greeting()
    match, conf = cmd_rec.recognize()

    if match in ["change language", "language"]:
        print(match)
        match = "change_language"

    if match in ["time", "date", "time and date", "time a date", "time an date"]:
        print(match)
        match = "time_and_date"

    if match in ["walk", "walking", "barking", "parking", "marking", "king"]:
        print(match)
        match = "walk"

    if match in ["money"]:
        print(match)
        match = "money"
        
    if match in ["colors", "color", "colours", "colour", "carla", "carlos", "caller", "corner", "colar"]:
        print(match)
        match = "colors"

    if match in ["add face", "add"]:
        print(match)
        match = "Add_face"
        
    if match in ["delete face", "delete"]:
        print(match)
        match = "delete face"
        
#    if match in ["settings", "set", "letting thing", "thing"]:
#        print(match)
#        match = "settings"

    if match in ["who", "who is this"]:
#    if match in ["person", "per son"]:
        print(match)
        match = "who_is_this"

    if match in ["what"]:
        print(match)
        match = "what"

    if match in ["go see", "gosee"]:
        print(match)
        match = "go see"

    if match in ["read"]:
        print(match)
        match = "read"
        
#    if match in ["scan", "can"]:
#        print(match)
#        match = "scan"
        
#    if match in ["up", "application", "app", "mobile", "mobile up", "mobile application", "mobile app"]:
    if match in ["up", "application", "app"]:
        print(match)
        match = "hearsight_app"
        
#    if match in ["storage"]:
#        print(match)
#        match = "hearsight_storage"

    if match in ["document"]:
        print(match)
        match = "document"
        
    if match in ["media"]:
        print(match)
        match = "media"
        
    if match in ["user", "guide", "user guide"]:
        print(match)
        match = "user_guide"
        
    if match in ["volume"]:
        print(match)
        match = "volume"
        
    if match in ["battery", "level", "battery level", "three level", "that ray", "that level"]:
        print(match)
        match = "battery_percentage"
        
    if match in ["way it", "wait", "weight", "right"]:
        print(match)
        match = "wait"

#    if match in ["book"]:
#        print(match)
#        match = "book"
#
#    if match in ["worksheet", "work sheet"]:
#        print(match)
#        match = "work sheet"
#
#    if match in ["bank"]:
#        print(match)
#        match = "bank"

    if match in ["temperature", "device temperature"]:
        print(match)
        match = "temperature"

    if match in ["of", "off"]:
        print(match)
        match = "off"

    print(match, conf, "%")

    if match == "":
        play_audio.play_machine_audio("Sorry could not understand that!.mp3")

    elif match == "out":
#        play_audio.play_machine_audio("exiting_voice_command.mp3")
        play_audio.play_machine_audio("see you next time.mp3")
        play_audio.play_machine_audio("Thank You.mp3")
        play_audio.play_machine_audio("Initializing button command.mp3")
        os._exit(0)

    else:
        if match not in ["wait", "way it", "weight", "right"]:  # Exclude "wait", "way it", "right" and "weight" from playing their audio files
            play_audio.play_machine_audio("{}.mp3".format(match))
            play_audio.play_machine_audio("activated.mp3")
        else:
            # For "wait", "way it", "right" and "weight", only play their audio files without activating
            play_audio.play_machine_audio("okay.mp3")
            os.system("python /home/rock/Desktop/Hearsight/weight.py")

    if match == "Add_face":
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
#        handle_face_feature()
        face_obj.add_person()
        play_audio.play_machine_audio("Thank You.mp3")
        
    if match == "delete face":
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
#        handle_face_feature()
        face_obj.remove_person()
        play_audio.play_machine_audio("Thank You.mp3")
        
#    if match == "settings":
#        settings()

    if match == "time_and_date":
        time_obj.tellTime()
        play_audio.play_machine_audio("Thank You.mp3")

    if match == "walk":
        time.sleep(3)
        os.system("python /home/rock/Desktop/Hearsight/English/walk/walk.py")
        play_audio.play_machine_audio("Thank You.mp3")

    if match == "change_language":
        lang_obj.handle_lang()
        play_audio.play_machine_audio("Thank You.mp3") 

    if match == "who_is_this":
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
#        handle_face_feature()
        face_obj.recognize()
        play_audio.play_machine_audio("Thank You.mp3")

    if match == "what":
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
        what_obj.detect()
        play_audio.play_machine_audio("Thank You.mp3")

    if match == "go see":
        time.sleep(3)
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
        os.system("python /home/rock/Desktop/Hearsight/English/go_see/go_see.py")
        play_audio.play_machine_audio("Thank You.mp3")

    if match == "money":
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
#        handle_money_feature()
        mon_obj.pred_1()
        play_audio.play_machine_audio("Thank You.mp3")
        
    if match == "colors":
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
        color_obj.color_det()
        play_audio.play_machine_audio("Thank You.mp3")
        
    if match == "read":
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
        os.system("python /home/rock/Desktop/Hearsight/English/read/read.py")
        play_audio.play_machine_audio("Thank You.mp3")

#    if match == "scan":
#        os.system("python /home/rock/Desktop/Hearsight/camera_reload.py")
#        b = "python /home/rock/Desktop/Hearsight/English/scan/scan.py"
#        a = os.system(b)
#        play_audio.play_machine_audio("Thank You.mp3")
        
    if match == "hearsight_app":
        os.system("python /home/rock/Desktop/Hearsight/English/hearsight_app/hearsight_app.py")
        play_audio.play_machine_audio("Thank You.mp3")

    if match == "document":
#        handle_read_features(match)
        handle_document_features()
        
    if match == "media":
#        handle_read_features(match)
        handle_media_features()

#    if match == "hearsight_storage":
#        hearsight_storage()
        
    if match == "user_guide":
        os.system("python /home/rock/Desktop/Hearsight/English/user_guide/user_guide.py")
        play_audio.play_machine_audio("Thank You.mp3")
        
    if match == "volume":
        os.system("python /home/rock/Desktop/Hearsight/English/volume/volume.py")
        play_audio.play_machine_audio("Thank You.mp3")
        
    if match == "battery_percentage":
        os.system("python /home/rock/Desktop/Hearsight/English/battery/battery_mean.py")
        os.system("python /home/rock/Desktop/Hearsight/English/battery/battery_raw.py")
        play_audio.play_machine_audio("Thank You.mp3")

#    if match == "book":
#        handle_read_features(match)
#
#    if match == "work sheet":
#        handle_read_features("worksheet")
#
#    if match == "bank":
#        handle_read_features(match)

    if match == "temperature":
        os.system("python /home/rock/Desktop/Hearsight/English/temperature/temperature.py")
        play_audio.play_machine_audio("Thank You.mp3")

    if match == "of" or match == "off":
        os.system("python /home/rock/Desktop/Hearsight/English/off/off.py")

engine = PreciseEngine('/home/rock/Desktop/Hearsight/mycroft-precise/.venv/bin/precise-engine', '/home/rock/Desktop/Hearsight/mycroft-precise/hearsight.pb')
runner = PreciseRunner(engine, trigger_level=5, sensitivity=0.8, on_activation=save_predict)
runner.start()

play_audio.play_machine_audio("welcome to hearsight.mp3")
play_audio.play_machine_audio("Voice command activated.mp3")
  
while True:
    if not GPIO.input(502):
        play_audio.play_machine_audio("feature_exited.mp3")
#        play_audio.play_machine_audio("exiting_voice_command.mp3")
        play_audio.play_machine_audio("see you next time.mp3")
        play_audio.play_machine_audio("Thank You.mp3")
        play_audio.play_machine_audio("Initializing button command.mp3")
        os._exit(0)

while True:
    time.sleep(10)