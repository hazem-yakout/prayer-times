import requests
import tkinter as tk
from tkinter import ttk, messagebox
def prayer_times(city,country):
      url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}Emirates&method=2"
      try:
          response = requests.get(url)
          info = response.json()
          if "data" in info:
               timings = info["data"]["timings"]
               return timings
          else:
               return None
      except Exception as e:
             return f"unexpected error occured {e}"
def gui_prayer_times():
      city= city_entry.get()
      country= country_entry.get()
      if city and country:
           prayer_timings = prayer_times(city,country) 
           for name, time in prayer_timings.items():
               result.insert(tk.END, f"{name}:{time}")
      else:
          messagebox.showerror("Error","unable to fetch prayer times, please enter correct city and country names")
   


app = tk.Tk()
app.title("Prayer Times By Hazem Yakout")
frame = ttk.Frame(app, padding="20")
frame.grid(row=0, column=0)
city_label = ttk.Label(frame, text="city:")
city_label.grid(row=0, column=0)
city_entry= ttk.Entry(frame, width=20)
city_entry.grid(row=0, column=1, pady=5)
country_label = ttk.Label(frame, text="country:")
country_label.grid(row=1, column=0)
country_entry= ttk.Entry(frame, width="20")
country_entry.grid(row=1, column=1)
button= ttk.Button(frame, text="Get Prayer Times",command=gui_prayer_times)
button.grid(row=2, column=0, columnspan=2, pady=10)
result= tk.Listbox(frame, height=11, width=30)
result.grid(row=3, column=0,columnspan=2, pady=5 )
app.mainloop()