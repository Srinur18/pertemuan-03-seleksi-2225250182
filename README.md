# Pertemuan 03 Seleksi Python
Nama: Sri Nur Rahmawati
NIM: 2225250182 
Kelas: 3F  

## Tujuan
Pertemuan ini bertujuan untuk memahami dan menerapkan konsep seleksi dalam pemrograman Python menggunakan `if`, `if-else`, kondisi majemuk, dan `nested if`.

Melalui latihan dan tugas yang diberikan, program dibuat agar dapat mengambil keputusan berdasarkan kondisi tertentu. Selain itu, kegiatan ini bertujuan untuk melatih kemampuan dalam menentukan kondisi yang tepat, menggunakan operator perbandingan dan logika, melakukan pengujian dengan beberapa test case, serta menemukan dan memperbaiki kesalahan logika pada program.

## Cara Menjalankan
1. Buka folder proyek `pertemuan-03-seleksi-2225250013` melalui VS Code.
2. Pastikan Python 3 sudah terpasang dan interpreter Python 3 telah dipilih di VS Code.
3. Buka menu **Terminal** lalu pilih **New Terminal**.
4. Pastikan terminal berada pada folder utama proyek.
5. Jalankan program latihan sesuai dengan file yang ingin diuji.

Untuk menjalankan latihan:
```bash
python3 latihan/01_genap_ganjil.py
python3 latihan/02_bandingkan_dua_bilangan.py
python3 latihan/03_kelulusan_bersyarat.py
python3 latihan/04_jenis_segitiga.py
````

Untuk menjalankan program tugas:
```bash
python3 tugas/analisis_persamaan_kuadrat.py
```

Pada Windows, perintah `python` dapat digunakan jika `python3` tidak tersedia.

## Algoritma Tugas
Program tugas digunakan untuk menganalisis persamaan kuadrat dengan bentuk:
`ax² + bx + c = 0`
Langkah-langkah algoritmanya:
1. Masukkan nilai koefisien `a`, `b`, dan `c`.
2. Periksa apakah nilai `a` sama dengan 0.
3. Jika `a = 0`, program menampilkan bahwa input bukan merupakan persamaan kuadrat.
4. Jika `a ≠ 0`, hitung diskriminan dengan rumus:

   `D = b² - 4ac`
5. Periksa nilai diskriminan.
6. Jika `D > 0`, persamaan memiliki dua akar real yang berbeda dan program menghitung nilai `x1` dan `x2`.
7. Jika `D = 0`, persamaan memiliki satu akar real kembar dan program menghitung nilai `x`.
8. Jika `D < 0`, persamaan tidak memiliki akar real.
9. Tampilkan hasil analisis sesuai dengan kondisi yang diperoleh.

## Hasil Pengujian
| No. | Input                | Keluaran yang Diharapkan            | Keluaran Aktual                     | Status   |
| --- | -------------------- | ----------------------------------- | ----------------------------------- | -------- |
| 1   | a = 1, b = -5, c = 6 | Dua akar real: x1 = 3.00, x2 = 2.00 | Dua akar real: x1 = 3.00, x2 = 2.00 | Berhasil |
| 2   | a = 1, b = 2, c = 1  | Akar real kembar: x = -1.00         | Akar real kembar: x = -1.00         | Berhasil |
| 3   | a = 1, b = 0, c = 1  | Tidak ada akar real                 | Tidak ada akar real                 | Berhasil |
| 4   | a = 0, b = 2, c = 3  | Bukan persamaan kuadrat             | Bukan persamaan kuadrat             | Berhasil |

## Refleksi
Kesalahan logika yang ditemukan adalah ketika kondisi `a = 0` tidak diperiksa terlebih dahulu sebelum menghitung diskriminan. Jika kondisi tersebut tidak diperiksa, program dapat tetap melakukan perhitungan seolah-olah input merupakan persamaan kuadrat, padahal persamaan dengan `a = 0` bukan persamaan kuadrat.

Kesalahan tersebut diperbaiki dengan menambahkan kondisi `if a == 0` sebelum proses perhitungan diskriminan. Dengan demikian, program dapat membedakan input yang merupakan persamaan kuadrat dan yang bukan persamaan kuadrat dengan benar.

Setelah dilakukan pengujian pada seluruh test case, setiap kondisi dapat menghasilkan keluaran yang sesuai dengan hasil yang diharapkan.

```
