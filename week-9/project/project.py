from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import customtkinter
import json
import requests

location_label = object
image = object
temperature = object
weather = object
api = "524b382968907ae30c822c0cc869ac26"

def gui():
    frame = Tk()
    frame.title("Weather app")
    frame.iconbitmap("icons\weather_icon.ico")

    # get the screen dimentions of a laptop
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()

    # centering the window
    center_width = int(screen_width/2 - 500/2)  # 500 is a frame dimentions
    center_height = int(screen_height/2 - 500/2)  # 500 is frame dimentions

    frame.geometry(f"500x500+{center_width}+{center_height}")
    frame.resizable(False, False)
    frame.attributes("-alpha", 0.94)  # making transparent for 94 percents

    frame.configure(background="#fffbd5")

    city_input = StringVar()
    input = customtkinter.CTkEntry(frame, textvariable=city_input, width=360)
    input.place(relx=0.5, rely=0.2, anchor=CENTER)
    input.focus_set()
    input.pack()

    search_button = customtkinter.CTkButton(master=frame, text="Search", width=260, command=lambda: search(city_input))
    search_button.pack()

    # labels
    global location_label
    location_label = Label(frame, text='', font=('bold', 20))
    location_label.config(background="#fffbd5")
    location_label.pack()

    global image
    canvas = Canvas(frame, width=100, height=100)
    canvas.config(background="#fffbd5")
    canvas.pack()
    image = PhotoImage(file="")
    canvas.create_image(50, 50, anchor=CENTER, image=image)

    global temperature
    temperature = Label(frame, text='')
    temperature.config(font=14, background="#fffbd5")
    temperature.pack()

    global weather
    weather = Label(frame, text='')
    weather.config(font=14, background="#fffbd5")
    weather.pack()

    # Execute Tkinter
    frame.mainloop()

def get_coordinates(city: str)-> None:
    url = "http://api.openweathermap.org/geo/1.0/direct?q={}&limit={}&appid={}"

    request = requests.get(url.format(city, 1, api))
    if request:
        json = request.json()
        # print(json[0]["lat"], json[0]["lon"])
        # print(get_weather(json[0]["lat"], json[0]["lon"]))
        return get_weather(json[0]["lat"], json[0]["lon"])

def get_weather(lat: str, lon: str)-> tuple:
    get_city_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}"

    result = requests.get(get_city_url.format(lat, lon, api))
    if result:
        json = result.json()
        city = json["name"]
        weather = json["weather"][0]["main"]
        icon = json["weather"][0]["icon"]
        temperature_kelvin = json["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9 / 5 + 32
        country = json["sys"]["country"]

        return  (city, weather, icon, temperature_celsius, temperature_fahrenheit, country)

def search(city_input):
    city = city_input.get()
    weather_tuple = get_coordinates(city)
    if weather_tuple:
        location_label['text'] = "{}, {}".format(weather_tuple[0], weather_tuple[5])
        image["file"] = "icons\{}.png".format(weather_tuple[2])
        temperature["text"] = "{}°C, {}°F".format(round(float(weather_tuple[3]), 2), round(float(weather_tuple[4])), 2)
        weather["text"] = weather_tuple[1]
    else:
        messagebox.showerror(title="Error", message=f"City {city} is not found")

def main():
    gui()

if __name__ == "__main__":
    main()
