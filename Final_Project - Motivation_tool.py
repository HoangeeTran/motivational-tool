"""
Final Project - Motivation Tool

This program includes 7 functions which are 6 helper function and a main function

This program takes emotional status of users as the input and
resposnes the output that are tools help people balance their emotion.

Authors:
    Ho Hoang Khoi Nguyen
    Tran Viet Hoang
    Ton Thi Dieu Ha
    Tran Nguyen Bao Phuong
"""


import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import webbrowser
import csv
import random
import pandas as pd
pd.set_option('display.max_rows', None) 
window = tk.Tk()
    
user_emotion = "hello"
user_response_type = ""
def read_file(emotion, response_type):
    """Function that reads database in csv file."
    Parameter:
    emotion - a string that contains user's emotion
    response_type - a string that contains user's favorite response type.
        database - csv file named "emotion.csv"
    return:
        response - a string that contains a quote or name of an image or url.
    """
    data = pd.read_csv("emotion.csv", usecols = ["Emotion", "Quote", "Image", "Song"], encoding="unicode_escape")
    emotion = "Sad"
    print("user type:", response_type)
    print(emotion)
    for i, j in zip(data["Emotion"], data[response_type]):
        if i == emotion:
            j = j.split(";")
            response = random.choice(j)
    return response

def display_quote_type():
    """
    Shows the quote as a type of response matching user's emotion
    """
    
    frame = tk.Frame(master=window, relief=tk.RAISED, width=100, height=100, bg="red", border=5)
    frame.pack()
    label = tk.Label(master=frame, text=response, bg="white", fg="green")
    label.grid(row=0, column=0, sticky="neuw", padx=12, pady=12)
    
def display_image_type(window):
    """
    Shows the images matching user's emotions
    """

    canvas = Canvas(window, width = 300, height = 300)  
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(response))  
    canvas.create_image(20, 20, anchor=NW, image=img)

def display_song_type(response):
    """
    Plays the video of song to response user's emotions

    Parameter:
        response - a url link leading to Youtube platform and play video
    """
    webbrowser.open(response,new=1)
    Btn = Button(window, text = "Please click on it to recieve your gift!",command=display_song_type)
    Btn.pack()

def feeling(EMOTION):
    """
    Save and print the emotional data of users in a variable through a parameter
    Parameter:
        EMOTION - a string that is one of five types of basic emotions.
    """
    user_emotion = EMOTION
    print(user_emotion)
    
def response_type(RESPONSE_TYPE):
    """
    Checks input as an emotional data and shows on the screen matched responsed from the CSV file.
    
    Parameter:
        RESPONSE_TYPE - a url link or an jpg file or a string taken from the CSV file
    """
    user_response_type= RESPONSE_TYPE
    user_emotion = "Joyful"
    print("user is", user_emotion)
    print(user_response_type)
    response = read_file(user_emotion, user_response_type)
    print(response)
    if RESPONSE_TYPE =="Quote":
        display_quote_type()
    elif RESPONSE_TYPE == "Image":
        im = Image.open(response)
        im.show()
    elif RESPONSE_TYPE == "Song":
        display_song_type(response)

def open_app():
    """
    Open Tkinter window and allow users to interact with the interface.
    Users will choose one of five emotional status by pushing a button.
    And then they will choose one of three favorite response: song, quote, image.
    """
    # Create a new window with the title "Emotional Tool"
    window.title("Emotional Tool")
    frame = tk.Frame(master=window, relief=tk.RAISED, width=100, height=100, bg="red", border=5)
    frame.pack()
    label = tk.Label(master=frame, text="Hi, How do you feel?", bg="white", fg="green")
    label.grid(row=0, column=0, sticky="n", padx=5, pady=5)
    # Create a new frame to contain the Label
    # and buttons widgets  so that users can press on the suitable emotion.
    frm_emo = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    # Pack the frame into the window
    frm_emo.pack()

    labels  = ["if you feel happy, excit, playful, energetic, playful, amused,...,click ", "if you feel hateful, rage, hostile, selfish, furious..., click ", "if you feel worried, nervous, fearful, anxious, insecure, submissive, helpless, confused,... click ", "if you feel bored, sleepy, lonely, depressed, ashamed, guilty, disappointed,...click ", "if you feel content, thoughtful, intimate, loving, trusting,...click "]
    buttons = ["Joyful", "Angry", "Scared", "Sad", "Peaceful"]
    # Loop over the list of field labels
    for idx, text in enumerate(labels):
        # Create a Label widget with the text from the labels list
        label = tk.Label(master=frm_emo, text=text, bg="blue", fg="yellow")
        # Create a button widget
        button = tk.Button(master=frm_emo, text=buttons[idx], bg="white", fg="red", command =lambda i= idx : feeling(buttons[i]))
        # Use the grid geometry fmanager to place the Label and
        # Button widgets in the row whose index is idx
        label.grid(row=idx, column=0, sticky="e", padx=5, pady=5)
        button.grid(row=idx, column=1, padx=5, pady=5)
        frame = tk.Frame(master=window, relief=tk.RAISED, width=100, height=100, bg="red", border=5)
    frame.pack()
    label = tk.Label(master=frame, text="What kind of response do you want?", bg="white", fg="green")
    label.grid(row=0, column=0, sticky="n", padx=5, pady=5)
    frm_response  = tk.Frame(relief=tk.RIDGE, borderwidth=3)
    # Pack the frame into the window
    frm_response.pack()
    res = ["Quote", "Image", "Song"]
    for idx, text in enumerate(res):
        button = tk.Button(master=frm_response, text=res[idx], bg="white", fg="red", command = lambda i= idx : response_type(res[i]))
        button.grid(row=0, column=idx, padx=5, pady=5)
    
    window.mainloop()
open_app()