from news_parser import NVParser
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.parser = NVParser('http://nv.ua/allnews.html')
        self.data = self.parser.work()
        self.news = list()
        self.pack()
        self.create_main_layout()
        self.create_news_layout()
        self.create_news()

    def create_main_layout(self):
        self.main_canvas = tk.Canvas(self, width=800, height=800)
        self.main_canvas.pack()
        self.center_frame = tk.Frame(self.main_canvas, bg='#80C1FF', bd=5)
        self.center_frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

    def create_news_layout(self):
        refresh_button = tk.Button(self.center_frame, text='Refresh', command=self.refresh)
        refresh_button.pack(side='top', pady=10)
        self.news_frame = tk.Frame(self.center_frame, bg='#FFFFFF', bd=2, padx=10)
        self.news_frame.pack(side='top', pady=10)

    def create_news(self):
        for data in self.data[:5]:
            text = f"{data['tag']} - {data['date']}\n{data['headline']}"
            label = tk.Label(self.news_frame, text=text, justify='left', height=4, wraplength=500)
            label.pack(side='top', anchor='w')
            self.news.append(label)

    def refresh(self):
        for entry in self.news:
            entry.destroy()
        self.news.clear()
        self.data = self.parser.work()
        self.create_news()

root = tk.Tk()
app = Application(root=root)
app.mainloop()