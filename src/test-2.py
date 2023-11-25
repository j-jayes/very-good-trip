from pydub import AudioSegment
audio = AudioSegment.from_file("data/podcasts/test.mp3")

very_good_segments = []

phrases = [{'phrase': 'Very good', 'start': 28.135, 'end': 28.615}, {'phrase': 'Very good', 'start': 514.265, 'end': 514.505}, {'phrase': 'Very good', 'start': 1217.68, 'end': 1218.24}, {'phrase': 'Very good', 'start': 1231.95, 'end': 1232.51}, {'phrase': 'Very good', 'start': 1238.99, 'end': 1239.31}, {'phrase': 'Very good', 'start': 1743.755, 'end': 1744.6349}, {'phrase': 'Very good', 'start': 1981.165, 'end': 1981.725}]

# extract timestamps
timestamps = []
for phrase in phrases:
    timestamps.append({
        "start": phrase['start'],
        "end": phrase['end']
    })

very_good_segments = []

for timestamp in timestamps:
    start_ms = int(timestamp['start'] * 1000)
    end_ms = int(timestamp['end'] * 1000)
    segment = audio[start_ms:end_ms]
    very_good_segments.append(segment)

# Concatenate all segments
supercut = very_good_segments[0]
for segment in very_good_segments[1:]:
    supercut += segment


supercut.export("very_good_supercut.mp3", format="mp3")
