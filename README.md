# PyUploadMate
### Telegram Bot Integration :
Users interact with the project via the File Receiver/Sender Bot on Telegram, providing URLs for their audio files and corresponding titles.

### File Conversion :
The received URLs and titles are processed by two Python scripts:

### URL to WAV Converter :
Converts the input files into WAV format, ensuring compatibility with Believe.com 
### Title Processor : 
Handles and formats metadata for seamless uploading.
### Automated Uploading:
Another Python script, powered by Selenium, takes the converted WAV files and metadata and automates the process of uploading them to the Believe.com platform.

# How It Works
- Step 1: Send the file URL and its title to the Telegram bot [File RS Bot](https://t.me/file_RS_bot).
- Step 2: The bot forwards the data to the processing scripts.
- Step 3: The file is converted to WAV format, and the title is prepared for upload.
- Step 4: The automated uploader script logs into Believe.com and uploads the processed files and metadata.
