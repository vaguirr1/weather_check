#This Program is current weather cheaker. This is based on a youtube video : https://www.youtube.com/watch?v=VaqYFs7Az50

import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk  
import ttkbootstrap as ttk 

def get_weather(city):
    API_KEY = 'API_KEY GOES HERE FROM OPENWeathermap.org' 
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}' 
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
