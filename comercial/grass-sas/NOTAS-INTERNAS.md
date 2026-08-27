# GRASS S.A.S. — notas internas del consolidado

**Uso interno. No enviar al cliente.** Fecha: 27/08/2026.

## 1. Cómo cuadran las cotizaciones

| Documento | Alcance | Valor sin IVA |
|---|---|---|
| COT-0086 (20/08) | 20 RELPOL + 40 HONGFA + 4 barras | $ 3.570.000 |
| COT-0092 (22/08) | 37 refs — neumática, PLC, instrumentación, tablero, conductores **+ los relés de la 0086** | $ 26.563.000 |
| COT-0098 | 30 refs — contactores, guardamotores, borneras + variador WEG | $ 5.912.921 |
| **COT-0096 (22/08)** | **67 refs — todo junto** | **$ 32.740.421** |

**Verificado:** 0092 + 0098 = $ 32.475.921. La 0096 da $ 264.500 más porque subió los RELPOL
de 20 a 25 unidades (5 × $ 52.900 = $ 264.500). Todo lo demás es idéntico. No hay error en ningún
documento.

La COT-0086 quedó absorbida dentro de la 0092 y de la 0096. En la 0096 ese bloque de relés vale
$ 3.834.500 (25 RELPOL en vez de 20).

Suma de los 8 subtotales de la 0096 verificada uno por uno: **$ 32.740.421 exacto, 67 referencias,
553 unidades.** La COT-0100 usa esas mismas cifras sin tocar un peso.

## 2. Cruce con los competidores

### Imagen Eléctrica Ltda. — IE-107-190 (13/08/2026)

Sus 34 ítems corresponden **uno a uno** con los grupos A–E de la cotización nuestra. Comparación
limpia:

| | Ellos | Nosotros |
|---|---|---|
| Base | $ 26.182.500 | $ 22.844.534 |
| IVA 19 % | $ 4.974.675 | $ 4.340.461 |
| Total | $ 31.157.175 | $ 27.184.995 |

**Ganamos por $ 3.337.966 de base (12,75 %).** Argumento sólido y verificable ítem por ítem.

### Industrial Solutions Colombia S.A.S. — 15025 (12/08/2026)

Cubre los grupos G + H (lo que se cotizó aparte como COT-0098).

| | Ellos | Nosotros |
|---|---|---|
| Base | $ 5.212.238 | $ 5.912.921 |
| IVA 19 % | $ 990.326 | $ 1.123.455 |
| Total | $ 6.202.564 | $ 7.036.376 |

> **Ojo con esto.** Sin IVA nuestra oferta ganaba ($ 5.912.921 contra $ 6.202.564 de ellos con
> IVA). **Al facturar con IVA ese argumento se cae:** quedamos $ 700.683 de base por encima
> (13,4 %). ISC es distribuidor Chint/Tbloc y saca entre 54 % y 68 % de descuento sobre lista;
> ítem por ítem estamos entre 10 % y 58 % arriba de ellos en ese bloque.
>
> Por eso el comparativo de la COT-0100 se plantea **a nivel de paquete completo**, no bloque por
> bloque. Si preguntan por ese bloque puntual, el argumento es el variador: WEG CFW500 de 3 HP con
> soporte en Colombia contra INVT GD27 de 2 HP importado.

### Huecos de alcance nuestros frente a ISC — REVISAR

ISC incluye tres referencias que nuestra cotización **no tiene**:

| Referencia | Cant. | Valor ISC |
|---|---|---|
| Contactor NXC 16 A (AC3) / 25 A (AC1), bobina 220 V | 10 | $ 234.300 |
| Guardamotor NS2-80B 25-40 A | 2 | $ 415.353 |
| Relevo JZX-22F 14 pines 3 A 220 V AC | 5 | $ 49.127 |
| **Total** | | **$ 698.780** |

Si GRASS los necesita hay que agregarlos a la COT-0100 antes de enviarla, o el cliente va a
encontrar el hueco cuando compare. Confirmar con Luis Enrique qué motores quedan en esos
arranques.

