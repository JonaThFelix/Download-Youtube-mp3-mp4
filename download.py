#JonathanFelix | Akenathon | @hiperbolante
#pip install pytube   // mp4
#pip install os_sys   // mp3

import time
import os 
from pytube import YouTube


yt = YouTube(input("~ Digite ou cole abaixo URL do vídeo que deseja baixar:\n "))
print("Em qual formato você deseja baixar?")
escolha = int(input("1 - MP4(Vídeo) | 2 - MP3 (Áudio) \n"))

if escolha == 1:
    print(f"Você escolheu {escolha} - MP4.")
    yt.streams.filter(progressive = True, file_extension='mp4').order_by('resolution')[-1].download()
    print("Download formato MP4 em andamento ...")
    time.sleep(1)
    print(f"{yt.title} vídeo baixado com sucesso !!!")
    print("Desenvolvido por Jonathan | IG: @hiperbolante")

if escolha == 2:
    print(f"Você escolheu {escolha} - MP3.")
    video = yt.streams.filter(only_audio=True).first()
    destination = str(input("Para Baixar pressione Enter ...")) or '.'
    out_file = video.download(output_path = destination)
    base, ext = os.path.splitext(out_file)
    new_file = base +  '.mp3'
    os.rename(out_file, new_file)
    print(f"{yt.title} áudio baixado com sucesso !!! ")
    print("Desenvolvido por Jonathan | IG: @hiperbolante")

elif escolha != 1 or escolha != 2:
    print(f"Opção {escolha} Inválida! \nRetorne opção 1 ou 2")



