import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import Playlist
from ttkwidgets import CheckboxTreeview
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('550x400')
        self.title('تحميل من اليوتيوب')
        tkvar = dict()
        def download():
            children = tree.get_children()
            links = plst.get()
            play_list = Playlist(links)
            Dir = dirr.get()
            count = 0
            cunt=0
            success=0
            for child in children:
                tkvar[cunt]=child
                cunt+=1
            try:
                for video in play_list.videos:
                        if str(tree.item(tkvar[count], 'tags'))== "('checked',)":
                            video.streams.get_highest_resolution().download(Dir)
                            success+=1
                        count += 1
                messagebox.showinfo('انتهى التحميل',f'تم تحميل '
                                                    f'{success} فيديو بنجاح يمكن ')
            except :
                messagebox.showerror('', 'حدث خطأ')
        def search():
            links = plst.get()
            play_list = Playlist(links)
            count = 0
            for video in play_list.videos:
                tree.insert('', count, values={video.title})
                count += 1
        frame=tk.LabelFrame(self, text='', padx=10, pady=10)
        frame.grid(pady=10, padx=10)
        frame2=tk.LabelFrame(self, text='', padx=10, pady=10)
        frame2.grid(column=0,pady=10, padx=10,sticky=tk.W)
        plst = ttk.Entry(frame,width=50)
        plst.grid(row=0, padx=20 , pady=5)
        dirr = ttk.Entry(frame,width=50)
        dirr.grid(row=1, padx=20, pady=5)
        ttk.Button(frame,
                   text='بحث', width=20,
                   command=lambda: (search())).grid(row=0, column=1, padx=20, pady=5)
        ttk.Button(frame,
                   text='تحميل', width=20,
                   command=lambda: (download())).grid(row=1, column=1, padx=20, pady=5)
        tree=CheckboxTreeview(frame2,columns='Video')
        tree.heading('Video',text='Video')
        tree.column("#0", width=50)
        tree.column("#1", width=300)
        tree.grid(row=0,column=0,sticky=tk.W)
App().mainloop()