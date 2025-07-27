import subprocess

video_path=r"D:\code\python\terry_davis\God's_Wisdom\divine_intellect.mp4"
vlc_path=r"D:\softwares\VLC\vlc.exe"

subprocess.run([vlc_path, video_path, "--play-and-exit", "--fullscreen"])
