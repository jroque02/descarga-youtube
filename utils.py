import os
from dotenv import load_dotenv

load_dotenv()

PATH_SALIDA_VIDEO = os.getenv("PATH_SALIDA_VIDEO")
PATH_SALIDA_AUDIO = os.getenv("PATH_SALIDA_AUDIO")

if not os.path.exists(PATH_SALIDA_VIDEO):
    os.makedirs(PATH_SALIDA_VIDEO)

if not os.path.exists(PATH_SALIDA_AUDIO):
    os.makedirs(PATH_SALIDA_AUDIO)

def get_path_salida_video():
    return PATH_SALIDA_VIDEO

def get_path_salida_audio():
    return PATH_SALIDA_AUDIO