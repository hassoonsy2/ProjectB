
import json
import tkinter as tk
import tkinter.messagebox
from tkinter import font
from tkinter import END
import pygame
import datetime
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
from matplotlib import pyplot as plt

from matplotlib.ticker import LinearLocator
from matplotlib import cm






def face_expressions():
    face_classifier = cv2.CascadeClassifier(r'.\\images\\haarcascade_frontalface_default.xml')
    classifier = load_model(r'.\\images\\Emotion_little_vgg.h5')

    class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()
        labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)


            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)




                preds = classifier.predict(roi)[0]
                global label
                label = class_labels[preds.argmax()]

                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        cv2.imshow('Emotion Detector', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break



    cap.release()



with open("steamdata.json",encoding= "utf-8" ) as f:
    data = json.load(f)



def partition(data, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if data[i]["name"] <= data[begin]["name"]:
            pivot_idx += 1
            data[i], data[pivot_idx] = data[pivot_idx], data[i]
    data[pivot_idx], data[begin] = data[begin], data[pivot_idx]
    return pivot_idx

def quick_sort_recursion(data,begin,end):
    if begin >= end:
        return
    pivot_idx = partition(data, begin, end)
    quick_sort_recursion(data, begin, pivot_idx - 1)
    quick_sort_recursion(data, pivot_idx + 1, end)

def quick_sort(data, begin=0, end=None):

    if end is None:
        end = len(data) - 1
        return quick_sort_recursion(data, begin, end)

def quick_sort1(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort1(items_lower) + [pivot] + quick_sort1(items_greater)



def eerste_spel():
    global naam
    naam = data[0]['name']
    return naam


def all_Games():
    for naam in data:
        global names
        names = naam['name']
        return names





def mean(lst):
    lst = quick_sort1(lst)
    A = float(len(lst))
    for i in range(len(lst)):
        B =sum(lst)
    C = B / A
    return C



def rnge(lst):

    list = quick_sort1(lst)
    grooste_value = int(max(list))
    klienste_value = int(min(list))
    X = int(grooste_value - klienste_value)
    return X



def median(lst):
    list = quick_sort1(lst)

    if len(list) % 2 == 0:
        mid = list[len(list) // 2]
        mid2 = list[len(list) // 2 - 1]
        median = float(mid + mid2) / 2
        return float(median)
    else:
        median = float(list[len(list) // 2])
        return float(median)




def q1(lst):
    list = quick_sort1(lst)
    max = len(list) // 2
    list = list[:max]
    q = median(list)

    return q


def q3(lst):
    list = quick_sort1(lst)
    max = len(list) // 2

    if len(list) % 2 == 0 :
        list = list[max:]
        q = float(median(list))
        return q

    else:
        list = list[max+1 :]
        q = float(median(list))
        return q



def var(lst):
    list = quick_sort1(lst)
    gemiddelde = float(mean(list))
    n = float(len(list))
    A = [(nummer - gemiddelde) ** 2 for nummer in list]
    B = sum(A) / n
    return float(B)



def std(lst):
    list = quick_sort1(lst)
    variante = var(list)
    sqr_num = float(variante ** 0.5)
    return sqr_num



def freq(lst):

    list = quick_sort1(lst)
    freqs = dict()

    for nummer in list:
        if (nummer in freqs):
            freqs[nummer] += 1
        else:
            freqs[nummer] = 1

    return freqs



def modes(lst):
    modi = []
    list = quick_sort1(lst)
    count = {}
    for nummer in list:
        count[nummer] = count.get(nummer,0) +1
        count[nummer]+=1
    mod = max(count.values())
    for nummer, freq in count.items():
        if freq == mod:
            modi.append(nummer)
    return quick_sort1(lst)


def describ(lst):
    rang = rnge(lst)
    mean1 = mean(lst)
    variantie = var(lst)
    standaard = std(lst)
    freq1 = freq(lst)
    modus = modes(lst)
    gemiddeled = median(lst)
    eerste_kwartal = q1(lst)
    derde_kwartal = q3(lst)
    y = f""" Data Beschrijving : 
    Rang : {rang}  
    Mean : {mean1} 
    Var :  {variantie} 
    Std : {standaard}
    Freq : \n{freq1}\n
    Modes : \n{modus}\n
    Median : {gemiddeled}
    q1 : {eerste_kwartal}
    Q3 : {derde_kwartal}
    """


    return y

def beschrijving_postive():
    t = []

    for x in data:
        y = x["positive_ratings"]
        t.append(y)

    return describ(t[:900])


def beschrijving_price():
    t = []

    for x in data:
        y = x["price"]
        t.append(y)


    return describ(t[:900])

def beschrijving_avr_playtim():
    t = []

    for x in data:
        y = x["average_playtime"]
        t.append(y)

    return describ(t[:900])



def statstiek_price():
    HEIGHT = 480
    WIDTH = 640
    screen = tk.Toplevel()
    screen.title("Steam Statistics")
    screen.tk.call('wm', 'iconphoto', screen._w, tk.PhotoImage(file="1200px-Steam_icon_logo.svg.png"))

    t = []
    for x in data:
        y = x["price"]
        t.append(y)
    r = freq(t[:900])
    y = r.values()
    x = r.keys()
    dev_x = x
    dev_y = y
    plt.plot(dev_x, dev_y)
    plt.title("Prijs digram ")
    plt.xlabel("spel prijs")
    plt.ylabel("prijs Freq")
    plt.savefig('price2.png')
    canvas = tk.Canvas(screen, height=HEIGHT, width=WIDTH)
    filename = tk.PhotoImage(file="price1.png")
    image = canvas.create_image(0, 0, anchor='nw', image=filename)
    canvas.pack()

    screen.mainloop()





def statstiek_postive():
    HEIGHT = 480
    WIDTH = 640
    screen = tk.Toplevel()
    screen.title("Steam Statistics")
    screen.tk.call('wm', 'iconphoto', screen._w, tk.PhotoImage(file="1200px-Steam_icon_logo.svg.png"))
    t = []
    for x in data:
        y = x["positive_ratings"]
        t.append(y)
    x = ["CS-GO", "Dota2", "Team\n Fortress2","PLAYER-\nUNKNOWN'S","Garry's Mod" ]
    per1 = [2644404 ,863507,515879,496184,363721]
    plt.bar(x,per1,color ="purple")
    plt.title("Top 5 Ratings spellen ")

    plt.ylabel("Rating in miljoenen")

    plt.savefig('Top54.png')
    canvas = tk.Canvas(screen, height=HEIGHT, width=WIDTH)
    filename = tk.PhotoImage(file="Top5.png")
    image = canvas.create_image(0, 0, anchor='nw', image=filename)
    canvas.pack()

    screen.mainloop()

def statstiek_avrage():
    HEIGHT = 480
    WIDTH = 640
    screen = tk.Toplevel()
    screen.title("Steam Statistics")
    screen.tk.call('wm', 'iconphoto', screen._w, tk.PhotoImage(file="1200px-Steam_icon_logo.svg.png"))

    labels = 'The Abbey of\n Crime Extensum', 'The Banner\n Saga: Factions', 'The Secret of\n Tremendous \n Corporation ', 'PRICE   '
    sizes = [43, 22, 22, 13]
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title("Top 4 games met lange speeltijd")
    plt.savefig('Top44.png')
    canvas = tk.Canvas(screen, height=HEIGHT, width=WIDTH)
    filename = tk.PhotoImage(file="Top44.png")
    image = canvas.create_image(0, 0, anchor='nw', image=filename)
    canvas.pack()

    screen.mainloop()




HEIGHT = 700
WIDTH = 1200
def do_something(label,text):

    label.configure(text=text)
def exit1():
    return exit()


def statistics():
    top = tk.Toplevel()

    top.title("Steam Statistics")
    top.tk.call('wm', 'iconphoto', top._w, tk.PhotoImage(file="1200px-Steam_icon_logo.svg.png"))

    canvas = tk.Canvas(top, height=HEIGHT, width=WIDTH)
    filename = tk.PhotoImage(file="cover.png")
    image = canvas.create_image(0, 0, anchor='nw', image=filename)
    canvas.pack()


    label = tk.Label(canvas,bd = 5, text = "Welcome in steam - Statistics " , font=("Courier", 10) , bg = "#A2D6EC")
    label.place(relx=0.50, rely=0.10, relwidth=0.90, relheight=0.7,anchor="n")


    button1 = tk.Button(canvas, text = " Top 5 Games",command = lambda :statstiek_postive(), bg = "#B456FF")
    button1.place(relx=0.80, rely=0.83, relwidth=0.10, relheight=0.10, anchor="n")

    button2 = tk.Button(canvas, text=" Games prijzen" , command = lambda : statstiek_price() , bg = "#B456FF")
    button2.place(relx=0.69, rely=0.83, relwidth=0.10, relheight=0.10, anchor="n")

    button3 = tk.Button(canvas, text=" Top 4 Games met lange speltijden" , command = lambda : statstiek_avrage(), bg = "#B456FF")
    button3.place(relx=0.14, rely=0.83, relwidth=0.18, relheight=0.10, anchor="n")

    button4 = tk.Button(canvas, text = "Describ positive ratings" , command = lambda : do_something(label, beschrijving_postive()) ,bg = "#B456FF")
    button4.place(relx=0.55, rely=0.83, relwidth=0.15, relheight=0.10, anchor="n")
    button5 = tk.Button(canvas, text="Describ average_playtime",
                        command=lambda: do_something(label, beschrijving_avr_playtim()), bg = "#B456FF")
    button5.place(relx=0.31, rely=0.83, relwidth=0.15, relheight=0.10, anchor="n")

    button6 = tk.Button(canvas, text="Describ Price",
                       command=lambda: do_something(label, beschrijving_price()), bg = "#B456FF")
    button6.place(relx=0.44, rely=0.83, relwidth=0.10, relheight=0.10, anchor="n")

    button7 = tk.Button(canvas, text = "Exit", command = lambda: exit1(),  bg = "#B456FF")
    button7.place(relx=0.90, rely=0.83, relwidth=0.10, relheight=0.10, anchor="n")




    top.mainloop()

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

    music_background = tk.PhotoImage(file = "music.png")
    music_label = tk.Label(canvas, bg = "#353770" ,image = music_background )
    music_label.place(relx= 0.52, rely=0.15 , relwidth = 0.15 , relheight = 0.20 ,anchor = "n" )
    play_button = tk.Button(music_label,text = "Play", command= lambda :paly()).pack(padx = 1 ,pady = 10)
    stop_button = tk.Button(music_label, text = "Stop", command= lambda :stop()).pack(pady = 20)


    face_button = tk.Button(canvas, text = "Face expressions" ,  command= lambda  :face_expressions())
    face_button.place(relx=0.8, rely=0.1, relwidth=0.10, relheight=0.10, anchor="n")

    Statstiek_button = tk.Button(canvas, text = "Go Statistics", command = lambda : statistics())
    Statstiek_button.place(relx=0.8, rely=0.30, relwidth=0.10, relheight=0.10, anchor="n")




    tk.mainloop()

Dashboard()