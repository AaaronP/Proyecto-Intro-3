# Huffman Compression and Decompression

## Descripción

Este repositorio contiene una implementación del algoritmo de Huffman para la compresión y descompresión de archivos. El algoritmo de Huffman es un método de compresión sin pérdida que asigna códigos de longitud variable a los símbolos de entrada, de manera que los símbolos más frecuentes tengan códigos más cortos, y los símbolos menos frecuentes tengan códigos más largos.

## Características

- Compresión de archivos utilizando el algoritmo de Huffman.
- Descompresión de archivos previamente comprimidos.
- Fácil de usar a través de una interfaz de línea de comandos (CLI).
- Soporte para diferentes tipos de archivos de texto.

## Instalación

Clona este repositorio en tu máquina local:

    ```bash
    [git clone https://github.com/tuusuario/huffman-compression.git](https://github.com/AaaronP/Proyecto-Intro-3.git)
    cd Proyecto-Intro-3
    ```

3. No se requieren instalaciones adicionales, todas las dependencias son parte de la biblioteca estándar de Python.

## Uso

### Compresión

Para comprimir un archivo, utiliza el siguiente comando:

```bash
python compress.py input_file output_file
