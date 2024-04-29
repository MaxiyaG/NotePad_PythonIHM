import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
from ttkthemes import ThemedTk

ram_file_path = "/dev/shm/text_file.txt"

def create_text_file():
    try:
        with open(ram_file_path, "w"):
            pass
        print(f"Fichier texte créé avec succès dans {ram_file_path}")
    except Exception as e:
        print(f"Erreur lors de la création du fichier texte : {e}")

def create_text_field(root):
    try:
        global text_field
        text_field = tk.Text(root, bg="black", fg="white")
        text_field.pack(fill="both", expand=True, padx=10, pady=10)
        text_field.bind("<KeyRelease>", update_text_in_ram)
        text_field.focus_set()
    except Exception as e:
        print(f"Erreur lors de la création du champ de texte : {e}")

def update_text_in_ram(event):
    try:
        with open(ram_file_path, "w") as file:
            file.write(text_field.get("1.0", tk.END))
        print(f"Texte enregistré dans {ram_file_path}")
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier texte : {e}")

def create_button(root, button_text, command):
    button = ttk.Button(root, text=button_text, command=command)
    button.pack(side="left", anchor="center", pady=10)

def remove_text_in_field():
    try:
        text_field.delete("1.0", tk.END)
        print("Contenu du champ de texte vidé avec succès")
        os.remove(ram_file_path)
    except Exception as e:
        print("Erreur lors de la suppression du contenu du champ de texte")

def est_vide(content):
    return not content.strip()

def sauvegarder():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
        if file_path:
            shutil.copy(ram_file_path, file_path)
            messagebox.showinfo("Sauvegarder", f"Fichier sauvegardé avec succès dans {file_path}")
            remove_text_in_field()
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def ouvrir_fichier():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            if est_vide(content):
                messagebox.showinfo("Fichier vide", "Le fichier ouvert est vide.")
            else:
                text_field.delete("1.0", tk.END)
                text_field.insert(tk.END, content)
                messagebox.showinfo("Fichier ouvert", "Fichier ouvert avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier : {e}")

def main():
    global root
    root = ThemedTk() 
    root.set_theme('radiance') 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.50)
    height = int(screen_height * 0.75)
    root.minsize(width, height)
    root.title("Blocknote")
    root.resizable(False, False)
    messagebox.showinfo("Auteur", "Ce programme a été réalisé par :\n- GUNDUZ Maxime\n- Github : https://github.com/MaxiyaG/\n- Date: Décembre 2023")
    title_label = tk.Label(root, text="Bloc Note", fg="black", font=("Arial", 20))
    title_label.pack(pady=(0, 10))
    create_text_file()
    create_text_field(root)
    create_button(root, "Sauvegarder", sauvegarder)
    create_button(root, "Ouvrir un fichier", ouvrir_fichier)
    root.mainloop()


