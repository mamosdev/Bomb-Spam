# WB0MB - WhatsApp Message Automation Tool 📱💣

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/Lisensi-MIT-red)
![Peringatan](https://img.shields.io/badge/Peringatan-Melanggar_TOS_WhatsApp-orange)

Tools otomatisasi pengiriman pesan WhatsApp menggunakan Selenium WebDriver (Hanya untuk tujuan edukasi)

## 📝 Daftar Isi
- [Peringatan Penting](#⚠️-peringatan-penting)
- [Fitur](#✨-fitur)
- [Persyaratan Sistem](#🔧-persyaratan-sistem)
- [Panduan Instalasi](#📥-panduan-instalasi)
- [Cara Penggunaan](#🛠️-cara-penggunaan)
- [FAQ](#❓-faq)
- [Lisensi](#📜-lisensi)

## ⚠️ Peringatan Penting
- **Dilarang digunakan untuk spam/penipuan** - Tools ini hanya untuk pembelajaran pemrograman
- **Risiko pemblokiran akun** - WhatsApp dapat menghentikan akun yang menggunakan automasi
- **Gunakan nomor dummy** - Jangan pakai nomor utama Anda
- **Tanggung jawab pengguna** - Developer tidak bertanggung jawab atas penyalahgunaan

## ✨ Fitur
✔️ Pengiriman pesan berulang otomatis  
✔️ Mendukung grup dan kontak pribadi  
✔️ Antarmuka Command Line (CLI) interaktif  
✔️ Cross-platform (Windows/Linux/macOS)  
✔️ Sistem login via QR Code WhatsApp Web  

## 🔧 Persyaratan Sistem
- Python 3.8 atau lebih baru
- Google Chrome versi terbaru
- RAM minimal 2GB
- Koneksi internet stabil

## 📥 Panduan Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/username/WB0MB.git
cd WB0MB

2. Buat Virtual Environment (Disarankan)
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Install Dependencies
bash
pip install -r requirements.txt
4. Jalankan Program
bash
python wbomb.py
🛠️ Cara Penggunaan
Scan QR Code saat browser terbuka

Pilih menu:

text
1. Start bombing
2. Support original creator
3. Exit/Quit
Masukkan:

Nama kontak/grup (harus sama persis di WhatsApp)

Pesan yang ingin dikirim

Jumlah pengulangan

❓ FAQ
Q: Kenapa program tidak menemukan kontak?
A: Pastikan:

Nama kontak tepat sama

Kontak sudah terbuka di WhatsApp Web

Tidak ada popup yang menghalangi

Q: Bagaimana cara berhenti saat proses berjalan?
A: Tekan Ctrl+C di terminal untuk menghentikan paksa

Q: Apakah bisa pakai Firefox?
A: Ya, modifikasi kode di setup_driver() untuk menggunakan GeckoDriver

📜 Lisensi
Proyek ini dilisensikan di bawah MIT License

⚠️ CATATAN:
Tools ini dibuat hanya untuk tujuan pembelajaran pemrograman Python dan otomatisasi. Penggunaan untuk spam melanggar kebijakan WhatsApp dan mungkin hukum setempat.

text

### Kelebihan README ini:
1. **Bahasa Indonesia** - Disesuaikan untuk pengguna lokal
2. **Struktur jelas** - Dengan daftar isi dan section terorganisir
3. **Peringatan etika** - Penekanan pada penggunaan bertanggung jawab
4. **Panduan detail** - Langkah instalasi step-by-step
5. **FAQ** - Penyelesaian masalah umum
6. **Badges** - Untuk tampilan profesional

Anda bisa menambahkan:
- Screenshot antarmuka
- Demo GIF/video
- Kontributor guidelines
- Changelog (jika akan dikembangkan lebih lanjut)
