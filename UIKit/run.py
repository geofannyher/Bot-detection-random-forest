import tkinter as tk
from tkinter import ttk
import subprocess
import webbrowser

# Membuat fungsi untuk menjalankan script preprocessing.py dan menampilkan outputnya di GUI
def run_preprocessing():
    process = subprocess.Popen(["python", "preprocessing.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode("utf-8") + stderr.decode("utf-8")
    txt_preprocessing.insert(tk.END, output)

# Membuat fungsi untuk menjalankan script model.py dan menampilkan outputnya di GUI
def run_model():
    process = subprocess.Popen(["python", "randomforest.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode("utf-8") + stderr.decode("utf-8")
    txt_model.insert(tk.END, output)

# Membuat fungsi untuk menjalankan script deteksi.py dan menampilkan outputnya di GUI
def run_predict():
    process = subprocess.Popen(["python", "deteksi.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode("utf-8") + stderr.decode("utf-8")
    txt_predict.insert(tk.END, output)



# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Data Processing App")
root.option_add("*tearOff", False)
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

# Membuat Frame untuk input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Teks copyright
label_copyright = tk.Label(root, text="© 2023 Databot", font=("Arial", 10), fg="gray")
label_copyright.grid(row=12, column=0, padx=10)
# Button preprocessing
button_preprocessing = ttk.Button(widgets_frame, text="Preprocessing", command=run_preprocessing)
button_preprocessing.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

# Button model
button_model = ttk.Button(widgets_frame, text="Model", command=run_model)
button_model.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

# Button predict
button_predict = ttk.Button(widgets_frame, text="Predict", command=run_predict)
button_predict.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

# Notebook
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

# Tab Preprocessing
tab_preprocessing = ttk.Frame(notebook)
notebook.add(tab_preprocessing, text="Preprocessing")

# Text area Preprocessing
txt_preprocessing = tk.Text(tab_preprocessing, wrap="word", font=("Segoe UI", 12))
txt_preprocessing.pack(fill="both", expand=True)

# Tab Model
tab_model = ttk.Frame(notebook)
notebook.add(tab_model, text="Model")
# Text area Model
txt_model = tk.Text(tab_model, wrap="word", font=("Segoe UI", 12))
txt_model.pack(fill="both", expand=True)

# Tab Predict
tab_predict = ttk.Frame(notebook)
notebook.add(tab_predict, text="Predict")

# Text area Predict
txt_predict = tk.Text(tab_predict, wrap="word", font=("Segoe UI", 12))
txt_predict.pack(fill="both", expand=True)

# Menjalankan GUI
root.mainloop()



# Menjalankan GUI
root.mainloop()
