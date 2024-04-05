# i am using chatgpt to make this
# at this point i am tryhing to make it so that i can input txt files 

import subprocess
from gtts import gTTS

def play_audio(filename):
    subprocess.run(["mpv", filename])

# Read English text from file
with open("en.txt", "r", encoding="utf-8") as f:
    english_text = f.read()

# Read Greek text from file
with open("gr.txt", "r", encoding="utf-8") as f:
    greek_text = f.read()

# Generate audio for English text
english_tts = gTTS(text=english_text, lang='en', slow=False)
english_temp_audio_file = "output_english.mp3"
english_tts.save(english_temp_audio_file)

subprocess.run(["ffmpeg", "-i", english_temp_audio_file, "output_english.wav"], check=True)

# Generate audio for Greek text
greek_tts = gTTS(text=greek_text, lang='el', slow=False)
greek_temp_audio_file = "output_greek.mp3"
greek_tts.save(greek_temp_audio_file)

subprocess.run(["ffmpeg", "-i", greek_temp_audio_file, "output_greek.wav"], check=True)

# Adjust pitch shift factor (lower values for deeper male voice)
pitch_shift_factor = -4
# Adjust speech rate (lower values for slower speech)
speech_rate = 1.2

# Apply pitch shifting and speech rate adjustment for English text
subprocess.run(["rubberband", "-p", str(pitch_shift_factor), "output_english.wav", "output_english_temp.wav"], check=True)
subprocess.run(["rubberband", "-t", str(speech_rate), "output_english_temp.wav", "output_english_male.wav"], check=True)

# Apply pitch shifting and speech rate adjustment for Greek text
subprocess.run(["rubberband", "-p", str(pitch_shift_factor), "output_greek.wav", "output_greek_temp.wav"], check=True)
subprocess.run(["rubberband", "-t", str(speech_rate), "output_greek_temp.wav", "output_greek_male.wav"], check=True)

subprocess.run(["rm", english_temp_audio_file, "output_english.wav", "output_english_temp.wav"], check=True)
subprocess.run(["rm", greek_temp_audio_file, "output_greek.wav", "output_greek_temp.wav"], check=True)

print("Male voices generated successfully.")

# Play English male voice
play_audio("output_english_male.wav")

# Play Greek male voice
play_audio("output_greek_male.wav")

