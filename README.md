# pyyt

*pyyt* is a genuine, lightweight Python library (and command-line utility) for downloading YouTube videos.

## Description

YouTube is the most popular video-sharing platform in the world and as a hacker, you may encounter a situation where you want to script something to download videos. For this, I present to you: *pyyt*.

*pyyt* is a lightweight library written in Python. It has minimal dependencies and aims to be highly reliable.

*pyyt* also makes pipelining easy, allowing you to specify callback functions for different download events, such as ``on progress`` or ``on complete``.

Furthermore, *pyyt* includes a command-line utility, allowing you to download videos right from the terminal.

## Features

- Support for both progressive & DASH streams
- Easily register ``on_download_progress`` & ``on_download_complete`` callbacks
- Command-line interface included
- Caption track support
- Outputs caption tracks to .srt format (SubRip Subtitle)
- Ability to capture thumbnail URL
- Extensively documented source code

## Quickstart

### Installation

pyyt requires an installation of Python 3.7 or greater, as well as pip. (Pip is typically bundled with Python [installations](https://python.org/downloads).)

To install from PyPI with pip:

```bash
pip install pyyt
```

Or install from source:

```bash
pip install -e .
```

### Using pyyt in a Python script

To download a video using the library in a script, you'll need to import the YouTube class from the library and pass an argument of the video URL. From there, you can access the streams and download them.

```python
from pyyt import download_video, download_captions, download_videos_from_list, download_videos_from_channels

# Download a single video
download_video(url="https://www.youtube.com/watch?v=VIDEO_ID")

# Download captions for a video
download_captions(url="https://www.youtube.com/watch?v=VIDEO_ID")

# Download Videos from a list, for example, videos.txt

download_videos_from_list(filename="videos.txt")

# Download Videos from a Channel, or multiple Channels

download_videos_from_channels(channels=["officialalphablocks", "Numberblocks"])
```

### Using the command-line interface

Using the CLI is remarkably straightforward as well. To download a video at the highest progressive quality, you can use the following command:

```bash
pyyt https://youtube.com/watch?v=2lAe1cqCOXo
```

## License

This project is licensed under The Unlicense - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open an issue or a pull request at https://github.com/Josh-XT/pyyt
