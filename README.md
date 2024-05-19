# YouTube-Audio-Downloader
Youtube Mp3 Downloader
# YouTube Audio Downloader

This Python script allows you to download the audio from YouTube videos based on a list of song names provided in a text file. The script searches for the songs on YouTube, downloads the audio files, and saves them into a zip archive.

## Features
- Search for songs on YouTube using the song names from a text file.
- Download the audio streams from the YouTube videos.
- Save the downloaded audio files into a zip archive.
- Log the YouTube links of the searched songs into a text file.

## Requirements
- Python 3.x
- `youtube-search-python` package
- `pytube` package

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:
   ```bash
   pip install youtube-search-python
   pip install pytube

#Usage
1.Prepare an input text file named songs.txt in the same directory as your script. The file should contain the list of song names, one per line. Example:


Song Name 1
Song Name 2
Song Name 3

2.Run the script:

python download_songs.py

3.The script will:

Read the song names from songs.txt.
Search for each song on YouTube.
Download the audio of the first search result.
Save the downloaded audio files into downloaded_songs.zip.
Log the YouTube links into ytblnks.txt.

#Notes
Ensure you have proper internet connectivity as the script relies on accessing YouTube for searches and downloads.
The audio files are temporarily saved in the current directory and deleted after being added to the zip archive.

#Troubleshooting
If you encounter errors while searching for songs or downloading audio, check the error messages printed in the console.
Ensure that the songs.txt file is correctly formatted and located in the same directory as the script.
If the script fails to download a specific song, it will log the issue in ytblnks.txt
