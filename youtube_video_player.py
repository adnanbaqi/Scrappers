import time
import pandas as pd
from pytube import YouTube

csv_file_path = r'C:\Users\adnan\OneDrive\Documents\data1.csv'
df = pd.read_csv(csv_file_path)

def download_video(video_id, output_path):
    try:
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'
        yt = YouTube(youtube_url)
        stream = yt.streams.get_lowest_resolution() 
        print(f"Downloading: {yt.title}")
        stream.download(output_path)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error downloading {video_id}: {e}")


output_folder = r'C:\Users\adnan\Downloads\vid_data1' 
selected_indices = []

for index, row in df.iterrows():
    video_id = row['Id']  

    print(f"Video {index + 1}/{len(df)}:")
    print(f"Title: {row['Title']}") 
    print("Do you want to download this video? (y/n): ", end="")
    
    choice = input().strip().lower()
    if choice == 'y':
        selected_indices.append(index)


delay_seconds = 1000
for index in selected_indices:
    video_id = df.loc[index, 'Id']
    download_video(video_id, output_folder)
    time.sleep(delay_seconds)

print("Download completed.")
