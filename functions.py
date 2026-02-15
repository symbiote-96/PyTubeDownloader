import yt_dlp
import os

# Detect the current user's 'Music' directory path
# This typically resolves to: /home/username/Music on Linux/macOS
music_dir = os.path.join(os.path.expanduser('~'), 'Music')

def download_song(song_url):
    """Download a single song from YouTube and convert it to MP3."""
    
    # Configure the output path using the 'music_dir' variable
    output_template = os.path.join(music_dir, '%(title)s.%(ext)s')
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_template, # Use the dynamic output path defined above
        'noplaylist': True          # Ensure only the video is downloaded, not the entire playlist
    }

    try:
        # Create the directory if it doesn't exist (safety check)
        os.makedirs(music_dir, exist_ok=True)
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])
        print(f"Song downloaded successfully to: {music_dir}")
    except Exception as e:
        print(f"Error downloading the song: {e}")


def download_playlist(playlist_url):
    """Download an entire playlist from YouTube and convert it to MP3."""
    
    # For playlists, create a subfolder with the playlist's name to keep files organized
    output_template = os.path.join(music_dir, '%(playlist)s', '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_template,
        'noplaylist': False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"Playlist downloaded successfully to: {music_dir}")
    except Exception as e:
        print(f"Error downloading the playlist: {e}")

# Usage example (uncomment to test):
# download_song('YOUR_SONG_URL_HERE')
