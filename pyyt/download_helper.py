import os
import re
import sys
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pyyt import YouTube
from pyyt.innertube import _default_clients


def get_videos_from_channel(channel_name: str = ""):
    if not channel_name:
        return "No channel name provided."
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    url = f"https://www.youtube.com/@{channel_name}"
    driver.get(url)
    time.sleep(5)
    video_elements = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
    video_ids = [
        video.get_attribute("href")
        for video in video_elements
        if video.get_attribute("href")
    ]
    driver.quit()
    return video_ids


def download_video(url: str = ""):
    if not url:
        return "No URL provided."
    os.makedirs("videos", exist_ok=True)
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        output_video = yt.title.replace(" ", "_")
        output_video = "".join([c for c in output_video if c.isalnum() or c in "._- "])
        video_stream.download(output_path="videos", filename=f"{output_video}.mp4")
    except:
        _default_clients["ANDROID_EMBED"] = _default_clients["MWEB"]
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        output_video = yt.title.replace(" ", "_")
        output_video = "".join([c for c in output_video if c.isalnum() or c in "._- "])
        video_stream.download(output_path="videos", filename=f"{output_video}.mp4")
    yt.captions["en-US"].download(title=f"{output_video}.srt", output_path="videos")
    yt.captions["en-US"].json_captions
    transcript = f"Transcription of video titled `{yt.title}` at {url}:\n"
    for event in yt.captions["en-US"].json_captions["events"]:
        for seg in event["segs"]:
            transcript += seg["utf8"]
    text = transcript.replace("\xa0", " ").replace("  ", " ").replace(" \n", " ")
    video_path = os.path.abspath(f"videos/{output_video}.mp4")
    transcript_path = os.path.abspath(f"videos/{output_video}.txt")
    with open(transcript_path, "w") as f:
        f.write(text)
    return f"Downloaded video from {url}\n  Video: {video_path}\n  Transcript: {transcript_path}"


def download_videos_from_channels(channels=[]):
    if not channels:
        return "No channels provided."
    filename = datetime.now().isoformat().replace(":", "-").split(".")[0] + ".txt"
    videos = []
    for channel in channels:
        videos += get_videos_from_channel(channel)
    downloaded_files = []
    with open(filename, "r") as f:
        links = f.read().splitlines()
        for video in videos:
            if video not in links:
                result = download_video(url=video)
                downloaded_files.append(result)
                with open(filename, "a") as f:
                    f.write(video + "\n")
    return (
        "Downloaded videos from channels: "
        + ", ".join(channels)
        + "\n"
        + "\n".join(downloaded_files)
    )


def download_videos_from_list(filename="videos.txt"):
    downloaded_files = []
    with open(filename, "r") as f:
        links = f.read().splitlines()
        for video in links:
            result = download_video(url=video)
            downloaded_files.append(result)
    return "Downloaded videos from list:\n" + "\n".join(downloaded_files)


def download_captions(url: str = ""):
    if not url:
        return "No URL provided."
    os.makedirs("captions", exist_ok=True)
    yt = YouTube(url)
    video_stream = yt.streams.get_lowest_resolution()
    output_video = yt.title.replace(" ", "_")
    output_video = "".join([c for c in output_video if c.isalnum() or c in "._- "])
    yt.captions["en-US"].download(title=f"{output_video}.srt", output_path="captions")
    yt.captions["en-US"].json_captions
    transcript = f"Captions of video titled `{yt.title}` at {url}:\n"
    for event in yt.captions["en-US"].json_captions["events"]:
        for seg in event["segs"]:
            transcript += seg["utf8"]
    text = transcript.replace("\xa0", " ").replace("  ", " ").replace(" \n", " ")
    # Find anything between [Ad Start] and [Ad End] and remove it
    text = re.sub(r"\[Ad Start\].*?\[Ad End\]", "", text, flags=re.DOTALL)
    return text
