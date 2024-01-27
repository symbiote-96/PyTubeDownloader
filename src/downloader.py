from pytube import YouTube, Playlist
from abc import ABC, abstractmethod

class Downloader(ABC):
    @abstractmethod
    def download(self):
        pass

class VideoDownloader(Downloader):
    def __init__(self, url):
        self.yt = YouTube(url)

    def download(self):
        return self.yt.streams.get_highest_resolution().download()

class PlaylistDownloader(Downloader):
    def __init__(self, url):
        self.playlist = Playlist(url)

    def download(self):
        for video_url in self.playlist.video_urls:
            yt = YouTube(video_url)
            yt.streams.get_highest_resolution().download()
