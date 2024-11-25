from __future__ import unicode_literals
import time
import os
import re
import yt_dlp
import ffmpeg
import yt_dlp
import pygetwindow as gw
from pywinauto import Desktop
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import sys

# Function to read URL-title pairs from a file
def read_url_title_pairs(file_path=r"C:\Users\Pouya\Documents\url_title_pairs.txt"):
    url_title_pairs = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("URL: "):
                url = line.split("URL: ")[1].split(", Title: ")[0]
                title = line.split(", Title: ")[1].strip()
                url_title_pairs[url] = title
    return url_title_pairs

def print_url_title_pairs(url_title_pairs):
    for url, title in url_title_pairs.items():
        print(f'URL: {url}, Title: {title}')

# Read URL-title pairs from the file
file_path = r"C:\Users\Pouya\Documents\url_title_pairs.txt"
url_title_pairs = read_url_title_pairs(file_path)
print_url_title_pairs(url_title_pairs)

# Get the title of the first line
first_title = next(iter(url_title_pairs.values()))

# Path to Edge WebDriver
edge_driver_path = r"D:\edgedriver_win64\msedgedriver.exe"  # Update this path to the actual location of msedgedriver.exe

# Create a Service object
service = Service(edge_driver_path)

# Open Microsoft Edge browser with InPrivate mode, proxy settings, and ignoring SSL certificate errors
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.add_argument("--inprivate")
options.add_argument("--disable-features=TrackingPrevention")
options.add_argument("--disable-features=CookiesWithoutSameSiteMustBeSecure")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--proxy-server=http://localhost:8081")  # Use the proxy server
options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors

# Use the existing Edge profile
options.add_argument("user-data-dir=C:\\Users\\Pouya\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")  # Use the correct profile directory

