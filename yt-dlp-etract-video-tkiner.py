import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import os
import threading
"""
download video from youtube, arrange the youtube videoes url as a playlist or can get playlist directly using the command as follow:
    yt-dlp --flat-playlist --get-url https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID > video_links.txt
"""
class VideoDownloaderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video Downloader")
        self.geometry("600x400")

        # Variables
        self.urls_file_path = tk.StringVar()
        self.download_directory = tk.StringVar()

        self.thread = None
        self.process = None

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # URLs File Selection
        tk.Label(self, text="URLs File:").pack(pady=5)
        tk.Entry(self, textvariable=self.urls_file_path, width=50).pack(pady=5)
        tk.Button(self, text="Browse", command=self.browse_urls_file).pack(pady=5)

        # Download Directory Selection
        tk.Label(self, text="Download Directory:").pack(pady=5)
        tk.Entry(self, textvariable=self.download_directory, width=50).pack(pady=5)
        tk.Button(self, text="Browse", command=self.browse_download_directory).pack(pady=5)

        # Download Button
        tk.Button(self, text="Start Download", command=self.start_download_thread).pack(pady=10)

        # Log Area
        self.log_area = scrolledtext.ScrolledText(self, width=70, height=100)
        self.log_area.pack(pady=10)

    def browse_urls_file(self):
        file_path = filedialog.askopenfilename()
        self.urls_file_path.set(file_path)

    def browse_download_directory(self):
        directory = filedialog.askdirectory()
        self.download_directory.set(directory)

    def log_message(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def download_video(self, url):
        try:
            command = f'yt-dlp -f "bestvideo+bestaudio/best" -o "{self.download_directory.get()}/%(title)s.%(ext)s" {url}'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True, encoding="utf-8")
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    self.log_message(output.strip())
            stderr = process.communicate()[1]
            if process.returncode != 0:
                raise Exception(stderr)
            return True
        except Exception as e:
            self.log_message(f"下载失败: {url} - {e}")
            return False

    def download_videos(self):
        with open(self.urls_file_path.get(), 'r') as f:
            urls = f.read().splitlines()

        for url in urls:
            if not url.strip():
                continue
            self.log_message(f"正在下载: {url}")
            success = self.download_video(url)
            if not success:
                self.log_message(f"下载失败: {url}")

    def start_download_thread(self):
        if not self.urls_file_path.get() or not self.download_directory.get():
            messagebox.showerror("Error", "Please select URLs file and download directory.")
            return
        threading.Thread(target=self.download_videos, daemon=True).start()

    def stop_scene_detection(self):
        if self.thread and self.thread.is_alive():
            if self.process:
                self.process.terminate()
            self.log_message("Scene detection stopped.")
            self.thread = None

if __name__ == "__main__":
    app = VideoDownloaderApp()
    app.mainloop()
