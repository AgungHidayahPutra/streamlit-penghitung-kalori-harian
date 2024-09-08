import streamlit as st
import numpy as np

st.title("Aplikasi Penghitung Kalori Harian")

# Input dari user
gender = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
age = st.number_input("Umur", min_value=1, max_value=100, value=25)
weight = st.number_input("Berat Badan (kg)", min_value=1.0, max_value=200.0, value=70.0)
height = st.number_input("Tinggi Badan (cm)", min_value=50.0, max_value=250.0, value=170.0)
activity_level = st.selectbox("Tingkat Aktivitas", ["Tidak Aktif", "Aktivitas Ringan", "Aktivitas Sedang", "Aktivitas Berat", "Sangat Aktif"])

# Fungsi untuk menghitung BMR
def calculate_bmr(gender, weight, height, age):
    if gender == "Pria":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

# Faktor aktivitas
activity_factors = {
    "Tidak Aktif": 1.2,
    "Aktivitas Ringan": 1.375,
    "Aktivitas Sedang": 1.55,
    "Aktivitas Berat": 1.725,
    "Sangat Aktif": 1.9
}

# Tombol untuk menghitung
if st.button("Hitung Kalori Harian"):
    # Validasi input umur, berat, dan tinggi
    valid = True
    if age < 10 or age > 100:
        st.error("Umur harus di antara 10 dan 100 tahun.")
        valid = False
    if weight < 30 or weight > 200:
        st.error("Berat badan harus di antara 30 dan 200 kg.")
        valid = False
    if height < 100 or height > 250:
        st.error("Tinggi badan harus di antara 100 dan 250 cm.")
        valid = False
    
    # Jika input valid, lakukan perhitungan
    if valid:
        bmr = calculate_bmr(gender, weight, height, age)
        calories = bmr * activity_factors[activity_level]
        
        # Tampilkan hasil
        st.subheader("Hasil Perhitungan")
        st.write(f"**BMR** Anda adalah: {bmr:.2f} kalori/hari")
        st.write(f"Kebutuhan kalori harian Anda berdasarkan tingkat aktivitas ({activity_level}) adalah: {calories:.2f} kalori/hari")
