import os
import requests
import pandas as pd
from dotenv import load_dotenv
import json

# Load Deepgram API Key from .env file
load_dotenv()
deepgram_api_key = os.getenv('deepgram_api_key')

# Ensure API key is available
if not deepgram_api_key:
    raise ValueError("Deepgram API key not found. Please check your .env file.")

# Load the DataFrame containing the podcast episodes from data/metadata/episodes.json
df_episodes = pd.read_json("data/metadata/episodes.json")

# Deepgram API URL and Headers
url = "https://api.deepgram.com/v1/listen"
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": f"Token {deepgram_api_key}"
}

def transcribe_audio(audio_url):
    """Transcribe audio from a URL using Deepgram API."""
    # Print the URL to track progress
    print(f"Transcribing: {audio_url}")

    # Updated URL with parameters
    params_url = f"{url}?punctuate=true&diarize=true&smart_format=true&paragraphs=true&model=nova-2"
    
    # Payload only contains the audio URL
    payload = {"url": audio_url}

    response = requests.post(params_url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: Unable to transcribe URL - {audio_url}")
        return None


# Assuming df_episodes is your DataFrame containing the episodes
# Replace 'df_episodes' with the actual variable name if different
for index, row in df_episodes.iterrows():
    file_name = row['title'] + ".json"
    file_path = os.path.join("data/transcripts/", file_name)
    
    # Check if transcript file already exists
    if os.path.exists(file_path):
        print(f"Transcript file already exists for episode: {row['title']}")
        continue
    
    transcript = transcribe_audio(row['audio_url'])
    if transcript:
        # Save the transcript to a file or process as needed
        # Example: Saving as a JSON file with the name of the episode from the DataFrame column called title
        # Ensure the directory exists at "data/transcripts/"
        os.makedirs("data/transcripts/", exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump(transcript, file, ensure_ascii=False, indent=4)
