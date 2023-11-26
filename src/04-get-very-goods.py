import json
import os

def extract_very_good_instances(title):
    # File path to the transcript JSON file
    file_path = "data/transcripts/" + title

    # Load the JSON file
    with open(file_path, 'r') as file:
        transcript_data = json.load(file)

    # Extract words data from the transcript
    words_data = transcript_data['results']['channels'][0]['alternatives'][0]['words']

    # Search for instances of "Very good" said by speaker 1
    very_good_instances = []

    for i in range(len(words_data) - 1):
        if (words_data[i]['word'].lower() == "very" and
            words_data[i + 1]['word'].lower() == "good" and
            words_data[i]['speaker'] == 1 and
            words_data[i + 1]['speaker'] == 1):
            very_good_instances.append({
                "start": words_data[i]['start'],
                "end": words_data[i + 1]['end']
            })

    # Save the output to JSON
    # Ensure the directory exists at "data/timestamps/"
    os.makedirs("data/timestamps/", exist_ok=True)
    output_file_path = os.path.join("data/timestamps", os.path.basename(file_path))
    with open(output_file_path, 'w') as output_file:
        json.dump(very_good_instances, output_file)

    print(f"Saved {len(very_good_instances)} instances of 'Very good' to {output_file_path}")

def process_transcripts():
    # Read the episode titles from "data/metadata/episodes.json"
    with open("data/metadata/episodes.json", 'r') as file:
        episodes_data = json.load(file)
    
    # Loop through the episodes
    for episode in episodes_data:
        title = episode['title']
        file_path = title + ".json"
        output_file_path = os.path.join("data/timestamps", os.path.basename(file_path))
        if os.path.exists(output_file_path):
            print(f"Skipping {title} as it already exists in data/timestamps")
            continue
        extract_very_good_instances(file_path)

process_transcripts()
