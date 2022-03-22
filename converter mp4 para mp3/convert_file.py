import os
from moviepy.editor import *

def Core ():
    #escolher uma pasta
    print("QUAL O NOME DO ARQUIVO QUE DEVE SER CONVERTIDO? ", end = '')
    dir_path = input()
    print("\n")
    #converter o arquivo
    audio_clip = AudioFileClip(r"./{}.mp4" .format(dir_path))
    audio_clip.write_audiofile(r"./{}.mp3" .format(dir_path))
    audio_clip.close()
    print("\nARQUIVO CONVERTIDO!")

os.system("cls")
Core()