import os

#Recortar un minuto del vídeo BBB_full.avi y llamarlo BBB1min
os.system("ffmpeg -i BBB_full.avi -ss 00:00:00 -t 00:01:00 -async 1 BBB1min.mp4")
#mono file
os.system("ffmpeg -i BBB1min.mp4 -ac 1 -vn monoaudio.mp3")
#lower bitrate
os.system("ffmpeg -i monoaudio.mp3 -map 0:a:0 -b:a 30k lowbitrate.mp3")
#create mp4 container
os.system('ffmpeg -i BBB1min.mp4 -i lowbitrate.mp3 -i subt.srt -c:v copy -c:a aac -c:s mov_text -map 0:v:0 -map 1:a:0 -map 2:s:0 container.mp4')

print(" ")
print("File container.mp4 created.")
print(" ")
