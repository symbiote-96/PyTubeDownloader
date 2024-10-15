from pytube import YouTube

def download_audio(video_url):
    try:
        # Load the video form YouTube
        yt = YouTube(video_url)

        # Filter for only audio
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio
        audio_stream.download(output_path="output/", filename_prefix="audio_")
        print(f"Audio descargado: {yt.title}")
    except Exception as e:
        print(f"Error al descargar el audio: {e}")

if __name__ == "__main__":
    video_url = input("Introduce la URL del video de YouTube: ")
    download_audio(video_url)
