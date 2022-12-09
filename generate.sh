max=24
expt=9
for e in `seq 1 $expt`
do 
    mkdir 100MB_expt_$e
    cd 100MB_expt_$e
    for i in `seq 0 $max`
    do
        dd if=/dev/urandom of=100MB_$i bs=1M count=100
    done
    cd ..
done