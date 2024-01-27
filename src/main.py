from downloader import VideoDownloader, PlaylistDownloader
from converter import MP3Converter

def get_save_path(default_path):
    return input(f"Enter the path where you want to save the file [{default_path}]: ") or default_path

# Ruta de guardado por defecto (ajusta según sea necesario)
default_video_save_path = "C:\\Users\\Public\\Videos"
default_mp3_save_path = "C:\\Users\\Public\\Music"

# Descargar un video individual
video_url = 'https://www.youtube.com/watch?v=XXXX'  # Reemplaza con la URL real del video
video_save_path = get_save_path(default_video_save_path)
video_downloader = VideoDownloader(video_url)
downloaded_video = video_downloader.download(video_save_path)

# Convertir el video a MP3
mp3_save_path = get_save_path(default_mp3_save_path)
mp3_converter = MP3Converter()
mp3_path = mp3_converter.convert(downloaded_video, mp3_save_path)
print(f"MP3 file saved as: {mp3_path}")

# Descargar una playlist completa
# playlist_url = 'https://www.youtube.com/playlist?list=XXXX'  # Reemplaza con la URL real de la playlist
# playlist_save_path = get_save_path(default_video_save_path)
# playlist_downloader = PlaylistDownloader(playlist_url)
# playlist_downloader.download(playlist_save_path)
