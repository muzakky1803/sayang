import streamlit as st
import random
from PIL import Image
import time

def play_birthday_music():
    st.audio("Happy Birthday.mp3", format="audio/mp3", start_time=0)

def show_special_message():
    st.markdown(
        """
        <div style="background-color: #f9a825; padding: 20px; border-radius: 15px; text-align: center; animation: fadeIn 2s;">
            <h2 style="color: #d32f2f;">🎉 SELAMAT ULANG TAHUN SAYANGKU! 🎂</h2>
            <p style="font-size: 18px;">Hari ini adalah hari yang spesial, bukan hanya untukmu, tetapi juga untukku, karena bisa merayakan momen berharga ini bersamamu. Semoga tahun baru dalam hidupmu penuh kebahagiaan, kesuksesan, dan segala hal indah yang kamu impikan.
Kamu adalah inspirasiku, dan aku bangga bisa menemanimu. Teruslah mengejar impianmu, karena aku tahu kamu bisa mencapai apa pun yang kamu inginkan. Semoga hari-harimu selalu cerah, seperti senyummu yang selalu menyinari hidupku.
Selamat ulang tahun, cintaku. Aku akan selalu mendukungmu, karena kamu adalah bagian terpenting dalam hidupku. 💖</p>
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

def choose_theme_message(theme):
    themes = {
        "Klasik": "Selamat ulang tahun Sayangku, Semoga hari-harimu dipenuhi dengan kebahagiaan yang tak terhingga. Semoga Tuhan selalu memberikan berkah, kesehatan, dan kebahagiaan dalam setiap langkahmu. Nikmati setiap momen dalam hidupmu dan teruslah bersinar 💖",
        "Motivasi": "Selamat ulang tahun Sayangku, Setiap tahun membawa peluang baru untuk tumbuh dan meraih impian. Jangan pernah takut untuk melangkah lebih jauh dan mengejar apa yang kamu inginkan. Terus berjuang dan percaya pada dirimu, karena dunia ini penuh dengan kemungkinan. Tahun ini adalah tahunmu untuk bersinar lebih terang 💖",
        "Romantis": "Selamat ulang tahun, cintaku! Setiap detik bersamamu adalah anugerah yang tak ternilai. Semoga hari ini seindah hatimu yang penuh dengan kasih dan kehangatan. Aku berjanji akan selalu ada untukmu, mendukungmu, dan mencintaimu dalam setiap langkah hidup kita bersama. Semoga tahun baru dalam hidupmu ini semakin indah dan penuh cinta 💖"
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

def show_birthday_image():
    st.write("## 🎊 GALERI FOTO ULANG TAHUN 🎂")
    
    images = ["love.png", "love1.png", "love2.png", "love3.png", "love4.png", "love5.png"]
    num_cols = 3  
    cols = st.columns(num_cols)
    
    for i, img_path in enumerate(images):
        col = cols[i % num_cols]  
        try:
            img = Image.open(img_path)
            col.image(img, use_container_width=True)  
        except FileNotFoundError:
            col.error(f"Gambar {img_path} tidak ditemukan.")

    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px; font-size: 18px; color: #ff5722; animation: bounceIn 2s;">
            🎉 Selamat Ulang Tahun Sayangku 🎂
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

def animate_text():
    messages = ["🎉 Happy Birthday Sayangku ", "Semoga hari ini spesial untukmu! 🎂", "Selamat Ulang Tahun Sayangku 🎈"]
    message = random.choice(messages)
    st.write(f"### <span style='color: #e91e63;'>{message}</span>", unsafe_allow_html=True)
    time.sleep(2)  

def birthday_game():
    st.write("## 🎉 PERMAINAN TEBAK ANGKA")
    st.write("Tebak angka antara 1 sampai 18!")
    
    correct_number = random.randint(1, 18)
    user_guess = st.number_input("Masukkan tebakan ayang:", min_value=1, max_value=18, step=1)

    if user_guess:
        if user_guess == correct_number:
            st.success(f"🎉 Selamat! Ayang berhasil menebak angka {correct_number} dengan benar!")
        else:
            st.error(f"Ups! Angka yang benar adalah {correct_number}. Coba lagi!")


def surprise():
    surprises = [
        "🎉 Surprise! ayang mendapatkan hadiah spesial: Paket Jalan-Jalan!",
        "🎁 Surprise! ayang mendapatkan voucher Jajan senilai 50!",
        "🎊 Surprise! ayang mendapatkan voucher kulineran kemana saja!",
        "🎊 Surprise! ayang mendapatkan voucher Sesi Belanja!",
        "🎁 Surprise! ayang mendapatkan voucher Nonton!",
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

def choose_gift():
    gifts = ["Paket Gacoan", "Es krim", "Kulineri", "Paket Jalan-Jalan", "Wist yang ayang pengeni"]
    gift = st.selectbox("PILIH HADIAH Ulang Tahun:", gifts)
    if st.button("Tebak Hadiah 🎁"):
        st.write(f"🎉 ayang memilih hadiah: {gift}. Semoga beruntung!")

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
         .balloon:nth-child(6) {
            left: 90%;
            animation-duration: 5s;
            animation-delay: 4s;
        }
         .balloon:nth-child(7) {
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
        <div class="balloon">🎈</div>
        <div class="balloon">🎈</div>
        """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_title="Selamat Ulang Tahun Sayangku", layout="wide")

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

