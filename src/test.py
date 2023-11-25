import json

# File path to the transcript JSON file
file_path = "data/transcripts/195. Question Time: Is Sunak's Rwanda plan doomed to fail?.json"

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
            "phrase": "Very good",
            "start": words_data[i]['start'],
            "end": words_data[i + 1]['end']
        })

very_good_instances

