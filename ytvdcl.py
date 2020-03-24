from pytube import YouTube

video_links = open("links list.txt","r")
for i in video_links:
    yt =YouTube(i)
    dw = yt.streams.get_highest_resolution()
    dw.download("C:/Users/acer/Desktop")
    print("Downloaded",i)