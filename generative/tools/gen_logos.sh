#!/bin/sh
cd ../01-content/output || exit 1
for i in logo-prompt*.txt
do
    name="${i%.*}"
    echo $name
    python ../../tools/generate-image-for-prompt2.py $name.txt $name
done
