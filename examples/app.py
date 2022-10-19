import requests
import json
from tkinter import BOTH, END, LEFT, Label, Listbox, Tk, Frame

API_URL = "http://localhost:8000"

class Window(Frame):
    def __init__(self, posts, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # List of articles
        listbox = Listbox(self)
        for article in posts:
            listbox.insert(END, article["title"])
        
        # Fetch first article
        article = posts[0]
        data = self.get_item(article["url_hash"])

        # Display fetched article
        pane = Frame(self, padx=10)
        title = Label(pane, text = data["title"])
        title.config(font =("Arial", 25))
        text = Label(pane, text = data["text"], wraplength=800)
        text.config(font =("Arial", 16))

        # Pack items inside window
        listbox.pack(side=LEFT, fill=BOTH)
        title.pack()
        text.pack()
        pane.pack()
    
    def get_item(self, url_hash: str):
        response = requests.get(f"{API_URL}/news/{url_hash}")
        data = json.loads(response.content)
        return {
            "title": data["title"],
            "text": data["text"]
        }


def main():
    response = requests.get(f"{API_URL}/news")
    data = json.loads(response.content)
    posts = data["posts"]

    root = Tk()
    app = Window(posts, master=root)

    root.wm_title("My News App")
    root.geometry("1000x600")
    root.mainloop()

if __name__ == "__main__":
    main()
