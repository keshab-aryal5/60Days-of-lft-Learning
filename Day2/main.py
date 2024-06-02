import tkinter as tk
from tkinter import messagebox
import json


def load_json():
    json_data = json_entry.get()
    try:
        data = json.loads(json_data)
        result_label.config(text=f"Loaded data: {data}")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid JSON data")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_example():
    example_data = {"name": "keshab", "age": 23, "city": "kathmandu"}
    json_entry.delete(0, tk.END)
    json_entry.insert(0, json.dumps(example_data))
    messagebox.showinfo("Example JSON", "Example JSON data inserted into the entry box")


root = tk.Tk()
root.title("Simple JSON Loader")


json_entry = tk.Entry(root, width=50)
json_entry.pack(pady=10)


load_button = tk.Button(root, text="Load JSON", command=load_json)
load_button.pack(pady=5)


example_button = tk.Button(root, text="Show Example JSON", command=show_example)
example_button.pack(pady=5)


result_label = tk.Label(root, text="Result will be shown here")
result_label.pack(pady=10)


root.mainloop()
