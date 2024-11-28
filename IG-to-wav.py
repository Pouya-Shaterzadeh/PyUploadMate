from __future__ import unicode_literals
import yt_dlp
import os
import re

# Ensure the output directory exists
output_dir = 'D:/Wav files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to sanitize filenames
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

# yt-dlp options for Instagram
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s').replace('\\', '/'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'cookiefile': 'D:/cookies.txt'  # Install Cookie Editor extension on your device, login to your Intagram account and export all cookies to D:/cookies.txt path
}

def download_from_url(url):
    try:
        print(f"Starting download for URL: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = sanitize_filename(info_dict.get('title', None))
            ext = info_dict.get('ext', None)
            input_file = os.path.join(output_dir, f"{title}.{ext}").replace('\\', '/')
            output_file = os.path.join(output_dir, f"{title}.wav").replace('\\', '/')
            print(f"Download completed: {input_file}")
            
            # Check if the output file exists
            if not os.path.exists(output_file):
                print(f"Error: Output file does not exist: {output_file}")
                return
            
            print(f"File converted to WAV format: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the Instagram video URL: ")
    download_from_url(url)
