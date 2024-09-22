# ===== 22 Nightmare =====

### nc 10.15.42.60 45000

1. File yang dikirim penyerang?
- Format: filename.extension
- Answer: Sh1k4.jpg

Kami menggunakan filter ftp untuk menemukan file yang dikirim penyerang, dan kami mendapatkan file Sh1k4.jpg

![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/22_Nightmare/src/1.png)

2. Apa nama file yang dikirim?
- Format: string
- Answer: NUN

Setelah file diatas kami download, ternyata ada tulisan "NUN"

![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/22_Nightmare/src/2.png)

3. Pada stream keberapa file kedua dikirim setelah file pertama?
- Format: Number
- Answer: 141

Ada keterangan stream index disini :

![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/22_Nightmare/src/3.png)

4. Siapa asli nama pengirim?
- Format: string ex. Nathan Kho
- Answer: Torako Koshi

Pada sebuah traffic, ada binary code yang tidak biasa, karenanya kami melakukan decode menggunakan cyberchef pada binary tersebut. dan hasilnya kami menemukan ini :

![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/22_Nightmare/src/4.png)

5. Flag :
```
JarkomIT{Sh1k4n0ko_N0_k05h1tan_WUw8ly6cPhe7sRKqxEObn8OSE7Ank3frfMeb7dz5CRCxziayZXpv4UNU}
```
![github-small](https://github.com/bielnzar/Jarkom-Modul-1-IT23-2024/blob/main/22_Nightmare/src/5.png)
