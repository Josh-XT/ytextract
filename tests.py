from pyyt.download_helper import download_video, download_captions

TEST_VIDEO_URL = "https://www.youtube.com/watch?v=B00lazPU_yM"

print("Download a Video from URL:")
print(download_video(url=TEST_VIDEO_URL))
print("Download Captions for Video:")
print(download_captions(url=TEST_VIDEO_URL))
