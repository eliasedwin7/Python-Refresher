import os
import re
import pyttsx3
from pydub import AudioSegment

def clean_markdown(text):
    text = re.sub(r'[`#>*_~]', '', text)  # Remove markdown characters
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)  # Replace links
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # Remove images
    return text.strip()

def md_to_mp3(input_folder, output_folder):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".md"):
            full_path = os.path.join(input_folder, file)
            with open(full_path, 'r', encoding='utf-8') as f:
                raw_text = f.read()
                text = clean_markdown(raw_text)

            print(f"🗣️ Converting: {file}")
            temp_wav = os.path.join(output_folder, "temp.wav")
            engine.save_to_file(text, temp_wav)
            engine.runAndWait()

            mp3_name = os.path.splitext(file)[0] + ".mp3"
            mp3_path = os.path.join(output_folder, mp3_name)
            sound = AudioSegment.from_wav(temp_wav)
            sound.export(mp3_path, format="mp3")
            print(f"✅ Saved: {mp3_path}")

    os.remove(temp_wav)
    print("🎉 All markdown files converted to MP3!")

# Example use:
md_to_mp3(".", "output")
