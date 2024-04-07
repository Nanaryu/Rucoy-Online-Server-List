import requests
from json import loads
import tkinter as tk

URL = "https://www.rucoyonline.com/server_list.json"

def _get(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def _format(data: str) -> dict:
    data = loads(data)

    data.pop("apk_version", None)
    data.pop("message", None)
    data.pop("daily_message", None)

    data = data["servers"]

    return sorted(data, key=lambda x: x['name'])

data = _get(URL)
data = _format(data)


window = tk.Tk()
window.title("Server Information")

server_frame = tk.Frame(window, borderwidth=3, relief="solid")
server_frame.pack(padx=3, pady=3)

labels = []

for server in data:
    server_info = f"{server['name']}: {server['characters_online']} characters online"
    chars = int(server['characters_online'])
    if chars <= 50:
        server_label = tk.Label(server_frame, text=server_info, borderwidth=3, relief="solid", fg="#fff", bg="#00f")
    elif 50 < chars <= 100:
        server_label = tk.Label(server_frame, text=server_info, borderwidth=3, relief="solid", fg="#000", bg="#0f0")
    elif 100 < chars <= 150:
        server_label = tk.Label(server_frame, text=server_info, borderwidth=3, relief="solid", fg="#000", bg="#ff0")
    elif 150 < chars:
        server_label = tk.Label(server_frame, text=server_info, borderwidth=3, relief="solid", fg="#000", bg="#f00")
    server_label.config(font=("helvetica", 16))
    server_label.pack(fill="x", padx=3, pady=3)

    labels.append(server_label)

i = 0
def _update() -> None:
    data = _get(URL)
    data = _format(data)

    for i, server in enumerate(data):
        server_info = f"{server['name']}: {server['characters_online']} characters online"
        chars = int(server['characters_online'])
        if chars <= 50:
            labels[i].config(fg="#fff", bg="#00f")
        elif 50 < chars <= 100:
            labels[i].config(fg="#000", bg="#0f0")
        elif 100 < chars <= 150:
            labels[i].config(fg="#000", bg="#ff0")
        elif 150 < chars:
            labels[i].config(fg="#000", bg="#f00")
        labels[i].config(text=server_info)
    window.after(30000, _update)

if __name__ == "__main__":
    _update()
    window.mainloop()