import heapq
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



def exit():
    return exit()


def face_expressions():
    screen = tk.Tk()



    face_classifier = cv2.CascadeClassifier(r'C:\\Users\\hasso\\Desktop\\Hu\\projectB\\ProjectB\\images\\haarcascade_frontalface_default.xml')
    classifier = load_model(r'C:\\Users\\hasso\\Desktop\\Hu\\projectB\\ProjectB\\images\\Emotion_little_vgg.h5')

    class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

    cap = cv2.VideoCapture(0)

    while True:
        # Grab a single frame of video
        ret, frame = cap.read()
        labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            # rect,face,image = face_detector(frame)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                # make a prediction on the ROI, then lookup the class

                preds = classifier.predict(roi)[0]
                label = class_labels[preds.argmax()]
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

    exit_button = tk.Button(screen, text=" Exit", command=exit()).pack

    cap.release()
    tk.mainloop()


with open("steamdata.json",encoding= "utf-8" ) as f:
    data = json.load(f)


def quick_sort(data):
    data = [data]
    length = len(data)
    if length <= 1:

        return data
    else:
        pivot = data.pop()

    items_greater = []
    item_lower = []

    for item in data:
        if item > pivot:

            items_greater.append(item)

        else:
            item_lower.append(item)


    return quick_sort(item_lower) + pivot + quick_sort(items_greater)


def binary_search_recursive(data , target):
    data =  quick_sort(data)
    min = 0
    mid = ((len(data) - 1) + min) // 2
    if len(data) != 0:
        if target == data[mid]:
            return True
        elif target > data[mid]:
            data = data[mid + 1:]
            return binary_search_recursive(data, target)
        elif target <data[mid]:
            data = data[0: mid]
            return binary_search_recursive(data, target)
    return False


def eerste_spel():
    global naam
    naam = data[0]['name']
    return naam





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
    face_button.place(relx=0.8, rely=0.1, relwidth=0.20, relheight=0.20, anchor="n")



    tk.mainloop()


Dashboard()