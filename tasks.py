import os
import utils
# from pytube import YouTube
from pytubefix import YouTube
from celery import Celery

app = Celery("tasks", broker="pyamqp://guest@localhost//")

@app.task
def download_from_youtube(url, download_video, download_audio):
    youtube_obj = YouTube(url)
    music_title = f"{youtube_obj.title} - {youtube_obj.author}"

    print(f"[Recurso: {music_title}] Descargando...")
    import pdb; pdb.set_trace()
    if download_video:
        print(f"\t[Recurso: {music_title}] Obteniendo video...")
        output = os.path.join(utils.get_path_salida_video(), f"{music_title}.mp4")
        video_obj = youtube_obj.streams.get_highest_resolution()
        video_obj.download(filename=output)
    if download_audio:
        print(f"\t[Recurso: {music_title}] Obteniendo audio...")
        output = os.path.join(utils.get_path_salida_audio(), f"{music_title}.mp3")
        audio_obj = youtube_obj.streams.get_audio_only()
        audio_obj.download(filename=output)

    print(f"\t[Recurso: {music_title}] Descarga completa!")
