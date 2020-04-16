# Profil-Kesehatan
Berkas LaTeX dan lain sebagainya untuk menyusun Profil Kesehatan (https://www.kemkes.go.id/article/view/19100200001/Juknis-Profil-Kesehatan-2019.html).

This particular template was made on TeX-Live 2016 (couldn’t get around to actually updating it), but it should be working reasonably well with newer releases.

Untuk pembuatan grafik memerlukan python, numpy dan pandas.

Konversi ke pdf menggunakan xelatex.

## fc-cache_batch.bat
Saat kompilasi ke pdf, xelatex mungkin akan sering macet di `(c:/texlive/2016/texmf-dist/tex/latex/euenc/eu1lmr.fd)`. Dari beberapa sumber, hal ini karena xelatex tidak menemukan tembolok (cache) fonta lokal, lalu mencoba membaca ulang seluruh font di sistem. Jalankan skrip fc-cache_batch.bat sebagai administrator untuk membangun ulang tembolok fonta lokal.
