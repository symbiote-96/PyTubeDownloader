## PyTubeDownloader

This Python project, **PyTubeDownloader**, allows you to download audio from individual YouTube videos or entire playlists and automatically convert them to MP3 format.

### Features:
- **Download individual songs**: Download audio from a single YouTube video.
- **Download entire playlists**: Download all audios from a YouTube playlist, each converted to MP3 and saved in its own folder.
- **Automatic MP3 conversion**: All downloaded videos are converted to MP3 using `FFmpeg` with a default quality of 192 kbps.

---

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd PyTubeDownloader
   ```

2. **Set up a virtual environment**:
   Create and activate a virtual environment to isolate your project's dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux or WSL
   ```

3. **Install the required dependencies**:
   Install the libraries needed for the project using `pip`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure FFmpeg is installed**:
   This project uses FFmpeg to convert videos to MP3. Make sure FFmpeg is installed on your system:
   - **On Linux/WSL**: Install FFmpeg by running:
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
   - **On Windows**: Follow the installation instructions [here](https://ffmpeg.org/download.html) to download and add FFmpeg to your system's PATH.

---

### Usage

1. **Run the program**:
   Start the program by running the main Python script. You'll be prompted to choose between downloading an individual song or an entire playlist.
   ```bash
   python downloader.py
   ```

2. **Choose an option**:
   - **Option 1**: Download a single song from YouTube.
   - **Option 2**: Download an entire playlist from YouTube.

3. **Enter the URL**:
   - For individual songs, paste the URL of the YouTube video.
   - For playlists, paste the URL of the playlist.

4. **Files will be saved**:
   - **Individual songs**: Saved directly to the `Downloads` folder with the video's title.
   - **Playlists**: A folder with the playlist's name will be created in `Downloads`, and each song will be saved in that folder.

---

### Code Structure

- **`downloader.py`**: The main entry point of the program, where users can choose between downloading individual songs or entire playlists.
- **`functions.py`**: Contains the core functions:
  - `download_song()`: Downloads a single YouTube video as audio and converts it to MP3.
  - `download_playlist()`: Downloads an entire playlist and converts each video to MP3.
- **`requirements.txt`**: Lists all dependencies required for the project, such as `yt-dlp` and `ffmpeg-python`.

---

### Example

1. **Download a single song**:
   - Run the program:
     ```bash
     python downloader.py
     ```
   - Select option 1 and enter the URL of the song:
     ```
     https://www.youtube.com/watch?v=example_video_id
     ```

2. **Download a playlist**:
   - Run the program:
     ```bash
     python downloader.py
     ```
   - Select option 2 and enter the URL of the playlist:
     ```
     https://www.youtube.com/playlist?list=example_playlist_id
     ```

---

### Planned Features

- **Command-line interface (CLI)**: In the next iteration, a `cli.py` file will be introduced to allow users to interact with the program through command-line arguments, without needing interactive input.

---

### Known Issues

- **Playlist URL in `download_song()`**: The `download_song()` function has been updated to handle URLs from videos that are part of a playlist, ensuring only the individual video is downloaded.

---

### Contributing

Feel free to fork this repository and create pull requests if you'd like to contribute or improve any part of the project.

---

### License

This project is licensed under the MIT License. See the LICENSE file for more details.