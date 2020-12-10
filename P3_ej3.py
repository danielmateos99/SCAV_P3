import os
import subprocess


print("Introduce el nombre del container (incluyendo .mp4):")
name = input()

line1 = "ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 {}".format(name)
vresult = subprocess.getoutput(line1)
line2 = "ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 {}".format(name)
aresult = subprocess.getoutput(line2)
print(" ")
print("El contenedor soporta los siguientes broadcasting standards:")
if (vresult == "mpeg2") or (vresult == "h264"):
    if aresult == "mp3":
        print("DVB y DTMB")
    elif aresult == "aac":
        print("DVB, ISDB y DTMB")
    elif aresult == "ac-3":
        print("DVB, ATSC y DTMB")
    elif aresult == "dra" or "mp2":
        print("DTMB")
    else:
        print("Error")
elif (vresult == "avs" or "avs+") and (aresult == "dra" or "aac" or "ac-3" or "mp2" or "mp3"):
    print("DTMB")
else:
    print("Error")
print(" ")
