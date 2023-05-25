from pytube import YouTube
from moviepy.editor import VideoFileClip


def convertir_a_mp3(ruta_video, ruta_mp3):
    try:
        video = VideoFileClip(ruta_video)
        video.audio.write_audiofile(ruta_mp3, verbose=False)
        print("Conversión a MP3 completa.")
    except Exception as e:
        print(f"Ocurrió un error durante la conversión a MP3: {str(e)}")


def descargar_video(links):
    enlaces = [link.strip() for link in links]
    try:
        for enlace in enlaces:
            print("Descargando ...")
            video = YouTube(enlace)
            title = video.title[:40].replace("/", "-")
            video.streams.get_highest_resolution().download("./", f"{str(title)}.mp4")
            print("Descarga MP4 completa.", title)
            convertir_a_mp3((f"./{str(title)}.mp4"), (f"./{str(title)}.mp3"))
        return "Todas las descargas completadas"
    except Exception as e:
        return f"Ocurrió un error durante la descarga: {str(e)}"