st.markdown(
    """
    <div style="background-color: rgba(0, 188, 212, 0.7); padding: 20px; border-radius: 10px; text-align: center;">
        <h1 style="color: #ffffff; font-family: 'Comic Sans MS', cursive; font-size: 40px;">🎈🎉SELAMAT DATANG DIPETUALANGAN BAHAGIA!🎂🎈</h1>
        <p style="font-size: 25px; color: #e3f2fd;">Semoga hari ini penuh kebahagiaan, cinta, dan Penuh Kejutan ❤️</p>
        <video width="100%" height="auto" controls style="margin-top: 10px; border-radius: 10px;">
            <source src="video_link.mp4" type="video/mp4">
            Browser Anda tidak mendukung pemutar video.
        </video>
    </div>
    """,
    unsafe_allow_html=True,
)


play_birthday_music()

menu = st.selectbox(
    "Pilih setiap langkah untuk merayakan ulang tahun:",
    ("MULAI PETUALANGAN ULANG TAHUN", "UCAPAN SELAMAT ULANG TAHUN", "TEMA UCAPAN", "MUSIK ULANG TAHUN", "GALERI FOTO ULANG TAHUN", "ANIMASI ULANG TAHUN", "PERMAINAN ULANG TAHUN", "KEJUTAN ULANG TAHUN", "PILIH HADIAH")
)

if menu == "Mulai Petualangan Perayaan Ulang Tahun":
    show_balloon_animation()
    st.write("### Selamat Ulang Tahun")
    show_special_message()

elif menu == "UCAPAN SELAMAT ULANG TAHUN":
    show_balloon_animation()
    st.write("### Langkah 1: UCAPAN SELAMAT ULANG TAHUN")
    show_special_message()

elif menu == "TEMA UCAPAN":
    show_balloon_animation()
    st.write("### Langkah 2: PILIH TEMA UCAPAN")
    theme = st.selectbox("PILIH TEMA UCAPAN", ["Klasik", "Motivasi", "Romantis"])
    choose_theme_message(theme)

elif menu == "MUSIK ULANG TAHUN":
    show_balloon_animation()
    st.write("### Langkah 3: MUSIK ULANG TAHUN")
    play_birthday_music()

elif menu == "GALERI FOTO ULANG TAHUN":
    show_balloon_animation()
    st.write("### Langkah 4: GALERI FOTO ULANG TAHUN")
    show_birthday_image()

elif menu == "ANIMASI ULANG TAHUN":
    show_balloon_animation()
    st.write("### Langkah 5: ANIMASI ULANG TAHUN")
    animate_text()
    
    
    time.sleep(2) 
    st.markdown(
        """
        <div style="background-color: #ffeb3b; padding: 20px; border-radius: 15px; text-align: center; animation: surpriseEffect 3s;">
            <h2 style="color: #e91e63;">🎉 KEJUTAN SPESIAL UNTUKMU! 🎁</h2>
            <p style="font-size: 18px; color: #388e3c;">Tunggu kejutan berikutnya! Kamu sangat berharga dan aku akan selalu membuat hari-harimu penuh kebahagiaan! 💖</p>
        </div>
        <style>
            @keyframes surpriseEffect {
                0% { transform: scale(0.5); opacity: 0; }
                100% { transform: scale(1); opacity: 1; }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


elif menu == "PERMAINAN ULANG TAHUN":
    show_balloon_animation()
    birthday_game()

elif menu == "KEJUTAN ULANG TAHUN":
    show_balloon_animation()
    surprise()

elif menu == "PILIH HADIAH":
    show_balloon_animation()
    choose_gift()


st.markdown(
    """
    <div style="text-align: center; font-size: 14px; margin-top: 20px;">
        <hr style="border: 1px solid #f50057;">
        Dibuat dengan sepenuh ❤️ untuk merayakan momen spesial ayang!
    </div>
    """,
    unsafe_allow_html=True,
)
