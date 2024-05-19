import os
import zipfile
from pytube import YouTube
from youtubesearchpython import VideosSearch

# Function to search for YouTube link for a given song
def search_youtube_link(song_name):
    try:
        # Searching for the song on YouTube
        videos_search = VideosSearch(song_name, limit=1)
        # Extracting the link of the first search result
        link = videos_search.result()['result'][0]['link']
        return link
    except Exception as e:
        print(f"Error occurred while searching for {song_name}: {e}")
        return None

# Function to download audio from YouTube link
def download_audio(link, output_dir):
    try:
        yt = YouTube(link)
        # Choosing the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        # Downloading the audio
        audio_stream.download(output_dir)
        return audio_stream.default_filename
    except Exception as e:
        print(f"Error occurred while downloading from {link}: {e}")
        return None

# Function to read songs from file, find YouTube links, and download audio
def process_songs(input_file, output_zip):
    audio_files = []
    with open(input_file, 'r') as f:
        songs = f.readlines()

    with open('ytblnks.txt', 'w') as f:
        for song in songs:
            song = song.strip()
            # Search for YouTube link for each song
            youtube_link = search_youtube_link(song)
            if youtube_link:
                f.write(f"{song}: {youtube_link}\n")
                # Download audio for each link
                audio_file = download_audio(youtube_link, '.')
                if audio_file:
                    audio_files.append(audio_file)
            else:
                f.write(f"{song}: Not found\n")

    # Create a zip file and add downloaded audio files to it
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for audio_file in audio_files:
            zipf.write(audio_file)
            # Delete the downloaded audio file after adding to zip
            os.remove(audio_file)

# Main function
def main():
    input_file = 'songs.txt'
    output_zip = 'downloaded_songs.zip'
    process_songs(input_file, output_zip)
    print("Audio files downloaded and saved in 'downloaded_songs.zip'")

if __name__ == "__main__":
    main()
