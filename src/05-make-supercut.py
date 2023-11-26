from pydub import AudioSegment
import os
import json
import pandas as pd

def make_supercut(filename, output_format="mp3"):
    """
    Creates a supercut by extracting segments from an audio file based on timestamps.

    Args:
        filename (str): The name of the audio file (without extension).
        output_format (str): The format of the exported audio file.

    Raises:
        FileNotFoundError: If the MP3 file or timestamps file is not found.
        JSONDecodeError: If the JSON file is not properly formatted.

    Returns:
        None
    """
    mp3_filename = f"data/podcasts/{filename}.mp3"
    if not os.path.exists(mp3_filename):
        raise FileNotFoundError(f"MP3 file '{mp3_filename}' not found.")

    audio = AudioSegment.from_file(mp3_filename)

    timestamps_filename = f"data/timestamps_sentences/{filename}.json"
    if not os.path.exists(timestamps_filename):
        raise FileNotFoundError(f"Timestamps file '{timestamps_filename}' not found.")

    try:
        with open(timestamps_filename, 'r') as file:
            phrases = json.load(file)
            
        if not phrases:
            print(f"Skipping {filename} as it doesn't have any timestamps.")
            return
    except json.JSONDecodeError as e:
        raise e

    very_good_segments = [audio[int(phrase['start'] * 1000):int(phrase['end'] * 1000)] for phrase in phrases]

    supercut = sum(very_good_segments, AudioSegment.silent(duration=0))

    supercuts_dir = "data/supercuts_by_episode/"
    os.makedirs(supercuts_dir, exist_ok=True)
    output_filename = f"{supercuts_dir}{filename}.{output_format}"
    supercut.export(output_filename, format=output_format)
    print(f"Exported supercut to {output_filename}")



# read in the episode titles
with open("data/metadata/episodes.json", 'r') as file:
    episodes_data = json.load(file)

# create a DataFrame
df_episodes = pd.DataFrame(episodes_data)

output_dir = "data/supercuts_by_episode"
# ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# loop through the episodes using title
for title in df_episodes['title']:
    try:
        output_filename = f"{output_dir}/{title}.mp3"
        if os.path.exists(output_filename):
            print(f"Skipping {title} as it already exists in the output directory.")
            continue
        make_supercut(title)
    except FileNotFoundError:
        print(f"Skipping {title} as it doesn't have a timestamps file.")
    except Exception as e:
        print(f"Error processing {title}: {e}")