driver = webdriver.Edge(service=service, options=options)
driver.get("https://www.believebackstage.com/")
try:
    # Inject CSS to support Safari
    css = """
    #jimo_view_wrapper.is-fullscreen {
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px); /* Support for Safari 9+ */
    }
    """
    driver.execute_script(f"""
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(`{css}`));
    document.head.appendChild(style);
    """)
    print("Injected CSS to support Safari.")
    # Wait for the username input field to be present and interactable, then enter "User1"
    print("Waiting for the username input field...")
    username_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "signInName"))
    )
    print("Username input field found.")
    time.sleep(0.5)
    username_field.send_keys("User1")

    # Wait for the password input field to be present and interactable, then enter "Uploader2023"
    print("Waiting for the password input field...")
    password_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    print("Password input field found.")
    time.sleep(0.5)
    password_field.send_keys("Uploader2023")

    # Wait for the login button to be clickable and click it
    print("Waiting for the login button...")
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "next"))
    )
    print("Login button found.")
    time.sleep(0.5)
    login_button.click()

    # Wait for the URL to change to the next page
    WebDriverWait(driver, 20).until(
        EC.url_to_be("https://www.believebackstage.com/index")
    )
    print("Successfully logged in and redirected!")
    try:
        # Click on the "add" button
        print("Waiting for 'add' button...")
        add_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//i[text()='add']"))
        )
        print("'Add' button found.")
        time.sleep(0.5)
        add_button.click()
    except Exception as e:
        print(f"No 'add' button found: {e}")

    # Click on "One release"
    print("Waiting for 'One release' link...")
    one_release_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@onclick='newRelease()']"))
    )
    print("'One release' link found.")
    time.sleep(0.5)
    one_release_link.click()

    # Click on the "NEXT" button
    next_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#newReleaseModalNextButton"))
    )
    time.sleep(0.5)
    next_button.click()
    print("Clicked on the 'NEXT' button.")

    # Click on the "NEXT" button again
    next_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#newReleaseModalNextButton"))
    )
    time.sleep(0.5)
    next_button.click()
    print("Clicked on the 'NEXT' button again.")

    # Iterate through the URL-title pairs from first line to the last line , find the title and assign it to a variable and pass it to the next code that puts the title in the input field
    for url, title in url_title_pairs.items():
        # Enter the title into the release title input field
        release_title_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#newReleaseInputTitle"))
        )
        release_title_input.clear()
        release_title_input.send_keys(title)
        print(f"Entered the title '{title}' into the release title input field.")
        break

    # Click on the "CREATE" button
    create_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#newReleaseModalCreateButton"))
    )
    time.sleep(0.5)
    create_button.click()
    print("Clicked on the 'CREATE' button.")

    # Scroll down to the bottom of the page to see 'i get it' button
    
    # Scroll down to the bottom of the page to see 'I get it' button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scrolled to the bottom of the page.")

    # Check for the "I get it" button and click it if it appears
    try:
        time.sleep(5)
        i_get_it_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "get-it-btn"))
        )
        time.sleep(2)
        i_get_it_button.click()
        print("Clicked on the 'I get it' button.")
        
        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        print("Scrolled to the top of the page.")
    except:
        print("'I get it' button did not appear, continuing...")
        # Simulate scrolling down with the mouse scroller
        actions = ActionChains(driver)
        for _ in range(10):  # Adjust the range for the amount of scrolling needed
            actions.scroll_by_amount(0, 100).perform()
            time.sleep(0.2)  # Adjust the sleep time if necessary
        print("Simulated scrolling down with the mouse scroller.")

    # Click on the "Upload" button
    upload_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.easyEntryStep[data-page='assets']"))
    )
    time.sleep(0.5)
    upload_button.click()
    print("Clicked on the 'Upload' button.")

    # Click on the "Uploader" button
    uploader_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navLinkItem[data-todisplay='uploader']"))
    )
    time.sleep(0.5)
    uploader_button.click()
    print("Clicked on the 'Uploader' button.")

    # Click on "Click here to launch the uploader"
    launch_uploader_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary[onclick^='launchUploader']"))
    )
    time.sleep(0.5)
    launch_uploader_button.click()
    print("Clicked on 'Click here to launch the uploader.'")

    # Wait for the new window to open
    WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
    print("New window opened.")

    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])
    print("Switched to the new window.")

    # Click on the "Add files" button
    time.sleep(2)

    add_files_buttons = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "fileinput-button"))
    )
    time.sleep(0.5)
    add_files_buttons[0].click()
    print("Clicked on the 'Add files' button.")

    # Find out if the URL of the current title consists instagram.com or youtu.be or /www.youtube.com. if instagram.com, then print it is an instagram link, if youtu.be, then print it is a youtube link, if /www.youtube.com, then print it is a youtube link
    #only for the title of the first line
    if "instagram.com" in url:
        print("This is an Instagram link.")
    elif "youtu.be" in url or "www.youtube.com" in url:
        print("This is a YouTube link.")
    else:
        print("This is a YOUTube link.")
    # if instagram.com, then run the following code and put the url IG-to-wav.py in the input field
    if "instagram.com" in url:
        # Enter the URL into the input field of the following code  IG-to-wav.py
                    
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
                # Manually paste the Instagram video URL here
                download_from_url(url)


    else:
        # if youtu.be or /www.youtube.com, then run the following code and put the url YT-to-wav.py in the input field
        # Ensure the output directory exists
        output_dir = 'D:/Wav files'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Function to sanitize filenames
        def sanitize_filename(filename):
            return re.sub(r'[\\/*?:"<>|]', "", filename)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s').replace('\\', '/'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
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
            # Manually paste the YouTube video URL here
            urlis = url
            download_from_url(url)

    # Select the converted WAV file
    wav_files = [f for f in os.listdir(output_dir) if f.endswith('.wav')]
    if wav_files:
        wav_file_path = os.path.join(output_dir, wav_files[0])
        print(f"Selecting WAV file: {wav_file_path}")
        # Simulate file selection (this part depends on the specific implementation of the file uploader)
        file_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        file_input.send_keys(wav_file_path)

        # Close the file dialog window
        # Print all window titles
        print([window.title for window in gw.getAllTitles()])

        # Close the window with the matching title
        windows = gw.getWindowsWithTitle('Open')
        if windows:
            windows[0].close()

        
        # Wait for the file to start uploading
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "td.upload .glyphicon.glyphicon-ok"))
        )
        print(f"{title} is being uploaded")

        # Wait for the uploading state to get checked
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "td.check .glyphicon.glyphicon-ok"))
        )
        print(f"{title} uploading process has been checked")

        # Wait for the processing to complete
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "td.encoding .glyphicon-ok"))
        )
        print(f"Processing completed for title: {title}, URL: {url}")
    else:    
        print("No WAV files found in the output directory.")

    
except Exception as e:
        print(f"An error occurred: {e}")
finally:
        # Print the current URL
        time.sleep(500)
        print(f"Current URL: {driver.current_url}")
        driver.quit()



