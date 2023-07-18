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
        if "playlist" in url:
            playlist = Playlist(url)
            playlist.populate_video_urls()
            total_videos = len(playlist.video_urls)
            counter = 1
            output_path = "D:/DESCARGAS"
            for video_url in playlist.video_urls:
                yt = YouTube(video_url)
                video = yt.streams.filter(only_audio=True).first()
                video.download(output_path=output_path)
                counter += 1
            return f"Descarga exitosa ({counter-1}/{total_videos})", 200
        else:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            output_path = "D:/DESCARGAS"
            video.download(output_path=output_path)
            return "Descarga exitosa (1/1)", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()
