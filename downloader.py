import yt_dlp
import ffmpeg

def download_audio_with_ytdlp(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Descarga solo el mejor audio disponible
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Usa FFmpeg para extraer el audio
            'preferredcodec': 'mp3',      # Convertir el archivo a MP3
            'preferredquality': '192',    # Calidad de audio en kbps
        }],
        'outtmpl': '/mnt/c/Users/msant/Downloads/%(title)s.%(ext)s',  # Ruta de guardado
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Audio descargado y convertido a MP3 exitosamente.")
    except Exception as e:
        print(f"Error durante la descarga o conversión: {e}")

if __name__ == "__main__":
    video_url = input("Introduce la URL del video de YouTube: ")
    download_audio_with_ytdlp(video_url)
