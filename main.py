# FSAnalyser-T
# v0.1.0
version = "0.1.0"

import requests
import json
import tkinter as tk
import threading

root = tk.Tk()
root.title(f"FSAnalyser-T {version}")
root.geometry("800x600")

try:
    root.iconbitmap("icon.ico")
except Exception:
    pass

url = "https://github.com/Maxel8/FSAnalyser-T/raw/refs/heads/data/data.json"

data = {}

def load_data():
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Fehler beim Laden:", e)
        return {"einsätze": []}


data = load_data()

label = tk.Label(root, text="FSAnalyser-T", font=("Arial", 20))
label.pack()

tk.Label(root, text="").pack()


loading_label = tk.Label(root, text="", font=("Arial", 12))
loading_label.pack()

def update_ui():
    anzahl_einsätze = len(data.get("einsätze", []))
    anzahl_einsätze_label.config(text=f"Anzahl der Einsätze: {anzahl_einsätze}")
    loading_label.config(text="")

def lookup():
    loading_label.config(text="Lade Daten...")

    def task():
        global data
        data = load_data()
        root.after(0, update_ui)

    threading.Thread(target=task, daemon=True).start()

button = tk.Button(
    root,
    text="Abrufen",
    bg="#343434",
    fg="white",
    font=("Arial", 14, "bold"),
    padx=10,
    pady=5,
    relief="flat",
    activebackground="#000000",
    cursor="hand2",
    command=lookup
)
button.pack(pady=10)

anzahl_einsätze_label = tk.Label(root, text="Anzahl der Einsätze: X", font=("Arial", 15))
anzahl_einsätze_label.pack()

root.mainloop()