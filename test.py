import pytube

link = input('https://www.youtube.com/watch?v=Q9HDIjTy66A&list=PLKVEzjo-d1qEKvv9JnIRQpwkURsozZEte&index=18')
video_download = pytube.Youtube(link)
video_download.streams.first().download()
print('Video Downloaded', link)