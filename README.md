
### SCAV LAB3
Daniel Mateos Manjón
NIA: 205514

## Ejercicio 1
Puedes encontrarlo en el archivo "P3_ej1.py", para que funcione necesitas el video original de BBB guardado como "BBB_full.avi" y sus subtítulos como "subt.srt".
Primero extraemos un fragmento de un minuto del vídeo del original
Extraemos el audio del vídeo como mono y le aplicamos un bitrate más bajo.

Link: https://superuser.com/questions/826669/ffmpeg-get-mono-wav-audio-8khz-16-bit-out-of-mp4-video
Link: https://superuser.com/questions/552817/fastest-way-to-convert-any-audio-file-to-low-bitrate

Finalmente generamos un contenedor, "container.mp4", con todas las pistas usando ffmpeg.

Link: https://stackoverflow.com/questions/8672809/use-ffmpeg-to-add-text-subtitles

## Ejercicio 2
Puedes encontrarlo en el archivo "P3_ej2.py".
En este ejercicio podemos crear un contenedor con las pistas de video, audio y subtítulos que reciba como input, el nombre del contenedor también lo indica el usuario.

## Ejercicio 3
Puedes encontrarlo en el archivo "P3_ej3.py".
Obtenemos el tipo de tracks utilizadas en un contenedor (CONTAINER.MP4) con la línea "ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 CONTAINER.MP4" y con el outut obtenido que tipos de broadcasting son compatibles.

## Ejercicio 4
Puedes encontrarlo en el archivo "P3_ej4.py"
Este ejercicio es una mezcla del ejercicio 2 y el ejercicio 3, el usuario puede crear contenedores y posteriormente se indican los tipos de broadcasting que son compatibles.

## Ejercicio 5
Puedes encontrarlo en el archivo "P3_ej5.py".
Este ejercicio consiste en un menú para seleccionar los ejercicios anteriores desde terminal con "python P3_ej5.py".
