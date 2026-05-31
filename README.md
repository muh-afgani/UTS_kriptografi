# UTS Mata Kuliah Kriptografi

* **Nama:** Muhammad Al Afgani
* **NIM:** 105841116524
* **Bahasa Pemrograman:** Python

---

## Deskripsi Proyek
Program ini dibuat untuk membandingkan kriptografi simetris (Fernet) dan kriptografi asimetris (RSA) berdasarkan 3 parameter utama:
1. **Kecepatan proses enkripsi & dekripsi** (dalam satuan detik).
2. **Ukuran ciphertext** yang dihasilkan dibandingkan dengan plaintext asli.
3. **Tingkat keamanan dasar** dari masing-masing algoritma yang diuji.

Algoritma yang dibandingkan dalam program ini meliputi:
* **Algoritma Simetris:** Fernet
* **Algoritma Asimetris:** RSA

---

## Fitur Utama Program
* **Pengukuran Waktu Eksekusi:** Menghitung secara akurat waktu komputasi yang dibutuhkan untuk proses enkripsi menggunakan library bawaan Python.
* **Analisis Ukuran Data:** Menampilkan perbandingan ukuran ciphertext yang dihasilkan oleh algoritma Fernet dan RSA (dalam satuan bytes).

---

## Hasil Pengujian
Berdasarkan uji coba yang dilakukan pada program, berikut adalah hasil perbandingan antara Fernet dan RSA:

| Algoritma | Ukuran Ciphertext (Bytes) | Waktu Eksekusi (Detik) |
| :--- | :---: | :---: |
| **Fernet** | 100 | ~0.0058 |
| **RSA** | 256 | ~0.0027 |

*Kesimpulan:* Pada pengujian ini, RSA memproses enkripsi lebih cepat daripada Fernet, namun menghasilkan ukuran ciphertext yang jauh lebih besar (256 bytes berbanding 100 bytes).
