"""
This script fetches episode information from an RSS feed and stores it in a JSON file.

The script performs the following steps:
1. Imports the necessary libraries: feedparser and pandas.
2. Defines the RSS feed URL.
3. Parses the RSS feed using feedparser.
4. Initializes an empty list to store episode data.
5. Extracts episode details from the parsed feed and appends them to the episodes list.
6. Creates a DataFrame from the episodes list using pandas.
7. Saves the DataFrame as a JSON file at 'data/metadata/episodes.json'.

Note: Make sure to have the necessary libraries installed before running this script.
"""

import feedparser
import pandas as pd

def store_episode_info(rss_url, output_file):
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # List to store episode data
    episodes = []

    # Extract episode details
    for entry in feed.entries:
        episode_info = {
            "title": entry.title,
            "published_date": entry.published,
            "description": entry.description,
            "audio_url": entry.enclosures[0]['href']
        }
        episodes.append(episode_info)

    # Create a DataFrame
    df_episodes = pd.DataFrame(episodes)

    # Save the DataFrame as a JSON file
    df_episodes.to_json(output_file, orient="records", indent=4)

# Call the function
rss_url = "https://feeds.megaphone.fm/GLT9190936013"
output_file = "data/metadata/episodes.json"
store_episode_info(rss_url, output_file)
