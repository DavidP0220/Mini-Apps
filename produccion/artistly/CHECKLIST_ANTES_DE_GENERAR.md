# Checklist Artistly — ANTES de cada imagen

Pegar en pantalla. Son 5 clics. Si se salta uno, la imagen sale distinta.

1. **Herramienta:** Consistent Characters → **3d & 2d Style Images**.
   (AI Image Designer v6 y Script To Storybook V2 NO sirven: ignoran el estilo.)

2. **Referencia:** volver a seleccionar **HOST_CORRECTO.png**.
   Artistly deja puesta como referencia **la última imagen que generó**.
   Si no la reseleccionas, la imagen 2 copia a la 1, la 3 copia a la 2…
   y a las 6 generaciones el personaje ya es otro. **Esta es la causa
   número uno de la pérdida de consistencia.**

3. **Formato:** poner **16:9**. Vuelve solo a 1:1 en cada generación.

4. **Prompt:** pegar completo, sin recortar. Cero negaciones
   (`no`, `without`, `never`, `avoid`, `remove`). Ver REGLAS_PROMPT_ARTISTLY.md.

5. **Una imagen por vez.** Nada de lotes: el lote encadena referencias.

---

## Si ya salió mal

No regenerar en cadena. Volver al paso 2, reseleccionar HOST_CORRECTO.png,
y generar de nuevo desde cero. Si falla un solo detalle: **inpaint**, no regenerar.
