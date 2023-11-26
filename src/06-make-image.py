import json
import os
from PIL import Image, ImageDraw, ImageFont
from pydub import AudioSegment
import subprocess
import pandas as pd

def create_highlighted_images(text, index, output_dir):
    img = Image.new('RGB', (800, 200), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    highlighted_text = text.replace('very good', '[very good]')  # Example highlighting
    d.text((10, 10), highlighted_text, font=font, fill=(0, 0, 0))
    img.save(os.path.join(output_dir, f'image_{index}.png'))

def process_episode(title):
    # Paths for the transcript, timestamps, and audio
    transcript_path = f"data/transcripts/{title}.json"
    timestamps_path = f"data/timestamps_sentences/{title}.json"
    audio_path = f"data/supercuts_by_episode/{title}.mp3"

    if not os.path.exists(transcript_path) or not os.path.exists(timestamps_path) or not os.path.exists(audio_path):
        print(f"Missing files for episode: {title}")
        return

    # Read timestamps and phrases
    with open(timestamps_path, 'r') as file:
        phrases = json.load(file)

    # Create images directory for the episode
    images_dir = f"data/images/{title}"
    os.makedirs(images_dir, exist_ok=True)

    for i, phrase in enumerate(phrases):
        create_highlighted_images(phrase['text'], i, images_dir)

    # Here you can add the logic to create video clips from these images and synchronize with the audio
    # ...

    # After creating and synchronizing each individual clip, concatenate them into one final video
    # ...

    print(f"Processed episode: {title}")

# Read in the episode titles
with open("data/metadata/episodes.json", 'r') as file:
    episodes_data = json.load(file)
    # make it a pandas DataFrame
    df_episodes = pd.DataFrame(episodes_data)

for title in df_episodes:
    process_episode(title)
