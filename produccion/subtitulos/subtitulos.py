# -*- coding: utf-8 -*-
"""Subtitulos del canal, con los tiempos reales de la voz.

Edge TTS puede entregar, en la misma pasada que el audio, la marca de tiempo
de CADA palabra. Este script toma ese archivo y lo reagrupa en bloques de 3 a
4 palabras con el estilo del canal. Los tiempos no se estiman: son los que
dijo el locutor.

Uso
---
1. Generar voz y marcas juntas:

   edge-tts --voice en-US-AndrewNeural --rate=-15% \\
            --file NARRACION.txt \\
            --write-media VOZ.mp3 --write-subtitles VOZ.vtt

2. Convertir a los subtitulos del canal:

   python3 subtitulos.py VOZ.vtt SUBS.ass

3. Quemarlos sobre el video:

   ffmpeg -i video.mp4 -vf "ass=SUBS.ass" -c:a copy final.mp4
"""
import re, sys

MAX_PALABRAS = 4        # canon del canal: 3 a 4 palabras por bloque
MIN_SEG      = 0.40     # nada mas corto se alcanza a leer

CABECERA = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: MM,Arial,72,&H0000D9FA,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,5,2,2,80,80,110,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""

def t(seg):
    h=int(seg//3600); m=int(seg%3600//60); s=seg%60
    return f"{h:d}:{m:02d}:{s:05.2f}"

def leer_vtt(ruta):
    """Devuelve [(inicio, fin, palabra)] desde el VTT de edge-tts."""
    txt=open(ruta, encoding='utf-8').read()
    pat=re.compile(r'(\d\d):(\d\d):(\d\d[.,]\d+)\s*-->\s*(\d\d):(\d\d):(\d\d[.,]\d+)\s*\n(.+)')
    out=[]
    for m in pat.finditer(txt):
        a=int(m[1])*3600+int(m[2])*60+float(m[3].replace(',','.'))
        b=int(m[4])*3600+int(m[5])*60+float(m[6].replace(',','.'))
        w=m[7].strip()
        if w: out.append((a,b,w))
    return out

def bloques(palabras):
    """Agrupa en bloques de hasta MAX_PALABRAS, cortando en la puntuacion."""
    out, buf = [], []
    for a,b,w in palabras:
        buf.append((a,b,w))
        fin_de_frase = w[-1] in '.!?,;:'
        if len(buf) >= MAX_PALABRAS or (fin_de_frase and len(buf) >= 2):
            out.append(buf); buf=[]
    if buf:
        if out and len(buf) == 1: out[-1] += buf      # una palabra suelta se pega al anterior
        else: out.append(buf)
    return out

def main():
    if len(sys.argv) < 3:
        raise SystemExit("uso: python3 subtitulos.py VOZ.vtt SUBS.ass")
    pal = leer_vtt(sys.argv[1])
    if not pal:
        raise SystemExit("el VTT no trae marcas de palabra. Genera el audio con --write-subtitles.")
    bl = bloques(pal)

    lineas, cortos = [], 0
    for i, grupo in enumerate(bl):
        ini = grupo[0][0]
        fin = grupo[-1][1]
        # que no se corte antes de tiempo ni se solape con el siguiente
        if fin - ini < MIN_SEG:
            fin = ini + MIN_SEG; cortos += 1
        if i+1 < len(bl):
            fin = min(fin, bl[i+1][0][0] - 0.02)
        texto = ' '.join(w for _,_,w in grupo).upper()
        lineas.append(f"Dialogue: 0,{t(ini)},{t(fin)},MM,,0,0,0,,{texto}")

    open(sys.argv[2],'w',encoding='utf-8').write(CABECERA + '\n'.join(lineas) + '\n')

    largos = [g for g in bl if len(g) > MAX_PALABRAS]
    print(f"{len(pal)} palabras -> {len(bl)} bloques")
    print(f"duracion total: {t(pal[-1][1])}")
    print(f"bloques de mas de {MAX_PALABRAS} palabras: {len(largos)}")
    print(f"bloques estirados al minimo de {MIN_SEG}s: {cortos}")
    print(f"escrito: {sys.argv[2]}")

if __name__ == '__main__':
    main()