### Comparación de paquete completo — la que va en el documento

| | Comprando a los dos | COT-0100 |
|---|---|---|
| Base | $ 31.394.738 | $ 32.740.421 |
| IVA 19 % | $ 5.965.001 | $ 6.220.680 |
| Total | $ 37.359.739 | $ 38.961.101 |

Pagan $ 1.601.362 más y se llevan incluidos los 69 módulos de relé de interfaz, que valen
$ 4.739.730 con IVA y que **ninguno de los dos cotizó**. **Ventaja neta a favor de GRASS:
$ 3.138.368.** Esta cifra sí es defendible con los tres documentos sobre la mesa.

## 3. Lo que se corrigió de la COT-0096

- **La cifra de "13,9 % más barato / $ 4.329.675 menos" no se sostiene.** Salía de comparar nuestro
  total *sin* IVA contra el total *con* IVA de Imagen Eléctrica, y además metía los relés que ellos
  no cotizaron. Con IVA en ambos lados el número desaparece. Se reemplazó por la comparación de
  paquete completo, que es verificable.
- Se quitó el bloque de marketing "por qué esta es la mejor compra" y el recuadro separado de la
  COT-0086: sobraban y hacían ruido.
- Se quitó la mención de "no responsable de IVA — Art. 437 E.T." del pie de la tabla, que ya no
  aplica.
- El anexo de detalle se mantiene completo, en página aparte, para que el cliente pueda auditar.

## 4. Números de la COT-0100

| Concepto | Valor |
|---|---|
| Base gravable | $ 32.740.421 |
| IVA 19 % | $ 6.220.680 |
| **Total** | **$ 38.961.101** |
| Anticipo 60 % | $ 23.376.661 |
| Saldo 40 % | $ 15.584.440 |

**Retenciones estimadas** si GRASS es agente retenedor: retefuente compras 2,5 % ≈ $ 818.511 y
reteIVA 15 % del IVA ≈ $ 933.102. Total ≈ **$ 1.751.613** que no llegan a la cuenta en el momento
del pago. No es plata perdida —se cruza en las declaraciones— pero **no contar con ella** para
comprar el material.

**IVA que realmente se gira a la DIAN:** IVA generado menos IVA descontable de las compras a
proveedores. Con el código 48 activo, el IVA que hoy queda enterrado como costo pasa a ser
descontable, así que el margen real sube manteniendo los mismos precios base.

## 5. Pendientes antes de enviar

- [ ] Decidir si se agregan los 10 contactores 16 A, los 2 guardamotores 25-40 A y los 5 relés
      JZX-22F (sección 2). Si se agregan, hay que recotizarlos y actualizar la COT-0100.
- [ ] Verificar vigencia de la firma electrónica en el portal de la DIAN.
- [ ] Verificar el correo registrado en el RUT — ahí llega el token de habilitación.
- [ ] Agregar la responsabilidad 48 en la casilla 53 del RUT.
- [ ] Habilitación de facturación electrónica, set de pruebas y numeración con prefijo FE.
- [ ] Conseguir contador: con el código 48 la declaración de IVA es obligatoria.
- [ ] Llenar los datos del representante legal de GRASS en el contrato y en el pagaré.
- [ ] Hacer revisar el contrato y el pagaré por un abogado antes de firmarlos.

## 6. Documentos generados

| Archivo | Qué es |
|---|---|
| `COT-0100-cotizacion-con-IVA` | Cotización consolidada, IVA incluido. Reemplaza 0086, 0092, 0096 y 0098 |
| `carta-facturacion-iva` | Comunicación formal al cliente sobre la facturación con IVA y los plazos |
| `contrato-suministro` | Contrato de suministro CS-0100-2026 |
| `pagare-y-carta-instrucciones` | Pagaré PG-0100-2026 y su carta de instrucciones |

Cada uno está en `.html` (fuente editable) y en `.pdf` (listo para enviar). Para regenerar los PDF
después de editar un HTML, se imprime a PDF desde el navegador con márgenes por defecto.
