import json
import tkinter as tk
import tkinter.messagebox
from tkinter import font
from tkinter import END
import random
from TwitterAPI import TwitterAPI
import tweepy
import pygame
import datetime








consumer_key = "TC8emZYxOTWeK1mDpYe1fCzTf"
consumer_secret = "WaIQc3VRomuTCclgJj9mnFjbdjg3aoqWeXjFKT9hDmc4wB0PoO"
access_token_key = "1306177869916274688-GwMA12l25qRU8edvSYk6e15xoJ7Azl"
access_token_secret = "n5mr3l7A81SHSJ9u5gM0ODETRrHVLEodlRA9VI65A6GC7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)


with open("steamdata.json",encoding= "utf-8") as f:
    data = json.load(f)
    for game in data:
        del game['developer'],game['publisher'],game['platforms'],game['required_age'],game['categories'], game['steamspy_tags'] ,game['achievements'],game['owners']

with open("newsteamdata.jason","w") as f:
    json.dump(data,f , indent=10)



def eerste_spel():
    global naam
    naam = data[0]['name']
    return naam


def get_tweets(api,username):

    page = 1
    deadend = False
    tweetlist = []
    new_tweets = api.user_timeline(username, page=page)
    for tweet in new_tweets:
        if (datetime.datetime.now() - tweet.created_at).days < 14:
            text = tweet.text
            tweetlist.append(text)
            page = page + 1

    aantaltweets = len(tweetlist)
    x = random.randrange(0, aantaltweets)
    twitter_message.config(text=tweetlist[x])
    twitter_message.after(8000, lambda: get_tweets(api, "Steam"))

    return tweetlist



def all_Games():
    for naam in data:
        global names
        names = naam['name']
        return names






HEIGHT = 700
WIDTH = 1200

def back(image_nu):


    global photos_label
    global button_forward
    global button_back

    photos_label.grid_forget()
    photos_label = tk.Label(photos_frame, image=List_images[image_nu-1])
    photos_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    button_forward = tk.Button(photos_label, text=">>",
                               command=lambda: forward(image_nu + 1))
    button_forward.grid(row=5, column=2)
    button_back = tk.Button(photos_label, text="<<", command=lambda :back(image_nu-1))
    button_back.grid(row=5, column=0)



    if image_nu == List_images[0]:
        button_back = tk.Button( state=tk.DISABLED)





def forward(image_nu):
    global photos_label
    global button_forward
    global button_back
    photos_label.grid_forget()
    photos_label =tk.Label(photos_frame,image = List_images[image_nu+1])
    photos_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    button_forward = tk.Button(photos_label, text=">>",
                               command=lambda: forward(image_nu+1))
    button_forward.grid(row=5, column=2)
    button_back = tk.Button(photos_label, text="<<", command= lambda : back(image_nu-1))
    button_back.grid(row=5, column=0)

    if image_nu == 10:
        button_forward = tk.Button( state=tk.DISABLED)



def paly():
    pygame.mixer.init()
    pygame.mixer.music.load("beat.mp3")
    pygame.mixer.music.play(loops=2)



def stop():
    pygame.mixer.music.stop()




def Dashboard():
    dashboard_screen = tk.Tk()



    dashboard_screen.title("Dashboard")
    dashboard_screen.tk.call('wm', 'iconphoto', dashboard_screen._w, tk.PhotoImage(file="1200px-Steam_icon_logo.svg.png"))


    canvas = tk.Canvas(dashboard_screen, height=HEIGHT, width=WIDTH )
    filename = tk.PhotoImage(file="cover.png")
    image = canvas.create_image(0,0,anchor='nw', image=filename)
    canvas.pack()

    eerste_spel()
    all_Games()


    eerste_spel_label = tk.Label(canvas,text = naam,bg = "#9429e7" , bd= 11 , font=("Helvetica",30), fg = '#0e155b')
    eerste_spel_label.place(relx=0.2, rely=0.11, relwidth=0.25, relheight=0.20, anchor="n")


    all_games_label = tk.Label(canvas, bg="#bb1a5e" ,)
    all_games_label.place(relx=0.2, rely=0.6, relwidth=0.35, relheight=0.30, anchor="n")
    scrollbar = tk.Scrollbar(all_games_label,orient="vertical" )
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y )
    mylist = tk.Listbox(all_games_label, yscrollcommand=scrollbar.set)
    for i in data:
        names = i['name']
        mylist.insert(END ,str(names))
    mylist.pack(side=tk.BOTTOM, fill=tk.BOTH)
    scrollbar.config(command=mylist.yview)




    twittrframe = tk.Frame(canvas  )
    twittrframe.place(relx=0.8, rely=0.2, relwidth=0.20, relheight=0.20, anchor="n")
    global twitter_message

    twitter_message = tk.Message(twittrframe,bg = "#d21c59", font=("Helvetica", 10),fg = "#0e155b")
    twitter_message.place(relx=0, rely=0, relwidth=1, relheight=1)
    global photos_frame


    photos_frame = tk.Frame(canvas)
    photos_frame.place(relx=0.69, rely=0.5, relwidth=0.35, relheight=0.30, anchor="n")



    image1 = tk.PhotoImage(file="header(0).png")
    image2 = tk.PhotoImage(file="header (1).png")

    image3 = tk.PhotoImage(file="header (2).png")

    image4 = tk.PhotoImage(file="header (3).png")

    image5 = tk.PhotoImage(file="header (4).png")

    image6 = tk.PhotoImage(file="header (5).png")

    image7 = tk.PhotoImage(file="header (6).png")

    image8 = tk.PhotoImage(file="header (7).png")

    image9 = tk.PhotoImage(file="header (8).png")

    image10 = tk.PhotoImage(file="header (9).png")

    image11 = tk.PhotoImage(file="header(10).png")

    image12 = tk.PhotoImage(file="header(11).png")
    global List_images

    List_images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12]
    global photos_label

    photos_label = tk.Label(photos_frame, image = image1)
    photos_label.place(relx=0, rely=0, relwidth=1, relheight=1)


    button_forward = tk.Button(photos_frame, text=">>",
                            command=lambda: forward(1))
    button_back = tk.Button(photos_frame, text="<<",
                         command=lambda: back())
    button_back.grid(row=5, column=0)
    button_forward.grid(row=5, column=2)


#________________________________________________________________________________________________________________________
    music_background = tk.PhotoImage(file = "music.png")
    music_label = tk.Label(canvas, bg = "#353770" ,image = music_background )
    music_label.place(relx= 0.52, rely=0.15 , relwidth = 0.15 , relheight = 0.20 ,anchor = "n" )
    play_button = tk.Button(music_label,text = "Play", command= lambda :paly()).pack(padx = 1 ,pady = 10)
    stop_button = tk.Button(music_label, text = "Stop", command= lambda :stop()).pack(pady = 20)

    get_tweets(api, "Steam")


    tk.mainloop()



Dashboard()
