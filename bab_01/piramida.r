## Another way to make population pyramid, using R
## You need to install the pyramid package first
##    install.packages(pyramid)
## Then run this file from R console
##    source("piramida.r")
## The shortcoming of this approach is that I still can't figure out the way 
## to put labels on each population bars

## Load pyramid library
library(pyramid)
ages <- c('0-4','5-9','10-14','15-19','20-24', '25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75+' )
males <- c(4882,5664,5373,5545,4775,4608,5043,6061,5357,4519,3357,2699,2123,1528,873,938)
females <- c(4573,5286,5124,5255,4558,4451,4634,5685,4711,3925,3072,2694,2176,1616,929,1271)
 
## Start PDF/ PNG device driver to save output
png(filename="piramida.png", height=500, width=800, bg="white")
#pdf(file="piramida.pdf", height=5, width=8)
 
## Plot the pyramid
data <- data.frame(males,females,ages)
pyramid(data, Clab='Kelompok Umur', Llab='Laki-laki', Rlab='Perempuan', Lcol="#bfe4ff", Rcol ="#ffcabf",Cgap=0.2, Cadj=0, Ldens=-1, AxisFM='d', AxisBM=".", GL=FALSE, main="Piramida Penduduk\n Tahun 2019")
 
## Flush plot to output file
dev.off()
