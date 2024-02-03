from googleapiclient.discovery import build

API_KEY = 'AIzaSyCREHc4q2xwhqyFXsA6kmhwkol1-NeMOqM'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

#################### new function


search_query = 'pride and prejudice'

search_response = youtube.search().list(
    q=search_query,
    part='id,snippet',
    type='video',
    order='relevance',  # You can change this to other options like 'date', 'rating', etc.
).execute()

for item in search_response['items']:
    video_title = item['snippet']['title']
    video_id = item['id']['videoId']
    
    print(f'Title: {video_title}, URL: https://www.youtube.com/watch?v={video_id}')
    
