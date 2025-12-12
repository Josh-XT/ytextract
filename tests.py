from pyyt.download_helper import download_video, download_captions

print("Download a Video from URL:")
print(download_video(url="https://www.youtube.com/watch?v=1HAcza0nE34"))
print("Download Captions for Video:")
print(download_captions(url="https://www.youtube.com/watch?v=1HAcza0nE34"))
