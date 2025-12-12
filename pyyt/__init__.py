# flake8: noqa: F401
# noreorder
"""
pyyt: a very serious Python library for downloading YouTube Videos.
"""
from importlib.metadata import version, PackageNotFoundError

__title__ = "pyyt"
__author__ = "Josh-XT"
__license__ = "The Unlicense (Unlicense)"
__js__ = None
__js_url__ = None

try:
    __version__ = version("pyyt")
except PackageNotFoundError:
    __version__ = "0.0.1"  # fallback for development

from pyyt.streams import Stream
from pyyt.captions import Caption
from pyyt.query import CaptionQuery, StreamQuery
from pyyt.__main__ import YouTube
from pyyt.innertube import InnerTube
from pyyt.download_helper import (
    download_video,
    download_videos_from_channels,
    download_videos_from_list,
    download_captions,
    get_videos_from_channel,
)
