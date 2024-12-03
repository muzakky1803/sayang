import streamlit as st
import random
from PIL import Image
import time

# Fungsi untuk menambahkan musik ulang tahun menggunakan HTML5 audio tag
def play_birthday_music():
    # Menggunakan st.audio untuk memutar musik
    st.audio("Happy Birthday.mp3", format="audio/mp3", start_time=0)

# Fungsi untuk menampilkan ucapan selamat ulang tahun dengan animasi
def show_special_message():
    st.markdown(
        """
        <div style="background-color: #f9a825; padding: 20px; border-radius: 15px; text-align: center; animation: fadeIn 2s;">
            <h2 style="color: #d32f2f;">🎉 Selamat Ulang Tahun! 🎂</h2>
            <p style="font-size: 18px;">Semoga penuh kebahagiaan, cinta, dan kejutan spesial! 💖</p>
        </div>
        <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Fungsi untuk memilih tema ucapan
def choose_theme_message(theme):
    themes = {
        "Klasik": "Semoga tahun ini penuh kebahagiaan!",
        "Motivasi": "Terus kejar impianmu!",
        "Romantis": "Semoga cinta kita bahagia selamanya!"
    }
    if theme:
        st.markdown(
            f"""
            <div style="background-color: #dcedc8; padding: 20px; border-radius: 15px; text-align: center; animation: slideIn 2s;">
                <p style="font-size: 18px; color: #388e3c;">{themes[theme]}</p>
            </div>
            <style>
                @keyframes slideIn {{
                    from {{ transform: translateX(-100%); }}
                    to {{ transform: translateX(0); }}
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )

# Fungsi untuk menampilkan galeri foto ulang tahun dengan efek animasi
def show_birthday_image():
    st.write("## 🎊 Galeri Ulang Tahun")
    images = ["love.png", "love1.png", "love2.png"]
    cols = st.columns(len(images))
    for col, img_path in zip(cols, images):
        try:
            img = Image.open(img_path)
            col.image(img, use_container_width=True)
        except FileNotFoundError:
            col.error(f"Gambar {img_path} tidak ditemukan.")
    
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px; font-size: 18px; color: #ff5722; animation: bounceIn 2s;">
            🎉 Selamat Ulang Tahun! 🎂
        </div>
        <style>
            @keyframes bounceIn {{
                0% {{ transform: scale(0); }}
                50% {{ transform: scale(1.05); }}
                100% {{ transform: scale(1); }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Fungsi untuk animasi teks yang muncul secara acak
def animate_text():
    messages = ["🎉 Happy Birthday!", "Semoga hari ini spesial untukmu! 🎂", "Selamat Ulang Tahun! 🎈"]
    message = random.choice(messages)
    st.write(f"### <span style='color: #e91e63;'>{message}</span>", unsafe_allow_html=True)
    time.sleep(2)  # Menunggu beberapa detik sebelum animasi berikutnya

# Fungsi untuk permainan ulang tahun (Tebak Angka)
def birthday_game():
    st.write("## 🎉 Permainan Ulang Tahun")
    st.write("Tebak angka antara 1 sampai 10!")
    
    correct_number = random.randint(1, 10)
    user_guess = st.number_input("Masukkan tebakan Anda:", min_value=1, max_value=18, step=1)

    if user_guess:
        if user_guess == correct_number:
            st.success(f"🎉 Selamat! Anda berhasil menebak angka {correct_number} dengan benar!")
        else:
            st.error(f"Ups! Angka yang benar adalah {correct_number}. Coba lagi!")

# Fungsi untuk kejutan spesial
def surprise():
    surprises = [
        "🎉 Surprise! Anda mendapatkan hadiah spesial: Paket liburan!",
        "🎁 Surprise! Anda mendapatkan voucher belanja senilai $100!",
        "🎊 Surprise! Anda mendapatkan tiket konser idola Anda!"
    ]
    st.markdown(
        f"""
        <div style="background-color: #e1bee7; padding: 20px; border-radius: 15px; text-align: center; animation: zoomIn 2s;">
            <h2>{random.choice(surprises)}</h2>
        </div>
        <style>
            @keyframes zoomIn {{
                0% {{ transform: scale(0.5); }}
                100% {{ transform: scale(1); }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Fungsi untuk memilih hadiah ulang tahun
def choose_gift():
    gifts = ["Smartphone", "Laptop", "Voucher Belanja", "Paket Liburan"]
    gift = st.selectbox("Pilih Hadiah Ulang Tahun:", gifts)
    if st.button("Tebak Hadiah 🎁"):
        st.write(f"🎉 Anda memilih hadiah: {gift}. Semoga beruntung!")

# Fungsi untuk menampilkan animasi balon
def show_balloon_animation():
    st.markdown(
        """
        <style>
        @keyframes balloonAnimation {
            0% { transform: translateY(100%); opacity: 1; }
            100% { transform: translateY(-200px); opacity: 0; }
        }

        .balloon {
            position: absolute;
            bottom: 0;
            animation: balloonAnimation 5s ease-in infinite;
            opacity: 1;
            font-size: 30px;
        }

        .balloon:nth-child(1) {
            left: 10%;
            animation-duration: 5s;
            animation-delay: 0s;
        }

        .balloon:nth-child(2) {
            left: 30%;
            animation-duration: 5s;
            animation-delay: 1s;
        }

        .balloon:nth-child(3) {
            left: 50%;
            animation-duration: 5s;
            animation-delay: 2s;
        }

        .balloon:nth-child(4) {
            left: 70%;
            animation-duration: 5s;
            animation-delay: 3s;
        }

        .balloon:nth-child(5) {
            left: 90%;
            animation-duration: 5s;
            animation-delay: 4s;
        }
        </style>
        <div class="balloon">🎈</div>
        <div class="balloon">🎈</div>
        <div class="balloon">🎈</div>
        <div class="balloon">🎈</div>
        <div class="balloon">🎈</div>
        """,
        unsafe_allow_html=True,
    )

# Streamlit App
st.set_page_config(page_title="Selamat Ulang Tahun", layout="wide")

# Mengatur Background dan Header
st.markdown(
    """
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1506748686212-3b84db4a6d95');
        background-size: cover;
        background-position: center;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header dengan styling
st.markdown(
    """
    <div style="background-color: rgba(0, 188, 212, 0.7); padding: 20px; border-radius: 10px; text-align: center;">
        <h1 style="color: #ffffff; font-family: 'Comic Sans MS', cursive;">🎈 Selamat Ulang Tahun! 🎈</h1>
        <p style="font-size: 20px; color: #e3f2fd;">Semoga hari ini penuh kebahagiaan, cinta, dan kejutan spesial!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Memutar musik saat pertama kali membuka halaman
play_birthday_music()

# Pilihan menu menggunakan selectbox
menu = st.selectbox(
    "Pilih langkah untuk merayakan ulang tahun:",
    ("Mulai Perayaan Ulang Tahun", "Ucapan Selamat Ulang Tahun", "Tema Ucapan", "Musik Ulang Tahun", "Galeri Ulang Tahun", "Animasi Ulang Tahun", "Permainan Ulang Tahun", "Kejutan Spesial", "Pilih Hadiah")
)

# Menampilkan bagian yang dipilih oleh pengguna
if menu == "Mulai Perayaan Ulang Tahun":
    show_balloon_animation()
    st.write("### Ucapan Selamat Ulang Tahun")
    show_special_message()

elif menu == "Ucapan Selamat Ulang Tahun":
    show_balloon_animation()
    st.write("### Langkah 1: Ucapan Selamat Ulang Tahun")
    show_special_message()

elif menu == "Tema Ucapan":
    show_balloon_animation()
    st.write("### Langkah 2: Pilih Tema Ucapan")
    theme = st.selectbox("Pilih Tema Ucapan", ["Klasik", "Motivasi", "Romantis"])
    choose_theme_message(theme)

elif menu == "Musik Ulang Tahun":
    show_balloon_animation()
    st.write("### Langkah 3: Musik Ulang Tahun")
    play_birthday_music()

elif menu == "Galeri Ulang Tahun":
    show_balloon_animation()
    st.write("### Langkah 4: Galeri Foto Ulang Tahun")
    show_birthday_image()

elif menu == "Animasi Ulang Tahun":
    show_balloon_animation()
    st.write("### Langkah 5: Animasi Ulang Tahun")
    animate_text()

elif menu == "Permainan Ulang Tahun":
    show_balloon_animation()
    birthday_game()

elif menu == "Kejutan Spesial":
    show_balloon_animation()
    surprise()

elif menu == "Pilih Hadiah":
    show_balloon_animation()
    choose_gift()

# Footer dengan sentuhan grafis
st.markdown(
    """
    <div style="text-align: center; font-size: 14px; margin-top: 20px;">
        <hr style="border: 1px solid #f50057;">
        Dibuat dengan ❤️ untuk merayakan momen spesial Anda!
    </div>
    """,
    unsafe_allow_html=True,
)
