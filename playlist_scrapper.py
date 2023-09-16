import csv
import os
from pytube import YouTube, Playlist
from tqdm import tqdm

# Define the YouTube playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLFjydPMg4Dapq9vcdmGyHs8uJhiqMgUrX"

# Initialize an empty list to store video details
video_details = []

# Function to fetch video details and add them to the list
def get_video_details(video_url):
    yt = YouTube(video_url)
    video_details.append({
        "Video Title": yt.title,
        "Video URL": video_url,
        "Video Author": yt.author,
        "Video Views": yt.views,
        "Video Length": yt.length,
    })

# Create a Playlist object
playlist = Playlist(playlist_url)

# Get the user's home directory and set the CSV file location in the Downloads folder
download_folder = os.path.expanduser("~/Downloads")
csv_filename = os.path.join(download_folder, "youtube_playlist.csv")

# Create a tqdm progress bar to track scraping progress
with tqdm(total=len(playlist.video_urls), desc="Scraping Progress") as pbar:
    # Iterate through each video in the playlist and get details
    for video_url in playlist.video_urls:
        get_video_details(video_url)
        pbar.update(1)  # Update the progress bar

# Write the video details to a CSV file in the Downloads folder
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["Video Title", "Video URL", "Video Author", "Video Views", "Video Length"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write video details for each video
    for video_detail in video_details:
        writer.writerow(video_detail)

print(f"Scraped {len(video_details)} videos and saved to {csv_filename}")
