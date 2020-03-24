from pytube import YouTube

yt =YouTube("https://www.youtube.com/watch?v=2KsrtJ3VtZs")

dw = yt.streams.get_highest_resolution()
dw.download("C:/Users/acer/Desktop")