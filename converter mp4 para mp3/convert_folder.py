import os, glob
from moviepy.editor import *

def Core ():
    #escolher uma pasta
    print("QUAL O NOME DA PASTA QUE DEVE SER CONVERTIDA? ", end = '')
    dir_path = input()
    #obter todos os diretorios dos arquivos da pasta
    dir_names = glob.glob(r"./{}/*.mp4" .format(dir_path))
    #obter todos os nomes dos arquivos da pasta
    archive_names = []
    replace_space = "./{}\\" .format(dir_path)
    for i in range (len(dir_names)):
        modify_dir = dir_names[i]
        modification1 = modify_dir.replace(replace_space, "")
        modification2 = modification1.replace(".mp4", "")
        archive_names.append(modification2)
    #criar a nova pasta de conversão
    if not os.path.exists (r"./{} to mp3/" .format(dir_path)):
        os.makedirs(r"./{} to mp3/" .format(dir_path))
    #converter os arquivos
    for w in range (len(dir_names)):
        audio_clip = AudioFileClip(r"{}" .format(dir_names[w]))
        audio_clip.write_audiofile(r"./{} to mp3/{}.mp3" .format(dir_path, archive_names[w]))
        audio_clip.close()
        print("CONVERTEU ARQUIVO {} de {}!" .format(w + 1, len(dir_names)))
    print("\nTUDO FOI CONVERTIDO!")

os.system("cls")
Core()