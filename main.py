from pytube import YouTube

path = input("Enter path of the youtube video: ")

try:
    video = YouTube(path)
except:
    print("Sorry some problem has occured or you have provided wrong video path")
else:
    video = YouTube(path)
    stream = video.streams.first()
    stream.download('.')