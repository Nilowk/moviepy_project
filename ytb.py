import youtube_dl


def download(youtube_link):
    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])