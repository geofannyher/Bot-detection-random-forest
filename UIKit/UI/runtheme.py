import tkinter as tk
from tkinter import ttk
import subprocess
import pandas as pd
from tkinter import filedialog
from ttkthemes import ThemedTk

    
# Fungsi untuk menghapus hasil dari tab "View Data" dan tab lainnya
def clear_results():
    txt_preprocessing.delete('1.0', tk.END)
    txt_model.delete('1.0', tk.END)
    txt_predict.delete('1.0', tk.END)

# Fungsi untuk menjalankan script preprocessing.py dan menampilkan outputnya di GUI
def run_preprocessing():
    process = subprocess.Popen(["python", "preprocessing.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode("utf-8") + stderr.decode("utf-8")
    txt_preprocessing.insert(tk.END, output)

# Fungsi untuk menjalankan script randomforest.py dan menampilkan outputnya di GUI
def run_model():
    process = subprocess.Popen(["python", "randomforest.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode("utf-8") + stderr.decode("utf-8")
    txt_model.insert(tk.END, output)

# Fungsi untuk menjalankan script deteksi.py dan menampilkan outputnya di GUI
def run_predict():
    process = subprocess.Popen(["python", "deteksi.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode("utf-8") + stderr.decode("utf-8")
    txt_predict.insert(tk.END, output)

# Fungsi untuk memuat data Pandas ke dalam Treeview
def load_data():
    tree.delete(*tree.get_children())
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

# Fungsi untuk menampilkan data terpilih di tab "View Data"
def show_selected_data(event):
    global selected_data
    selected_item = tree.focus()
    selected_values = tree.item(selected_item)['values']
    txt_view_data.delete('1.0', tk.END)
    txt_view_data.insert(tk.END, str(selected_values))
    selected_data = pd.DataFrame([selected_values], columns=df.columns)

# Fungsi untuk menyimpan data terpilih dalam bentuk CSV
def save_selected_data():
    global selected_data
    if selected_data is not None:
        selected_data.to_csv('selected_data.csv', index=False)
        txt_save_status.config(text="Data terpilih telah disimpan sebagai selected_data.csv.")

# Fungsi untuk mengunggah file melalui antarmuka pengguna (GUI) dan menyimpannya ke dalam pandas DataFrame
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        global df
        df = pd.read_csv(file_path)
        load_data()

# Membaca data dari file CSV (contoh data)
df = pd.read_csv('datatest.csv')
selected_data = None

# Membuat GUI dengan Tkinter
root = ThemedTk(theme="arc")  # Menggunakan tema 'arc'
root.title("Data Analysis App")

style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 10))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

tree = ttk.Treeview(root)
tree["columns"] = tuple(df.columns)
tree["show"] = "headings"
for column in df.columns:
    tree.heading(column, text=column)

# Menambahkan scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Tombol "Unggah File"
button = ttk.Button(root, text="Unggah File", command=browse_file)
button.pack()

# Tombol untuk memuat data dengan gaya 'flat' dan warna latar belakang 'lightgray'
load_button = ttk.Button(root, text="Muat Data", command=load_data, style="TButton")
load_button.pack(pady=10)

# Tombol Preprocessing dengan gaya 'flat' dan warna latar belakang 'lightgray'
preprocessing_button = ttk.Button(root, text="Preprocessing", command=run_preprocessing, style="TButton")
preprocessing_button.pack(pady=10)

# Tombol Model dengan gaya 'flat' dan warna latar belakang 'lightgray'
model_button = ttk.Button(root, text="Model", command=run_model, style="TButton")
model_button.pack(pady=10)

# Tombol Predict dengan gaya 'flat' dan warna latar belakang 'lightgray'
predict_button = ttk.Button(root, text="Predict", command=run_predict, style="TButton")
predict_button.pack(pady=10)

# Menampilkan Treeview
tree.pack()

# Membuat notebook untuk tab dengan gaya 'clam'
notebook = ttk.Notebook(root, style="TNotebook")
notebook.pack(pady=10)

# Tab View Data dengan gaya 'TFrame'
tab_view_data = ttk.Frame(notebook, style="TFrame")
notebook.add(tab_view_data, text="View Data")

# Text area View Data dengan gaya 'TText'
txt_view_data = tk.Text(tab_view_data, wrap="word", font=("Segoe UI", 12), bg="white", fg="black", padx=10, pady=10, width=200, height=20)
txt_view_data.pack(fill="both", expand=True)

# Menambahkan binding saat item dipilih di Treeview
tree.bind("<<TreeviewSelect>>", show_selected_data)

# Tombol Pilih Data dengan gaya 'TButton' dan warna latar belakang 'lightgray'
button_save_data = ttk.Button(tab_view_data, text="Pilih Data", command=save_selected_data, style="TButton")
button_save_data.pack(pady=10)

# Status penyimpanan
txt_save_status = tk.Label(tab_view_data, text="", font=("Segoe UI", 10), fg="green")
txt_save_status.pack()

# Tab Preprocessing dengan gaya 'TFrame'
tab_preprocessing = ttk.Frame(notebook, style="TFrame")
notebook.add(tab_preprocessing, text="Preprocessing")

# Tab Model dengan gaya 'TFrame'
tab_model = ttk.Frame(notebook, style="TFrame")
notebook.add(tab_model, text="Model")

# Tab Predict dengan gaya 'TFrame'
tab_predict = ttk.Frame(notebook, style="TFrame")
notebook.add(tab_predict, text="Predict")

# Tombol Clear pada tab Preprocessing
button_clear_preprocessing = ttk.Button(tab_preprocessing, text="Clear", command=clear_results, style="TButton")
button_clear_preprocessing.pack(pady=10)

# Tombol Clear pada tab Model
button_clear_model = ttk.Button(tab_model, text="Clear", command=clear_results, style="TButton")
button_clear_model.pack(pady=10)

# Tombol Clear
# pada tab Predict
button_clear_predict = ttk.Button(tab_predict, text="Clear", command=clear_results, style="TButton")
button_clear_predict.pack(pady=10)

# Text area Preprocessing dengan gaya 'TText'
txt_preprocessing = tk.Text(tab_preprocessing, wrap="word", font=("Segoe UI", 12), bg="white", fg="black", padx=10, pady=10)
txt_preprocessing.pack(fill="both", expand=True)

# Text area Model dengan gaya 'TText'
txt_model = tk.Text(tab_model, wrap="word", font=("Segoe UI", 12), bg="white", fg="black", padx=10, pady=10)
txt_model.pack(fill="both", expand=True)

# Text area Predict dengan gaya 'TText'
txt_predict = tk.Text(tab_predict, wrap="word", font=("Segoe UI", 12), bg="white", fg="black", padx=10, pady=10)
txt_predict.pack(fill="both", expand=True)

# Menjalankan GUI
root.mainloop()
