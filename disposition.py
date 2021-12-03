from moviepy.editor import *
import shutil
import os


def count_to_disposition(video_count, clips):
    logo = ImageClip("./img/logo.png")
    if video_count == 1:
        clip = clips_array([clips])
        clip.write_videofile("clip.mp4")
        logo.set_duration(clip.duration)
        final_clip = CompositeVideoClip([clip, logo]).set_duration(clip.duration)
        final_clip.write_videofile("video1.mp4")
        os.remove("./clip.mp4")
        shutil.move("video1.mp4", os.path.join("./result", "video1.mp4"))
    elif video_count == 2:
        clip = clips_array([clips])
        clip.write_videofile("clip.mp4")
        logo.set_duration(clip.duration)
        final_clip = CompositeVideoClip([clip, logo]).set_duration(clip.duration)
        final_clip.write_videofile("video2.mp4")
        os.remove("./clip.mp4")
        shutil.move("video2.mp4", os.path.join("./result", "video2.mp4"))
    elif video_count == 3:
        clip = clips_array([clips])
        clip.write_videofile("clip.mp4")
        logo.set_duration(clip.duration)
        final_clip = CompositeVideoClip([clip, logo]).set_duration(clip.duration)
        final_clip.write_videofile("video3.mp4")
        os.remove("./clip.mp4")
        shutil.move("video3.mp4", os.path.join("./result", "video3.mp4"))
    elif video_count == 4:
        clip = clips_array([clips])
        clip.write_videofile("clip.mp4")
        logo.set_duration(clip.duration)
        final_clip = CompositeVideoClip([clip, logo]).set_duration(clip.duration)
        final_clip.write_videofile("video4.mp4")
        os.remove("./clip.mp4")
        shutil.move("video4.mp4", os.path.join("./result", "video4.mp4"))
    elif video_count == 5:
        clip = clips_array([clips[:3], clips[3:]])
        clip.write_videofile("clip.mp4")
        logo.set_duration(clip.duration)
        final_clip = CompositeVideoClip([clip, logo]).set_duration(clip.duration)
        final_clip.write_videofile("video5.mp4")
        os.remove("./clip.mp4")
        shutil.move("video5.mp4", os.path.join("./result", "video5.mp4"))
    elif video_count == 6:
        clip = clips_array([clips[:3], clips[3:]])
        clip.write_videofile("clip.mp4")
        logo.set_duration(clip.duration)
        final_clip = CompositeVideoClip([clip, logo]).set_duration(clip.duration)
        final_clip.write_videofile("video6.mp4")
        os.remove("./clip.mp4")
        shutil.move("video6.mp4", os.path.join("./result", "video6.mp4"))
    elif video_count == 7:
        clip = clips_array([clips[:4], clips[4:]])
        clip.write_videofile("clip.mp4")
        logo.set_duration(clip.duration)
        final_clip = CompositeVideoClip([clip, logo]).set_duration(clip.duration)
        final_clip.write_videofile("video7.mp4")
        os.remove("./clip.mp4")
        shutil.move("video7.mp4", os.path.join("./result", "video7.mp4"))
    elif video_count == 8:
        clip = clips_array([clips[:4], clips[4:]])
        clip.write_videofile("clip.mp4")
        logo.set_duration(clip.duration)
        final_clip = CompositeVideoClip([clip, logo]).set_duration(clip.duration)
        final_clip.write_videofile("video8.mp4")
        os.remove("./clip.mp4")
        shutil.move("video8.mp4", os.path.join("./result", "video8.mp4"))