import os, _thread, time
import pytube.exceptions
from pytube import YouTube as yt
from pytube import Playlist as pl

def Core ():
    #variaveis
    global finish_timer
    global the_timer
    finish_timer = False
    the_timer = 0
    errors_array = []
    impossible_array = []
    modular_url = ''
    #input
    print("Criado por .: Salu Conteratto Ramos")
    print("Digite a url: ", end = '')
    url = input()
    #verificar se é playlist ou video sozinho
    try:
        #este caminho caso seja playlist
        url_playlist = pl(url)
    except:
        #este caminho caso seja video único
        yt(url).streams.first().download()
        print("O VIDEO FOI BAIXADO!")
        return
    #continuar caso seja playlist
    playlist_array = url_playlist.video_urls
    _thread.start_new_thread(TotalTime, ()) #thread do timer
    os.system("cls")
    print("INICIANDO!!!\n")
    for i in range (len(playlist_array)):
        try:
            modular_url = playlist_array[i]
            yt(modular_url).streams.first().download()
            print("acabou de baixar video {} de {}" .format((i + 1), len(playlist_array)))
        except KeyError:
            impossible_array.append(modular_url)
            print("erro ao tentar baixar o video {} de {} (IMPOSSIVEL TENTAR NOVAMENTE)" .format((i + 1), len(playlist_array)))
        except:
            print("erro ao tentar baixar o video {} de {} (POSSIVEL TENTAR NOVAMENTE)" .format((i + 1), len(playlist_array)))
            errors_array.append(modular_url)
    finish_timer = True
    print("\nTUDO FOI BAIXADO EM {} SEGUNDO(S)!\n" .format(the_timer))
    print("{} VIDEO(S) É/SÃO IMPOSSIVE(L/IS) DE BAIXAR!\n" .format(len(impossible_array)))
    print(impossible_array)
    print("\nERRO AO BAIXAR {} VIDEO(S)!:\n" .format(len(errors_array)))
    print(errors_array)
    print("\n--------------------------------------------------------------\n")
    TryAgain(errors_array)

def TryAgain (the_list):
    print("TENTANDO BAIXAR OS VIDEOS COM ERRO NOVAMENTE!\n")
    global new_one
    new_one = []
    for x in range (len(the_list)):
        try:
            yt(the_list[x]).streams.first().download()
            print("VIDEO {} DA LISTA DE RETENTATIVAS DEU CERTO" .format(x + 1))
        except:
            new_one.append(the_list[x])
            print("VIDEO {} DA LISTA DE RETENTATIVAS NÃO DEU CERTO" .format(x + 1))
    if len(new_one) > 0:
        print("\n")
        print(new_one)
        print("\n--------------------------------------------------------------\n")
        TryAgain(new_one)
    else:
        print("\nTODOS OS VIDEOS POSSIVEIS FORAM BAIXADOS!")

def TotalTime ():
    global the_timer
    global finish_timer
    while (finish_timer == False):
        time.sleep(1)
        the_timer += 1

os.system("cls")
Core()