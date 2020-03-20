from pytube import YouTube

yt =YouTube("https://www.youtube.com/watch?v=Tqsz6fjvhZM")

dw = yt.streams.get_highest_resolution()
dw.download("C:/Users/acer/Desktop")