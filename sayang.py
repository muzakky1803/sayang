import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="Selamat Ulang Tahun!",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Header
st.markdown("<h1 style='text-align: center; color: darkblue;'>🎉 Selamat Ulang Tahun! 🎂</h1>", unsafe_allow_html=True)

# Fungsi
def play_birthday_music():
    """Memutar musik ulang tahun."""
    try:
        st.audio("Happy Birthday.mp3")
    except FileNotFoundError:
        st.error("Musik tidak ditemukan.")

def show_special_message():
    """Menampilkan pesan spesial."""
    st.success("🎉 Selamat Ulang Tahun! Semoga penuh kebahagiaan dan kesuksesan! 💖")

def choose_theme_message():
    """Memilih tema ucapan."""
    themes = {
        "Klasik": "Semoga tahun ini penuh kebahagiaan!",
        "Motivasi": "Terus kejar impianmu!",
        "Romantis": "Semoga cinta kita bahagia selamanya!",
    }
    theme = st.selectbox("Pilih Tema Ucapan:", list(themes.keys()))
    if theme:
        st.info(themes[theme])

def show_birthday_images():
    """Menampilkan gambar ulang tahun secara horizontal."""
    st.markdown("<h3 style='text-align: center;'>🎈 Gambar Ulang Tahun 🎈</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    try:
        with col1:
            img1 = Image.open("love.png").resize((300, 400))
            st.image(img1, use_column_width="auto")
        with col2:
            img2 = Image.open("love1.png").resize((300, 400))
            st.image(img2, use_column_width="auto")
        with col3:
            img3 = Image.open("love2.png").resize((300, 400))
            st.image(img3, use_column_width="auto")
        st.markdown("<p style='text-align: center; font-size: 20px;'><b>Selamat Ulang Tahun! 🎉</b></p>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Salah satu gambar tidak ditemukan.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

# Layout tombol
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Ucapan Spesial"):
        show_special_message()

with col2:
    if st.button("Pilih Tema Ucapan"):
        choose_theme_message()

with col3:
    if st.button("Lihat Gambar"):
        show_birthday_images()

with col4:
    if st.button("Putar Musik"):
        play_birthday_music()
