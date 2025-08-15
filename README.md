markdown
# 🚀 WB0MB - WhatsApp Message Automation Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Warning](https://img.shields.io/badge/%F0%9F%9A%A8-Violates_WhatsApp_TOS-red)

Tools pengiriman pesan otomatis WhatsApp menggunakan Python dan Selenium (Untuk tujuan edukasi semata)

<img src="https://img.icons8.com/color/96/000000/whatsapp.png" width="100" align="right">

## 📌 Daftar Isi
1. [Peringatan Penting](#-peringatan-penting)
2. [Fitur Utama](#-fitur-utama)
3. [Persyaratan Sistem](#-persyaratan-sistem)
4. [Panduan Instalasi](#-panduan-instalasi)
5. [Cara Penggunaan](#-cara-penggunaan)
6. [Troubleshooting](#-troubleshooting)
7. [FAQ](#-faq)
8. [Lisensi](#-lisensi)

## ⚠️ Peringatan Penting
- **Dilarang keras** untuk spam/penipuan/aksi ilegal
- WhatsApp dapat **memblokir permanen** akun Anda
- Gunakan hanya di lingkungan testing dengan nomor dummy
- Developer **tidak bertanggung jawab** atas penyalahgunaan

## ✨ Fitur Utama
✔️ Pengiriman pesan berulang otomatis  
✔️ Mendukung grup dan kontak pribadi  
✔️ Antarmuka CLI interaktif dengan warna  
✔️ Sistem login via QR Code  
✔️ Cross-platform support  
✔️ Manajemen WebDriver otomatis  

## 💻 Persyaratan Sistem
| Komponen | Minimal |
|----------|---------|
| OS | Windows 10 / Ubuntu 18.04 / macOS 10.15 |
| Python | 3.8+ |
| RAM | 2GB |
| Chrome | Versi terbaru |
| Storage | 500MB |

## 📥 Panduan Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/username/WB0MB.git && cd WB0MB
```
### 2. Setup Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Jalankan Aplikasi
```bash
python wbomb.py
```
🛠️ Cara Penggunaan
Scan QR Code WhatsApp Web yang muncul

Pilih menu:

text
1. Start bombing
2. Support original creator 
3. Exit/Quit
Masukkan:

Nama kontak/grup (case sensitive)

Pesan yang ingin dikirim

Jumlah repetisi (angka)

🐛 Troubleshooting
Masalah	Solusi
ChromeDriver error	Update Chrome ke versi terbaru
Element not found	Pastikan nama kontak tepat sama
QR code tidak muncul	Cek koneksi internet/firewall
Module not found	Jalankan pip install -r requirements.txt
❓ FAQ
Q: Apakah aman menggunakan tools ini?
A: Tidak sepenuhnya aman, risiko pemblokiran akun sangat tinggi.

Q: Bisakah digunakan tanpa browser GUI?
A: Bisa dengan menambahkan headless mode di chrome_options:

python
options.add_argument('--headless')
Q: Bagaimana cara berhenti saat proses berjalan?
A: Tekan Ctrl+C di terminal atau tutup paksa browser.

📜 Lisensi
MIT License - Lihat LICENSE untuk detail lengkap

💡 Catatan Developer:
Tools ini dibuat semata untuk tujuan pembelajaran teknologi automasi. Pertimbangkan untuk menggunakan WhatsApp Business API untuk solusi resmi.

<div align="center"> <sub>Dibuat dengan ❤️ oleh [Nama Anda] | © 2023</sub> </div> ```
Fitur README ini:
Desain modern dengan emoji dan badges

Responsif untuk tampilan GitHub

Tabel troubleshooting untuk masalah umum

Panduan step-by-step yang jelas

Penekanan etika berulang

Struktur terorganisir dengan daftar isi

Anda bisa:

Tambahkan screenshot di folder /assets

Buat GIF demo menggunakan ScreenToGif

Tambahkan bagian "Berkontribusi" jika proyek open source
