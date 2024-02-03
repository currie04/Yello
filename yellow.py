from googleapiclient.discovery import build

API_KEY = 'AIzaSyCREHc4q2xwhqyFXsA6kmhwkol1-NeMOqM'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
Urls = []

class Yello:
    def __init__(self, row_query_topic):
        search_query = row_query_topic
        search_response = youtube.search().list(
            q=search_query,
            part='id,snippet',
            type='video',
            order='relevance',  # You can change this to other options like 'date', 'rating', etc.
        ).execute()

        for item in search_response['items']:
            video_title = item['snippet']['title']
            video_id = item['id']['videoId']
            Urls.append(f'https://www.youtube.com/watch?v={video_id}') 

    def display_urls(self):
        for i in Urls:
            print(i)

# Example usage of the Yello class
search_topic = 'Python programming'  # Replace with your desired search topic
yello_instance = Yello(search_topic)
yello_instance.display_urls()

