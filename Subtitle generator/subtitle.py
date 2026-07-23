import os
from flask import Flask, render_template, request
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
import srt
import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGINAL_SRT_PATH = os.path.join(BASE_DIR, "subtitles.srt")
SHIFTED_SRT_PATH = os.path.join(UPLOAD_FOLDER, "temp_shifted.srt")

def generator(txt):
    return TextClip(
        text=txt, 
        font=r'C:\Windows\Fonts\arial.ttf',          
        font_size=24,           
        color='white',         
        stroke_color='black',  
        stroke_width=1,        
        method='caption',      
        size=(video.w - 100, None)  
    )
def shift_subtitles(srt_path, output_path, offset_seconds):
    with open(srt_path, 'r', encoding='utf-8') as f:
        subtitles = list(srt.parse(f.read()))
    for sub in subtitles:
        sub.start += datetime.timedelta(seconds=offset_seconds)
        sub.end += datetime.timedelta(seconds=offset_seconds)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(srt.compose(subtitles))
def subtitle(video_path, srt_path, output_path):
    global video
    video = VideoFileClip(video_path)
    subtitles = SubtitlesClip(srt_path, make_textclip=generator, encoding='utf-8')
    subtitles = subtitles.with_duration(video.duration)
    final_video = CompositeVideoClip([
        video, 
        subtitles.with_position(('center', 'bottom'))
    ])
    final_video = final_video.with_audio(video.audio)
    final_video.write_videofile(
        output_path, 
        fps=video.fps, 
        codec="libx264", 
        audio_codec="aac",
        audio=True,
        temp_audiofile="temp-audio.m4a", 
        remove_temp=True
    )
    video.close()
    final_video.close()

@app.route('/')
def home():
    return render_template('subtitle.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'video_file' not in request.files:
        return "No file part", 400
    file = request.files['video_file']
    if file.filename == '':
        return "No selected file", 400
    try:
        shift_amount = float(request.form.get('shift_seconds', 0))
    except ValueError:
        shift_amount = 0.0
    if file:
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)
        try:
            shift_subtitles(ORIGINAL_SRT_PATH, SHIFTED_SRT_PATH, shift_amount)
            srt_to_use = SHIFTED_SRT_PATH
        except FileNotFoundError:
            return "Error: Base subtitles.srt file not found on the server.", 400
        output_filename = "result.mp4"
        output_path = os.path.join(STATIC_FOLDER, output_filename)
        subtitle(input_path, srt_to_use, output_path)
        os.remove(input_path)
        if os.path.exists(SHIFTED_SRT_PATH):
            os.remove(SHIFTED_SRT_PATH)
        
        video_url = f"/{STATIC_FOLDER}/{output_filename}"
        return render_template('subtitle.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)