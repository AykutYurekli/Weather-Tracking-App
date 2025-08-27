import requests
import tkinter as tk

window = tk.Tk()
window.title("Weather Tracking")
window.minsize(450, 350)

FONT = ("Arial", 10)

label1 = tk.Label(window, text="Şehrinizi Girin")
label1.config(font=("Calibri", 15, "bold"))
label1.pack(pady=(10))



weather_image_label = tk.Label(window)
weather_image_label.place(x=300, y=100)


city_entry = tk.Entry(window, font=(FONT))
city_entry.pack(pady=5)



weather_image = None

def click_button():
    global weather_image
    city = city_entry.get()
    API_KEY = "36cf9743c1575137308f1787632d2628"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
    r = requests.get(url)
    data = r.json()


    if data.get("cod") != 200:
        result_label.config(text="Şehir bulunamadı!")
        return

    sicaklik = data["main"]["temp"]
    hissedilen = data["main"]["feels_like"]
    durum = data["weather"][0]["description"]
    nem = data["main"]["humidity"]

    result_label.config(text=f"Sıcaklık: {sicaklik}°C\nHissedilen: {hissedilen}°C\nDurum: {durum}\nNem: %{nem}")


    if "açık" in durum.lower():
        image = "weather-tracking-sunny.png"
    elif "bulut" in durum.lower():
        image = "weather-tracking-cloudy.png"
    elif "yağmur" in durum.lower():
        image = "weather-tracking-rainy.png"
    elif "kapalı" in durum.lower():
        image = "weather-tracking-overcastclouds.png"
    else:
        image = "coming-soon.png"

    weather_image = tk.PhotoImage(file=image).subsample(4, 4)
    weather_image_label.config(image=weather_image)




my_button = tk.Button(window, text="Hava Durumu Nasıl", command=click_button)
my_button.config(font=(FONT),bg="#4CAF50", fg="white", activebackground="#45a049")
my_button.pack(pady=15)

result_label = tk.Label(window, text="", font=("arial", 12))
result_label.pack(pady=10,padx=10)



window.mainloop()

