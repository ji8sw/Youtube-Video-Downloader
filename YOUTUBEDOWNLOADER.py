try:
    import pytube 
except ImportError: 
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install pytube'\nPress enter to exit") 
    exit() 

import pytube
from pytube import YouTube
URL = input("Enter URL: ")
video = YouTube(URL)
video_streams = video.streams.filter(file_extension='mp4').get_by_itag(18)
video_streams.download(filename = "video",
	output_path = "video_path")
    