from moviepy.editor import *
import os

class MP3Converter:
    def convert(self, video_file, save_path):
        if not save_path.endswith("\\"):
            save_path += "\\"
        mp3_file = save_path + os.path.basename(video_file).replace(".mp4", ".mp3")
        audioclip = AudioFileClip(video_file)
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        os.remove(video_file)
        return mp3_file
