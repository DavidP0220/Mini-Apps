#!/usr/bin/env python3
"""FACTORY SETTINGS - avatar del canal desde el arte de logo generado con IA.

Metodo de la marca: el arte lo hace la IA, la geometria la hace el codigo.
Aqui el codigo hace dos cosas que el generador no hace bien:

  1. Normaliza el fondo al negro de marca #02060E. El generador entrega un
     cuadrado redondeado sobre un negro ligeramente distinto; a 32 px eso se
     ve como un halo sucio.
  2. Reencuadra al craneo. En el arte original el punto ambar ocupa el 1,26%
     del lienzo; reencuadrado sube al 1,70% sin recortar el perfil. El punto
     ambar es la firma de la marca - es lo unico que tiene que sobrevivir al
     tamano de 32 px al que YouTube muestra la foto de perfil.

Uso:  python3 generar-avatar.py     (lee logo-fuente-ia.png, escribe avatar.png)
"""
from PIL import Image
import numpy as np

FUENTE, SALIDA = "logo-fuente-ia.png", "avatar.png"
NEGRO_MARCA = [2, 6, 14]      # #02060E
UMBRAL_FONDO = 85             # por debajo de esto un pixel es fondo, no dibujo
LADO, CX, CY = 880, 519, 450  # recorte cuadrado sobre el lienzo 1024 de origen
FINAL = 800                   # 800x800, la medida que pide YouTube

im = Image.open(FUENTE).convert("RGB")
a = np.asarray(im).astype(int)
a[a.max(axis=2) < UMBRAL_FONDO] = NEGRO_MARCA
im = Image.fromarray(a.astype("uint8"))
im = im.crop((CX - LADO // 2, CY - LADO // 2, CX + LADO // 2, CY + LADO // 2))
im.resize((FINAL, FINAL), Image.LANCZOS).save(SALIDA)
print(f"{SALIDA} ok - {FINAL}x{FINAL}")
