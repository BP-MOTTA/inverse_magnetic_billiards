set terminal pngcairo size 1290,641
set output 'pBi1Bo2PS.png'
set key noautotitle
set title 'Bin = 1, Bout = 2'
set xlabel "s (adimensional)"
set ylabel "{/Symbol q} (º)"
plot 'sdata1.dat' pt 0 lc 'black', 'sdata2.dat' pt 0 lc 'black'  ,'sdata3.dat' pt 0 lc 'black' ,'sdata4.dat' pt 0 lc 'black' ,'sdata5.dat' pt 0 lc 'black' ,'sdata6.dat' pt 0 lc 'black' ,'sdata7.dat' pt 0 lc 'black' ,'sdata8.dat' pt 0 lc 'black' ,'sdata9.dat' pt 0 lc 'black' ,'sdata10.dat' pt 0 lc 'black' 

