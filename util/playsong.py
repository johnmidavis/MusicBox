from multiprocessing import Process
from pydub import AudioSegment
from pydub.playback import play

def playSegment(seg):
    play(seg)

def playInProcess(seg):
    p = Process(target=playSegment, args=(seg,))
    p.start()
    p.join()

song = '/home/pi/music/Crack The Skye/01 Oblivion.mp3'
audio = AudioSegment.from_file(song)
playInProcess(audio)
song = '/home/pi/music/BeLL/New Kind Of Rome/02 Overexposed.m4a'
audio = AudioSegment.from_file(song)
playInProcess(audio)
