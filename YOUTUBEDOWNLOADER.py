import pytube
import time

from pytube import YouTube

print("Loading")

time.sleep(0.5)

URL = input("Enter URL: ")


print("Retrieving")

time.sleep(0.5)

video = YouTube(URL)

print("Retrieved")

video = YouTube(URL)
video_streams = video.streams.filter(file_extension='mp4').get_by_itag(18)
print(video_streams.title)


time.sleep(0.5)

print("Download Start")

video_streams = video.streams.filter(file_extension='mp4')
print(video_streams)

print("Downloaded")

time.sleep(0.5)

print("Saving Video")

vidname = input("Enter Save Name: ")

video_streams.download(filename = (vidname + ".mp4"),
	output_path = "downloads")
    
print("Saved And Completed")