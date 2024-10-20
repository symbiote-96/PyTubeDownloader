from functions import download_song, download_playlist

def main():
    print("Welcome to YouTube Audio Downloader.")
    print("1. Download a single song")
    print("2. Download a playlist")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        song_url = input("Enter the YouTube song URL: ")
        download_song(song_url)
    elif choice == '2':
        playlist_url = input("Enter the YouTube playlist URL: ")
        download_playlist(playlist_url)
    else:
        print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
