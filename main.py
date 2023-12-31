import tkinter as tk
from extractor import extractor

# Initalize tkinter 
root = tk.Tk() 
root.geometry('600x400')
root.title('Youtube MP3 Extractor')
root.iconbitmap('imgs/icon.ico')
root.resizable(False, False)
root['bg'] = '#000000'

#Add text
text = tk.Label(root, height=3, width=70, bg='#000000', fg='#FFFFFF', text='Enter Youtube URL:', font=('Ariel',20))
text.pack(pady=20)

#Get youtube link
youtubelink = tk.Text(root, height=1.5, width=70)
youtubelink.pack(pady=20)

#make extractor object
link = extractor(youtubelink)

#make button to download
download_img = tk.PhotoImage(file='imgs/download.png')
download_button = tk.Button(root,image=download_img,command=link.download_file,border='2')
download_button.pack(pady=30)

root.mainloop() 