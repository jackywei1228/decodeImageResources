for file in *.dds
do
    echo convert "$file" "$(basename "$file" .dds).png"
    convert "$file" "$(basename "$file" .dds).png"
done
