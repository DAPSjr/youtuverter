import os
from flask import Flask, render_template, request, url_for
from pytube import Playlist, YouTube

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Youtuverter.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    try:
        download_folder = os.path.join(os.path.dirname(__file__), "songs")
        os.makedirs(download_folder, exist_ok=True)

        if "playlist" in url:
            playlist = Playlist(url)
            playlist.populate_video_urls()
            total_videos = len(playlist.video_urls)
            counter = 1
            for video_url in playlist.video_urls:
                yt = YouTube(video_url)
                video = yt.streams.filter(only_audio=True).first()
                video.download(output_path=download_folder)
                counter += 1
            return f"Descarga exitosa ({counter-1}/{total_videos})", 200
        else:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            video.download(output_path=download_folder)
            return "Descarga exitosa (1/1)", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()
