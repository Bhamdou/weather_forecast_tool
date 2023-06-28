import requests
from tkinter import *
from tkinter import ttk, messagebox
import traceback

def kelvin_to_celsius(temp_k):
    return round(temp_k - 273.15)

def get_weather():
    try:
        api_key = 'your_api_key'  # replace 'your_api_key' with your actual API key
        city = city_name.get()

        # first, get the weather data of the city
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        weather_data = requests.get(weather_url).json()

        if weather_data["cod"] != "404":
            # get and display current weather data
            current_temp = kelvin_to_celsius(weather_data['main']['temp'])
            current_pressure = weather_data['main']['pressure']
            current_humidity = weather_data['main']['humidity']
            current_weather = weather_data['weather'][0]['description']

            results_text.delete(1.0, END)
            results_text.insert(END, f"Current weather in {city}:\n"
                                  f"Temperature: {current_temp}°C\n"
                                  f"Atmospheric Pressure: {current_pressure}hPa\n"
                                  f"Humidity: {current_humidity}%\n"
                                  f"Weather Description: {current_weather}\n\n")

        else:
            messagebox.showerror("Error", "City not found")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"API request failed: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}\n{traceback.format_exc()}")

root = Tk()
root.geometry('600x600')
root.title("Advanced Weather Forecast Tool")

style = ttk.Style(root)
style.theme_use("clam")
style.configure('.', font=('Helvetica', 12))

Label(root, text="Enter city name:", padx=10, pady=10).pack()
city_name = StringVar()
Entry(root, textvariable=city_name).pack(padx=10, pady=10)

Button(root, text="Get Weather", command=get_weather).pack(padx=10, pady=10)

results_text = Text(root, wrap=WORD, padx=10, pady=10, width=60, height=20)
results_text.pack(padx=10, pady=10)

root.mainloop()
