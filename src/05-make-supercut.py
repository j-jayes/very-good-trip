from pydub import AudioSegment
import os

def make_supercut(filename):
    """
    Creates a supercut by extracting segments from an audio file based on timestamps.

    Args:
        filename (str): The name of the audio file (without extension).

    Raises:
        FileNotFoundError: If the MP3 file or timestamps file is not found.

    Returns:
        None
    """
    # Rest of the code...
def make_supercut(filename):
    # make the mp3 filename
    mp3_filename = "data/podcasts/" + filename + ".mp3"
    
    # Check if the mp3 file exists
    if not os.path.exists(mp3_filename):
        raise FileNotFoundError(f"MP3 file '{mp3_filename}' not found.")

    # Load the audio
    audio = AudioSegment.from_file(mp3_filename)

    # Load the timestamps
    timestamps_filename = "data/timestamps/" + filename + ".json"
    with open(timestamps_filename, 'r') as file:
        phrases = eval(file.read())

    # Extract segments
    very_good_segments = []
    for phrase in phrases:
        start_ms = int(phrase['start'] * 1000)
        end_ms = int(phrase['end'] * 1000)
        segment = audio[start_ms:end_ms]
        very_good_segments.append(segment)

    # Concatenate all segments
    supercut = very_good_segments[0]
    for segment in very_good_segments[1:]:
        supercut += segment

    # Export the supercut
    # Ensure the directory exists at "data/supercuts_by_episode/"
    supercuts_dir = "data/supercuts_by_episode/"
    os.makedirs(supercuts_dir, exist_ok=True)
    output_filename = supercuts_dir + filename + ".mp3"
    supercut.export(output_filename, format="mp3")
    print(f"Exported supercut to {output_filename}")

# Example usage
make_supercut("192. What David Cameron\u2019s return means for Israel-Gaza")