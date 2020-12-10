import os

print("Introduce el nombre del video junto con su tipo de expansión:")
video = input()
print("Introduce el nombre del audio junto con su tipo de expansión:")
audio = input()
print("Introduce el nombre de los subtitulos junto con su tipo de expansión:")
subt = input()
print("Introduce el nombre que deseas para el container mp4:")
name = input()

line = "ffmpeg -i {} -i {} -i {} -c:v copy -c:a aac -c:s mov_text -map 0:v:0 -map 1:a:0 -map 2:s:0 {}.mp4".format(video,audio,subt,name)
os.system(line)
