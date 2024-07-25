"""
This program is based on a YouTube video: https://www.youtube.com/watch?v=VaqYFs7Az50

Link to openweather: https://openweathermap.org/
-Will need an API Key from openweathermap, they are
free ones registering with an exmail. 

"""

import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk  
import ttkbootstrap as ttk 

def get_weather(city):
    API_KEY = 'NEED_ANY_API_KEY_FROM_OPENWEATHERMAP.ORG' 
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


   """ 
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

        """
"""
#This functions searches by the weather condtions, 
and lists all the captial cities that have that weather 
type.

"""
def get_captials_with_weather
    API_KEY = "API_KEY_OPENWEATHER"
    capitals = ['Ankara', 'Athens', 'Baghdad', 'Baku', 'Bamako', 'Bandar Seri Begawan', 'Bangkok', 'Bangui', 'Banjul', 'Basseterre', 'Beijing', 'Beirut', 'Belgrade', 'Belmopan', 'Berlin', 'Bern', 'Bishkek', 'Bissau', 'Bogotá', 'Brasília', 'Bratislava', 'Brazzaville', 'Bridgetown', 'Brussels', 'Bucharest', 'Budapest', 'Buenos Aires', 'Cairo', 'Canberra', 'Caracas', 'Castries', 'Copenhagen', 'Dakar', 'Damascus', 'Dhaka', 'Djibouti', 'Doha', 'Dublin', 'Dushanbe', 'Freetown', 'Gaborone', 'Georgetown', 'Hanoi', 'Harare', 'Havana', 'Helsinki', 'Honiara', 'Islamabad', 'Jakarta', 'Jamestown', 'Juba', 'Kabul', 'Kampala', 'Kathmandu', 'Khartoum', 'Kigali', 'Kingston', 'Kinshasa', 'Kuala Lumpur', 'Kuwait City', 'La Paz', 'Libreville', 'Lilongwe', 'Lima', 'Lisbon', 'Ljubljana', 'Lomé', 'London', 'Luanda', 'Lusaka', 'Madrid', 'Majuro', 'Malabo', 'Malé', 'Managua', 'Manama', 'Manila', 'Maputo', 'Maseru', 'Mbabane', 'Minsk', 'Mogadishu', 'Monaco', 'Monrovia', 'Montevideo', 'Moroni', 'Moscow', 'Muscat', "N'Djamena", 'Nairobi', 'Nassau', 'Naypyidaw', 'New Delhi', 'Niamey', 'Nicosia', 'Nouakchott', "Nukuʻalofa", 'Nur-Sultan', 'Oslo', 'Ottawa', 'Ouagadougou', 'Panama City', 'Paramaribo', 'Paris', 'Phnom Penh', 'Port Louis', 'Port Moresby', 'Port Vila', 'Port-au-Prince', 'Port of Spain', 'Porto-Novo', 'Prague', 'Praia', 'Pretoria', 'Pyongyang', 'Quito', 'Rabat', 'Reykjavik', 'Riga', 'Riyadh', 'Rome', 'Roseau', 'San José', 'San Marino', 'San Salvador', 'Sanaa', 'Santiago', 'Santo Domingo', 'São Tomé', 'Sarajevo', 'Seoul', 'Singapore', 'Skopje', 'Sofia', 'Stockholm', 'Suva', 'Tallinn', 'Tarawa', 'Tashkent', 'Tbilisi', 'Tehran', 'Thimphu', 'Tirana', 'Tokyo', 'Tripoli', 'Tunis', 'Ulaanbaatar', 'Vaduz', 'Valletta', 'Vatican City', 'Victoria', 'Vienna', 'Vientiane', 'Vilnius', 'Warsaw', 'Washington', 'Wellington', 'Windhoek', 'Yamoussoukro', 'Yaoundé', 'Yerevan', 'Zagreb']
    matching_cities = []

    for captial in captials:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={capital}&appid={API_KEY}'
        res = requests.get(url)

        if res.status_code == 200:
            weather = res.json()
            description = weather['weather'][0]['description'].title()
            if weather_type.lower() in description.lower():
                matching_cities.append(capital)

       if matching_cities:
        messagebox.showinfo("Results", f"Cities with {weather_type.title()}: {', '.join(matching_cities)}")
    else:
        messagebox.showinfo("Results", f"No capital cities found with {weather_type.title()}")

def search_weather_type():
    weather_type = weather_type_entry.get()
    get_capitals_with_weather(weather_type)
        


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

weather_type_label = tk.Label(root, text="Search for weather type in capital cities:\n (clouds, thunderstorm, rain, snow, clear, mist)", font=('Helvetica', 18 ))
weather_type_label.pack(pady=10)

weather_type_entry = ttk.Entry(root, font=('Helvetica', 18))  
weather_type_entry.pack(pady=10)

weather_type_button = ttk.Button(root, text='Search Weather Type', command=search_weather_type, bootstyle='warning')  
weather_type_button.pack(pady=10)

root.mainloop()


