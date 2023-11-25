
# Rory Stewart "Very Good" Supercut Project

#### Overview

This project aims to create a supercut of all instances where Rory Stewart says "very good" in the "The Rest Is Politics" podcast. We will download podcast episodes, use automatic speech transcription and diarization to identify the relevant segments, and then edit these segments together.

#### Project Structure

- **data/**: Contains downloaded podcast audio files.
- **transcripts/**: Stores the generated transcripts of the podcasts.
- **output/**: Final supercut audio files.

#### Requirements

- **Python**: For running scripts and data analysis.
- **Deepgram**: Used for speech transcription and diarization.
- **Audio Editing Software**: For cutting and joining audio segments (e.g., Audacity, Adobe Audition).
- **Podbean**: To download podcast episodes.

#### Steps

1. **Download Podcast Episodes**
   - Utilize Podbean to download the required episodes of "The Rest Is Politics" podcast.

2. **Transcription and Diarization**
   - Use Deepgram for transcribing the downloaded audio files.
   - Implement diarization to differentiate between speakers and identify when Rory Stewart is speaking.

3. **Analysis Script**
   - Write a Python script to parse the transcripts and identify instances of Rory Stewart saying "very good".
   - Extract timestamps of these instances for audio editing.

4. **Audio Editing**
   - Use an audio editing tool to cut the identified segments from the original audio files.
   - Merge these segments to create the supercut.

5. **Final Output**
   - Save the final supercut in the 'output' folder.

#### Installation and Usage

- Install Python and required libraries (e.g., `requests`, `json`, `pydub`).
- Setup Deepgram account and obtain API key.
- Clone the repository and navigate to the project directory.
- Run the analysis script: `python script_name.py`.
- Manually edit the audio as per the timestamps obtained.

#### Contributing

Feel free to contribute to this project by improving the analysis script, optimizing the audio editing process, or suggesting better transcription methods.

#### License

Specify the license under which this project is released.

---

This README provides a clear and concise overview of your project, including its purpose, structure, and the steps involved in the analysis. The 'Contributing' and 'License' sections can be tailored to your preferences for collaboration and distribution.