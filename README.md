# Profil-Kesehatan
Berkas LaTeX dan lain sebagainya untuk menyusun Profil Kesehatan (https://www.kemkes.go.id/article/view/22101000001/Juknis-Profil-Kesehatan-2022.html).

This particular template was made on TeX-Live 2021, but it should be working reasonably well with either older or newer releases.

Editor yang direkomendasikan: TeXStudio.

Untuk pembuatan grafik memerlukan python, matplotlib, numpy dan pandas. (Or use Excel built-in chart, but it's harder to maintain consistency)

Jika perlu grafik peta, QGIS sangat direkomendasikan (of course, looking for your city's/ regency's districts division .shp files on the first place might be tad difficult).

Konversi ke pdf menggunakan xelatex.

Bibliografi menggunakan BibTeX.

## Why use XeTeX?
LaTeX supposedly support myriad of modern fonts, but when I first create this template back in 2016, I just couldn't find the right settings to use them. After some time, I threw the towel and just use XeTeX instead. Voila, instant modern font.

## fc-cache_batch.bat
Saat kompilasi ke pdf, xelatex mungkin akan sering macet di `(c:/texlive/2021/texmf-dist/tex/latex/euenc/eu1lmr.fd)`. Dari beberapa sumber, hal ini karena xelatex tidak menemukan tembolok (cache) fonta lokal, lalu mencoba membaca ulang seluruh font di sistem. Jalankan skrip fc-cache_batch.bat sebagai administrator untuk membangun ulang tembolok fonta lokal.

## On Appendix 3 - Profile Tables
There's really no short way to make this particular appendix in LaTeX. `excel2latex` add-in helps, but you'd still need to fine tune every single tables.

https://ctan.org/pkg/excel2latex?lang=en

Conversely you could just use the provided Excel sheets from the Juknis itself and call it a day, but then you have to find another way to integrate them to the List of Tables...

Not going to put all of tables here. Just the very first one and a quite long table for the general idea.

## Why so few samples on chart picture scripts?
I *think* there's about 100+ charts used in this report. So it's too much efforts to edit and upload to begin with, and there are even some more charts that I had to scrap away because it didn't get editorial approval and thus didn't make it to the published version. I'm putting some samples here and there, though.

## Why not using Word or other word processors?
I used to. Honestly, the only good thing out of office suites are their spreadsheets (presentation is up to debate). Unfortunately, I found out that a structured document demanding consistent formatting across hundreds of pages and with lots of cross-references is a bit difficult to do with word processors. The results, binded into paperback or hardcover, were just a little bit better than inconsistent mess. It's very frustrating, and to be honest, quite shameful. There were some kind of amateurish vibes when you looked at them. Maybe I'm just not good enough with it.

Anyway, I moved to LaTeX for the last six yearly reports and I could say I'm quite satisfied with the printed results. Even if the learning curve was steep at first.
