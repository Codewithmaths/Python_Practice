# ...existing code...
"""
Simple YouTube downloader using pytube.
Usage:
    python yt_donload.py <URL> [-o OUTPUT_DIR] [-r 720p]
"""
from pytube import YouTube
import argparse
from pathlib import Path
import sys

def on_progress(stream, chunk, bytes_remaining):
    total = stream.filesize or 0
    if total:
        downloaded = total - bytes_remaining
        pct = downloaded / total * 100
        print(f"\rDownloading... {pct:5.1f}% ", end="", flush=True)

def download(url: str, out_dir: str = ".", resolution: str | None = None):
    yt = YouTube(url, on_progress_callback=on_progress)
    # Prefer progressive mp4 streams (audio+video)
    if resolution:
        stream = yt.streams.filter(progressive=True, file_extension="mp4", res=resolution).first()
        if not stream:
            print(f"Requested resolution {resolution} not available, using highest available progressive stream.")
    if not resolution:
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

    if not stream:
        # fallback to any mp4 stream
        stream = yt.streams.filter(file_extension="mp4").order_by("resolution").desc().first()

    if not stream:
        raise RuntimeError("No suitable stream found for this video.")

    out_path = Path(out_dir).expanduser()
    out_path.mkdir(parents=True, exist_ok=True)

    print(f"Title: {yt.title}")
    print(f"Author: {yt.author}")
    print(f"Downloading to: {out_path}")
    stream.download(output_path=str(out_path))
    print("\nDownload complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a YouTube video (use only for content you own or are allowed to download).")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", default=".", help="Output directory")
    parser.add_argument("-r", "--resolution", help="Desired resolution, e.g. 720p")
    args = parser.parse_args()

    try:
        download(args.url, args.output, args.resolution)
    except Exception as exc:
        print("Error:", exc)
        sys.exit(1)
# ...existing code...