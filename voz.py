#List of voices: say -v ?
import os
def say(msg = "Finish", voice = "Karen"):
    os.system(f'say -v {voice} {msg}')

say("Great! Finally finished, please check the result!") 