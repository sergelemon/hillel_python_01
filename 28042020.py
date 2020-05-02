import requests
import tkinter as tk

def prepare_data(data):
    name = data['name']
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    result = f'Weather in {name} is {weather}\ntemperature is {temp} С.'
    weather_label['text'] = result

def get_weather_data(city):
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url=url, params=params)
    weather = response.json()
    s = prepare_data(weather)
    return s

root = tk.Tk()

main_canvas = tk.Canvas(root, height=700, width=800)
main_canvas.pack()

top_frame = tk.Frame(main_canvas, bg='#80C1FF', bd=20)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

bottom_frame = tk.Frame(main_canvas, bg='#80C1FF', bd=20)
bottom_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

weather_label = tk.Label(bottom_frame, text='')
weather_label.place(relx=0.1, rely=0.1, relwidth=0.8, height=100)

entry = tk.Entry(top_frame, font=40)
entry.place(relx=0.05, relwidth=0.6, relheight=0.8)

button = tk.Button(top_frame, text = 'Get Weather', font=40, command=lambda:get_weather_data(entry.get()))
button.place(relx=0.75, relwidth=0.2, relheight=0.8)

root.mainloop()

# get_weather_data('Boston')

