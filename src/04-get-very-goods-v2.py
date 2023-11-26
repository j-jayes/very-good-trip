import json
import os

output_dir = "data/timestamps_sentences/"

def extract_very_good_instances(title):
    # File path to the transcript JSON file
    file_path = "data/transcripts/" + title

    # Load the JSON file
    with open(file_path, 'r') as file:
        transcript_data = json.load(file)

    # Extract paragraphs data from the transcript
    paragraphs_data = transcript_data['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']

    # Search for instances of sentences containing "Very good" said by speaker 1
    very_good_instances = []

    for paragraph in paragraphs_data:
        if paragraph['speaker'] == 1:
            for sentence in paragraph['sentences']:
                if 'very good' in sentence['text'].lower():
                    very_good_instances.append({
                        "start": sentence['start'],
                        "end": sentence['end'],
                        "text": sentence['text']

                    })

    # Save the output to JSON
    # Ensure the directory exists at "data/timestamps/"
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, os.path.basename(file_path))
    with open(output_file_path, 'w') as output_file:
        json.dump(very_good_instances, output_file, indent=4)

    print(f"Saved {len(very_good_instances)} instances of 'Very good' to {output_file_path}")


def process_transcripts():
    # Read the episode titles from "data/metadata/episodes.json"
    with open("data/metadata/episodes.json", 'r') as file:
        episodes_data = json.load(file)
    
    # Loop through the episodes
    for episode in episodes_data:
        title = episode['title']
        file_path = title + ".json"
        output_file_path = os.path.join(output_dir, os.path.basename(file_path))
        if os.path.exists(output_file_path):
            print(f"Skipping {title} as it already exists in data/timestamps")
            continue
        extract_very_good_instances(file_path)

process_transcripts()
