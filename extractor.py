import os
from pytube import YouTube 
from tkinter import filedialog

class extractor:
    def __init__(self,urltext):
        self.urltext = urltext 
        self.url = None 
        self.path = None

    def get_directory(self, filename):
        self.path = (filedialog.askdirectory()+ '\\' + filename + '.mp3')
    
    def get_url(self):
        self.url = self.urltext.get('1.0','end')

    def download_file(self):
        self.get_url()
        yt = YouTube(self.url)
        try:
            video = yt.streams.filter(only_audio=True).first()
            out_file= video.download()
            file = os.path.basename(out_file)
            file_name = os.path.splitext(file)[0]
            self.get_directory(file_name)
            os.rename(out_file, self.path)
            print("DONE!")
        except:
            print("Invalid URL")