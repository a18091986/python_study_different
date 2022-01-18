from youtube_dl import YoutubeDL

def get_info_about_video(link):
    print("For: ", link)
    youtube_dl_opts = {
        'ignoreerrors': True,
        'quiet': False
    }

    with YoutubeDL(youtube_dl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        # for item in info_dict:
    #     print(item)
    #     video_id = info_dict.get("id", None)
    #     video_views = info_dict.get("view_count", None)
    #     video_date = info_dict.get("upload_date", None)
    #     video_duration = info_dict.get("duration", None)
        video_title = info_dict.get('title', None)
        uploader = info_dict.get('uploader', None)
        print(video_title, uploader)
        return video_title, uploader



# from youtube_dl import YoutubeDL
# video = "https://youtu.be/0Pq8vOVbvzs?list=WL"
#
# print("For: ", video)
#
# youtube_dl_opts = {
#     'ignoreerrors': True,
#     'quiet': False
# }
#
# with YoutubeDL(youtube_dl_opts) as ydl:
#     info_dict = ydl.extract_info(video, download=False)
#     # for item in info_dict:
#     #     print(item)
#     video_id = info_dict.get("id", None)
#     video_views = info_dict.get("view_count", None)
#     video_date = info_dict.get("upload_date", None)
#     video_duration = info_dict.get("duration", None)
#     video_title = info_dict.get('title', None)
#     uploader = info_dict.get('uploader', None)
#     print(video_id, video_views, video_date, video_duration, video_title, uploader)

