"""
This program is based on a YouTube video: https://www.youtube.com/watch?v=VaqYFs7Az50

"""

import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk  
import ttkbootstrap as ttk 

def get_weather(city):
    API_KEY = 'a54eab6943ebb74318408c5c30a3ec2d' 
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'  
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
    
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature_kelvin = weather['main']['temp']
    temperature_fahrenheit = (temperature_kelvin - 273.15) * 9/5 + 32
    
    description = weather['weather'][0]['description'].title()
    city = weather['name']
    country = weather['sys']['country']
    pressure = weather['main']['pressure']  
    precipitation = weather.get('rain', {}).get('1h', 0)

    lat = weather['coord']['lat']  
    lon = weather['coord']['lon']  
    uv_url = f'https://api.openweathermap.org/data/2.5/uvi?lat={lat}&lon={lon}&appid={API_KEY}'  
    uv_res = requests.get(uv_url)  
    uv_index = uv_res.json().get('value', 'N/A')  

    # This gets the icon from the Url
    icon_url = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'  
    return (icon_url, temperature_fahrenheit, description, city, country, pressure, precipitation, uv_index)

# This function will search the city's weather
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    
    icon_url, temperature, description, city, country, pressure, precipitation, uv_index = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw) 
    resized_image = image.resize((200, 200), Image.LANCZOS)
    icon = ImageTk.PhotoImage(resized_image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°F")  
    description_label.configure(text=f"Description: {description}")
    pressure_label.configure(text=f"Pressure: {pressure} hPa")  
    precipitation_label.configure(text=f"Precipitation: {precipitation} mm")  
    uv_label.configure(text=f"UV Index: {uv_index}")  
    
#This will update the background color based on the weather category
    if 'rain' "thunderstrom" or "cloud" in description.lower():
        root.configure(bg='darkgray')  
    elif 'clear' in description.lower():
        root.configure(bg='skyblue')  
    elif 'mist' in description.lower():
        root.configure(bg='lightgray')  
    elif 'snow' in description.lower():
        root.configure(bg='white')  
    else:
        root.configure(bg='lightgreen')

root = ttk.Window(themename='morph')  
root.title('Weather Check')
root.geometry('700x700')

city_entry = ttk.Entry(root, font=('Helvetica', 18))  
city_entry.pack(pady=10)

search_button = ttk.Button(root, text='Search', command=search, bootstyle='warning')  
search_button.pack(pady=10)

location_label = tk.Label(root, font=('Helvetica', 25)) 
location_label.pack()

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font=('Helvetica', 25))  
temperature_label.pack()

description_label = tk.Label(root, font=('Helvetica', 25)) 
description_label.pack()

pressure_label = tk.Label(root, font=('Helvetica', 25))
pressure_label.pack()

precipitation_label = tk.Label(root, font=('Helvetica', 25))  
precipitation_label.pack()

uv_label = tk.Label(root, font=('Helvetica', 25)) 
uv_label.pack()

root.mainloop()
