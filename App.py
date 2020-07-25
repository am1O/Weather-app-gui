import tkinter as tk
from PIL import Image, ImageTk
import requests
def get_weather(city):
    key = 'USE_YOUR_KEY'
    url = 'https://api.weatherbit.io/v2.0/current'
    params = {'key': key, 'city': city}
    response = requests.get(url,params=params)
    weather = response.json()
    label['text'] = str(str(weather['data'][0]['city_name'])+', '+str(weather['data'][0]['country_code']) + '\n' +str(weather['data'][0]['weather']['description']) + '\n' + str(weather['data'][0]['temp']))
    loc = 'D:/FILE/save-here/py/ADV/Tkinter/icons/'+str(weather['data'][0]['weather']['icon'])+'.png'
    iconp = Image.open(loc)
    ico = ImageTk.PhotoImage(iconp)
    print(loc)
    ilab.configure(image=ico)
    ilab.image = ico

root = tk.Tk()
HEIGHT = 600
WIDTH = 600

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

bg_img = tk.PhotoImage(file='landscape.png')
bg_img_label = tk.Label(root,image=bg_img)
bg_img_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='grey',bd=2)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text="Get Weather",font=40,command= lambda: get_weather(entry.get()))
button.place(relx=0.658,relwidth=0.342,relheight=1)

frameB= tk.Frame(root,bg='grey',bd=3)
frameB.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(frameB)
label.pack(side='left')

ilab = tk.Label(frameB)
ilab.pack(side='right')



root.mainloop()
