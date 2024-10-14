#!/bin/bash

# Descomprimir el archivo imagenes.zip directamente en carpeta_imagenes
echo "Descomprimiendo imagenes.zip..."
unzip -q imagenes.zip -d carpeta_imagenes

# Verificar si se descomprimió correctamente
if [ $? -eq 0 ]; then
    echo "Archivo descomprimido en carpeta_imagenes."
else
    echo "Error al descomprimir el archivo."
    exit 1
fi

# Hash MD5 que estamos buscando
HASH_BUSCADO="e5ed313192776744b9b93b1320b5e268"

# Buscar el archivo con el hash MD5 especificado
echo "Buscando archivo con hash MD5 $HASH_BUSCADO..."
for file in carpeta_imagenes/*; do
    HASH_ACTUAL=$(md5sum "$file" | awk '{print $1}')
    if [ "$HASH_ACTUAL" == "$HASH_BUSCADO" ]; then
        echo "¡Archivo encontrado!: $file"
        exit 0
    fi
done

echo "No se encontró ningún archivo con el hash $HASH_BUSCADO."
exit 1
