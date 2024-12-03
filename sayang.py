import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import pygame

def animate(canvas, text, dx):
    canvas.move(text, dx, 0)
    if canvas.coords(text)[0] > canvas.winfo_width():
        canvas.coords(text, -100, canvas.coords(text)[1])
    canvas.after(50, animate, canvas, text, dx)

def play_birthday_music():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("Happy Birthday.mp3")
        pygame.mixer.music.play()
    except pygame.error as e:
        messagebox.showerror("Error", f"Gagal memutar musik: {e}")

def show_special_message():
    messagebox.showinfo("Ucapan Ulang Tahun", "Selamat Ulang Tahun! 🎉\nSemoga penuh kebahagiaan dan kesuksesan! 💖")

def choose_theme_message():
    themes = {"klasik": "Semoga tahun ini penuh kebahagiaan!", "motivasi": "Terus kejar impianmu!", 
              "romantis": "Semoga cinta kita bahagia selamanya!"}
    theme = simpledialog.askstring("Pilih Tema", "Pilih tema ucapan: Klasik, Motivasi, Romantis")
    if theme and theme.lower() in themes:
        messagebox.showinfo(f"Tema: {theme.capitalize()}", themes[theme.lower()])

def show_birthday_image():
    """Menampilkan tiga gambar ulang tahun secara horizontal dengan teks di bawahnya."""
    try:
        image_window = tk.Toplevel(root)
        image_window.title("Gambar Ulang Tahun")

        image_frame = tk.Frame(image_window)
        image_frame.pack(pady=20)

        images = ["love.png", "love1.png", "love2.png"]  
        for image_path in images:
            img = Image.open(image_path)
            img = img.resize((450, 650), Image.Resampling.LANCZOS)  
            img = ImageTk.PhotoImage(img)

            label = tk.Label(image_frame, image=img)
            label.image = img  
            label.pack(side="left", padx=10)  
        label_text = tk.Label(image_window, text="Selamat Ulang Tahun! 🎉", font=("Arial", 30, "bold"), bg="lightblue", fg="darkblue")
        label_text.pack(side="bottom", fill="x", pady=20)

        image_window.geometry("950x350") 
    except FileNotFoundError:
        messagebox.showerror("Error", "Gambar tidak ditemukan.")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


root = tk.Tk()
root.title("Selamat Ulang Tahun!")
root.state('zoomed')

tk.Label(root, text="Selamat Ulang Tahun! 🎉", font=("Arial", 32, "bold"), bg="lightblue", fg="darkblue").pack(pady=20, fill="x")
frame = tk.Frame(root); frame.pack(expand=True)
button_font = ("Arial", 20, "bold")

buttons = [
    ("Dapatkan Ucapan Spesial", "cyan", show_special_message),
    ("Pilih Tema Ucapan", "pink", choose_theme_message),
    ("Lihat Gambar Ulang Tahun", "yellow", show_birthday_image),
    ("Putar Musik Ulang Tahun", "green", play_birthday_music)
]

for text, color, cmd in buttons:
    tk.Button(frame, text=text, font=button_font, bg=color, height=3, command=cmd).pack(pady=10, fill="x", padx=100)

canvas = tk.Canvas(root, height=100, bg="lightgray")
canvas.pack(fill="x", side="bottom")
text = canvas.create_text(-100, 50, text="🎉 Happy Birthday! Semoga hari ini spesial untukmu! 🎂", 
                          font=("Arial", 24, "italic"), fill="purple")
animate(canvas, text, 5)

root.mainloop()
