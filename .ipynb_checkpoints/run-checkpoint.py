# import subprocess
# import tkinter as tk
# from tkinter import ttk

# # Membuat fungsi untuk menjalankan script preprocessing.py dan menampilkan outputnya di GUI
# def run_preprocessing():
#     # Menggunakan modul subprocess untuk menjalankan script preprocessing.py
#     process = subprocess.Popen(["python", "preprocessing.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#     output = stdout.decode("utf-8") + stderr.decode("utf-8")
    
#     # Menampilkan output di dalam tab Preprocessing
#     txt_preprocessing.insert(tk.END, output)

# # Membuat fungsi untuk menjalankan script model.py dan menampilkan outputnya di GUI
# def run_model():
#     # Menggunakan modul subprocess untuk menjalankan script model.py
#     process = subprocess.Popen(["python", "randomforest.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#     output = stdout.decode("utf-8") + stderr.decode("utf-8")
    
#     # Menampilkan output di dalam tab Model
#     txt_model.insert(tk.END, output)
# def run_predict():
#     # Menggunakan modul subprocess untuk menjalankan script model.py
#     process = subprocess.Popen(["python", "deteksi.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = process.communicate()
#     output = stdout.decode("utf-8") + stderr.decode("utf-8")
    
#     # Menampilkan output di dalam tab Model
#     txt_predict.insert(tk.END, output)

# # Membuat GUI dengan Tkinter
# root = tk.Tk()
# root.geometry("600x400")  # Menentukan ukuran jendela
# root.title("Data Processing App")  # Menentukan judul jendela

# # Membuat tema untuk tombol
# style = ttk.Style()
# style.configure("TButton", padding=10, relief="flat", font=("Segoe UI", 12), background="#0078D7", foreground="#FFFFFF")

# # Membuat tombol untuk menjalankan preprocessing.py
# btn_preprocessing = ttk.Button(root, text="Preprocessing", command=run_preprocessing)
# btn_preprocessing.place(x=10, y=10)

# # Membuat tombol untuk menjalankan model.py
# btn_model = ttk.Button(root, text="Model", command=run_model)
# btn_model.place(x=120, y=10)

# # Membuat tombol untuk menjalankan deteksi.py
# btn_predict = ttk.Button(root, text="Predict", command=run_predict)
# btn_predict.place(x=240, y=10)

# # Membuat widget Notebook untuk menampilkan output
# notebook = ttk.Notebook(root, width=580, height=340)
# notebook.place(x=10, y=50)

# # Membuat tab Preprocessing di dalam Notebook
# tab_preprocessing = ttk.Frame(notebook)
# notebook.add(tab_preprocessing, text="Preprocessing")

# # Membuat widget Text di dalam tab Preprocessing
# txt_preprocessing = tk.Text(tab_preprocessing, wrap="word", font=("Segoe UI", 12))
# txt_preprocessing.pack(fill="both", expand=True)

# # Membuat tab Model di dalam Notebook
# tab_model = ttk.Frame(notebook)
# notebook.add(tab_model, text="Model")

# # Membuat widget Text di dalam tab Model
# txt_model = tk.Text(tab_model, wrap="word", font=("Segoe UI", 12))
# txt_model.pack(fill="both", expand=True)

# # ======================================================================

# # Membuat tab Predict di dalam Notebook
# tab_predict = ttk.Frame(notebook)
# notebook.add(tab_predict, text="Predict")

# # Membuat widget Text di dalam tab Predict
# txt_predict = tk.Text(tab_predict, wrap="word", font=("Segoe UI", 12))
# txt_predict.pack(fill="both", expand=True)

# # Menjalankan GUI
# root.mainloop()


import tkinter as tk
from tkinter import ttk
import subprocess

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
root.geometry("600x400")
root.title("Data Processing App")

# Membuat tema untuk tombol
style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", font=("Segoe UI", 12), background="#0078D7", foreground="#FFFFFF")

# Membuat tombol untuk menjalankan preprocessing.py
btn_preprocessing = ttk.Button(root, text="Preprocessing", command=run_preprocessing)
btn_preprocessing.place(x=10, y=10)

# Membuat tombol untuk menjalankan model.py
btn_model = ttk.Button(root, text="Model", command=run_model)
btn_model.place(x=120, y=10)

# Membuat tombol untuk menjalankan deteksi.py
btn_predict = ttk.Button(root, text="Predict", command=run_predict)
btn_predict.place(x=240, y=10)

# Membuat widget Notebook untuk menampilkan output
notebook = ttk.Notebook(root, width=580, height=340)
notebook.place(x=10, y=50)

# Membuat tab Preprocessing di dalam Notebook
tab_preprocessing = ttk.Frame(notebook)
notebook.add(tab_preprocessing, text="Preprocessing")

# Membuat widget Text di dalam tab Preprocessing
txt_preprocessing = tk.Text(tab_preprocessing, wrap="word", font=("Segoe UI", 12))
txt_preprocessing.pack(fill="both", expand=True)

# Membuat tab Model di dalam Notebook
tab_model = ttk.Frame(notebook)
notebook.add(tab_model, text="Model")

# Membuat widget Text di dalam tab Model
txt_model = tk.Text(tab_model, wrap="word", font=("Segoe UI", 12))
txt_model.pack(fill="both", expand=True)

# Membuat tab Predict di dalam Notebook
tab_predict = ttk.Frame(notebook)
notebook.add(tab_predict, text="Predict")

# Membuat widget Text di dalam tab Predict
txt_predict = tk.Text(tab_predict, wrap="word", font=("Segoe UI", 12))
txt_predict.pack(fill="both", expand=True)

# Menjalankan GUI
root.mainloop
