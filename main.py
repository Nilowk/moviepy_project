from moviepy.editor import *
from disposition import count_to_disposition
import paramiko
import ytb
import sys
import os
import json


#ytb.download("https://www.youtube.com/watch?v=GJAMjCWO2TI")
def load_json(file):
    with open(file, "r") as f:
        global data
        return json.load(f)


d = "data.json"
c = "config.json"
data = load_json(d)
config = load_json(c)
clips = []

if min([data[clip_id]["start"] for clip_id in data]) != 0:
    print("\033[91m" + "\033[1m" + "ERROR: no video start at 0s" + "\033[0m")
    sys.exit()

host, port = config["host"], config["port"]
transport = paramiko.Transport((host, port))

username, password = config["username"], config["password"]
transport.connect(None, username, password)

sftp = paramiko.SFTPClient.from_transport(transport)

for clip_id in data:
    local_path = os.path.join("./clips", f"{clip_id}.mp4")
    sftp.get(data[clip_id]["remote_path"] + f"{clip_id}.mp4", local_path)
    clip = VideoFileClip(local_path)
    clip = clip.set_start(data[clip_id]["start"])
    clip = clip.set_end(clip.duration + data[clip_id]["start"])
    clips.append(clip)

if sftp:
    sftp.close()
if transport:
    transport.close()

video_count = len([clip for clip in clips])
count_to_disposition(video_count, clips)


