from moviepy import ImageClip, AudioFileClip

image = ImageClip("img.jpg").with_duration(10)  # Set a default duration for the image
audio = AudioFileClip("music.mp3").subclipped(0, 10)  # Set a default duration for the audio

# Make image duration equal to audio duration
video = image.with_duration(audio.duration)

# Add audio
video = video.with_audio(audio)

# Create MP4
video.write_videofile(
    "wedding_invitation.mp4",
    fps=30,
    codec="libx264",
    audio_codec="aac"
)

audio.close()
video.close()