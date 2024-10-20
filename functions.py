import yt_dlp

def download_song(song_url):
    """Download a single song from YouTube and convert it to MP3."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '/mnt/c/Users/msant/Downloads/%(title)s.%(ext)s',
        'noplaylist': True  # Ensure only the video (song) is downloaded, not the entire playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])
        print("Song downloaded and converted to MP3 successfully.")
    except Exception as e:
        print(f"Error downloading the song: {e}")


def download_playlist(playlist_url):
    """Download an entire playlist from YouTube and convert it to MP3."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '/mnt/c/Users/msant/Downloads/%(playlist)s/%(title)s.%(ext)s',
        'noplaylist': False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("Playlist downloaded and converted to MP3 successfully.")
    except Exception as e:
        print(f"Error downloading the playlist: {e}")
