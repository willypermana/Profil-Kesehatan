# Profil-Kesehatan
Berkas LaTeX dan lain sebagainya untuk menyusun Profil Kesehatan (https://www.kemkes.go.id/article/view/19100200001/Juknis-Profil-Kesehatan-2019.html).

This particular template was made on TeX-Live 2016 (couldn’t get around to actually updating it), but it should be working reasonably well with newer releases.

Untuk pembuatan grafik memerlukan python, matplotlib, numpy dan pandas.

Konversi ke pdf menggunakan xelatex.

## fc-cache_batch.bat
Saat kompilasi ke pdf, xelatex mungkin akan sering macet di `(c:/texlive/2016/texmf-dist/tex/latex/euenc/eu1lmr.fd)`. Dari beberapa sumber, hal ini karena xelatex tidak menemukan tembolok (cache) fonta lokal, lalu mencoba membaca ulang seluruh font di sistem. Jalankan skrip fc-cache_batch.bat sebagai administrator untuk membangun ulang tembolok fonta lokal.

## Why so few samples on chart picture scripts?
I *think* there's about 70+ charts used in this report. So it's too much efforts to edit and upload to begin with, and there are even some more charts that I had to scrap away because it didn't get editorial approval and thus didn't make it to the published version. I'm putting some samples here and there, though.

## Why not using Word or other word processors?
I used to. Honestly, the only good thing out of office suites are their spreadsheets. Unfortunately, I found out that a structured document demanding consistent formatting across hundred of pages and with lots of cross-references is a bit difficult to do with word processors. The results, binded into paperback or hardcover, were just a little bit better than inconsistent mess. It's very frustrating, and to be honest, quite shameful. There were some kind of amateurish vibes when you looked at them. Maybe I'm just not good enough with it.

Anyway, I moved to LaTeX for the last three yearly reports and I could say I'm quite satisfied with the printed results. Even if the learning curve was steep at first.
