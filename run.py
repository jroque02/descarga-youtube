from tasks import download_from_youtube

class DownloadYoutube:
    def __init__(self, file_txt, download_video=False, download_audio=False):
        self.file_txt = "./musica.txt"
        self.download_video = download_video
        self.download_audio = download_audio

    def download_from_youtube(self):
        file = open(self.file_txt, "r")
        file_lines = file.readlines()
        file.close()
        
        for url in file_lines:
            download_from_youtube(url, self.download_video, self.download_video)


if __name__ == "__main__":
    download_video = input("Descargar video (y/n):: ")
    download_audio = input("Descargar audio (y/n):: ")

    download_video = download_video.lower() == "y"
    download_audio = download_audio.lower() == "y"
    download_obj = DownloadYoutube(download_video, download_audio)
    download_obj.download_from_youtube()