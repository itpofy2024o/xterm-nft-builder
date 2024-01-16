#!/bin/sh

read num

rm -rf tw.json

for ((c=0;c<=$num-1;c++))
do 
    if [[ $c -eq 0 ]];then
        echo "[" >> tw.json
    fi
    cat ./assets/$c.json >> tw.json
    if [[ $c -eq $num-1 ]];then
        echo "]" >> tw.json
    else
        echo "," >> tw.json
    fi
done