#!/bin/bash


echo "Descomprimiendo imagenes.zip..."
unzip -q imagenes.zip -d carpeta_imagenes


if [ $? -eq 0 ]; then
    echo "Archivo descomprimido en carpeta_imagenes."
else
    echo "Error al descomprimir el archivo."
    exit 1
fi


HASH_BUSCADO="e5ed313192776744b9b93b1320b5e268"


echo "Buscando archivo con hash MD5 $HASH_BUSCADO..."
for file in carpeta_imagenes/*; do
    HASH_ACTUAL=$(md5sum "$file" | awk '{print $1}')
    if [ "$HASH_ACTUAL" == "$HASH_BUSCADO" ]; then
        echo "¡Se ha encontrado el archivo!: $file"
        exit 0
    fi
done

echo "No se encontró ningún archivo con el hash $HASH_BUSCADO."
exit 1
