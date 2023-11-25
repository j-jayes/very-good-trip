import requests
import feedparser
import os

def download_podcasts(rss_url, save_directory):
    """
    Downloads podcasts from an RSS feed and saves them to a specified directory.

    Args:
        rss_url (str): The URL of the RSS feed.
        save_directory (str): The directory to save the audio files.

    Returns:
        None
    """

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Create the save directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Download each episode
    for entry in feed.entries:
        file_name = entry.title + ".mp3"
        file_path = os.path.join(save_directory, file_name)

        # Check if the file already exists
        if not os.path.exists(file_path):
            audio_url = entry.enclosures[0]['href']  # URL of the audio file

            try:
                response = requests.get(audio_url, stream=True)

                if response.status_code == 200:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                    print(f"Downloaded: {file_name}")
                else:
                    print(f"Failed to download {file_name} - HTTP {response.status_code}")

            except Exception as e:
                print(f"Error downloading {file_name}: {e}")
        else:
            print(f"File already exists: {file_name}")

    print("All downloads complete.")

rss_url = "https://feeds.megaphone.fm/GLT9190936013"
save_directory = "data/podcasts/"

download_podcasts(rss_url, save_directory)