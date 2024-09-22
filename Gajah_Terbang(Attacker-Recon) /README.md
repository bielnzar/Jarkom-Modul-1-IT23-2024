# ===== Gajah Terbang (Server Recon) =====

### nc 10.15.42.60 61000

1. Apa DBMS yang digunakan pada server tersebut?
- Format: string ex. MonggoDB
- Answer: PostgreSQL

Pada filter kami seleksi menggunakan `frame contains "sql"` dan mendapatkan ada keterangan PostgreSQL sebagai DBMS yg digunakan server

![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/Gajah_Terbang(Server-Recon)%20/src/1.png)

2. Di port berapa DBMS server tersebut berjalan?
- Format: xxxx ex. 443
- Answer: 6969

Pada traffic terdapat banyak port yang mengarah ke `6969` dan ternyata benar itu port DBMS server berjalan

3. OS apa yang digunakan untuk server tersebut?
- Format: string ex. linux
- Answer: Debian

Ada tulisan Debian... yang mengasumsikan, server menggunakan OS Debian dan ternyata benar

![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/Gajah_Terbang(Server-Recon)%20/src/2.png)

4. Apa credentials username DBMS valid yang digunakan?
- Format: string
- Answer: s1gm4

5. Ada berapa banyak users dalam database tersebut?
- Format: number
- Answer: 4

6. Apa email yang digunakan oleh admin?
- Format: email@gmail.com
- Answer: jojohermawan@gmail.com

7. Apa password yang digunakan oleh admin?
- Format: string
- Answer: admin1234

Kami mengekpor hasil dari capture traffic database, dan menjadikannya file .txt agar mudah membacanya ['GajahTerbang.txt'](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/Gajah_Terbang(Server-Recon)%20/src/GajahTerbang.txt)

8. Flag
```
JarkomIT{Gy4tT_M5g_4U_Qa4EJZagtbzZwuGn1phiGRvFJ5k1JGP2Mp5NpBZ7saMyjU1IUkPTPBiD1}
```

![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/Gajah_Terbang(Server-Recon)%20/src/3.png)
