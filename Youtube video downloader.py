from pytube import YouTube

# YouTube video link
link = "https://www.youtube.com/watch?v=fCUPzgoABQQ"

# Create YouTube object
youtube_1 = YouTube(link)

# Print video details
print("Title:", youtube_1.title)
print("Thumbnail URL:", youtube_1.thumbnail_url)

# Get available streams
videos = youtube_1.streams

# List available streams
vid = list(enumerate(videos))
for i in vid:
    print(i)

# Choose and download
strm = int(input("Enter the stream number: "))
videos[strm].download()
print("Downloaded successfully!")

# videos = youtube_1.streams.filter(only_audio=True)
# to download entire playlist

# from pytube import Playlist
# py = Playlist("")
# print('Downloading : {py.title}')

# for video in py.videos:
#     video.streams.first().download()