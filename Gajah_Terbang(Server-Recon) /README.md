#  ===== Gajah Terbang (Attacker Recon) =====

### nc 10.15.42.60 62000

1. Akun apa yang dimiliki oleh penyerang dalam database tersebut, berikan emailnya!
- Format: `user@gmail.com`
- Answer: `kuntoajiisrillll@gmail.com`

2. Apa password yang digunakan oleh penyerang?
- Format: `string`
- Answer: `kissme`

3. Pada tanggal berapa akun penyerang diban?
- Format:  `YYYY-MM-DD` ex. 1945-08-17
- Answer: `2024-06-09`

Setelah mengekpor data kedalam format .txt, kami merapihkannya di excel agar lebih mudah lagi untuk membacanya untuk menjawab pertanyaan". dan ini hasilnya :

![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/Gajah_Terbang(Attacker-Recon)%20/src/1.png)

4. Table apa saja yang dimodifikasi oleh penyerang?
- Format: string dan string
- Answer: users dan banned_users

kami menggunakan terminal untuk mencari table yang dimodifikasi, menggunakan command `strings gajahterbang.pcapng | grep "SELECT` dan hasilnya kami mencoba satu persatu, yang mana kiranya benar.

5. Barang apa saja yang telah dibeli oleh penyerang?
- Format: string dan string
- Answer: rokok dan es krim

6. Berapa total transaksi dari barang yang dibeli oleh penyerang?
- Format: number
- Answer: 24500

kami mencocokan data menggunakan table yang telah dibuat sebelumnya, agar pertanyaan dapat dijawab dengan tepat.

7. Flag
```
JarkomIT{G4jaH_K0k_t3RbaNG_Z5Bzm1k4yBmbZ5vl5wlIVvwvqYntsFz33iFPnNN98610WqlcHvf4VKt5}
```
![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/Gajah_Terbang(Attacker-Recon)%20/src/2.png)

