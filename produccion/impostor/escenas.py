# -*- coding: utf-8 -*-
"""Escenas por bloque, escritas CONTRA la linea de voz de cada plano.

Solo texto corto: la ficha del personaje y el sufijo de estilo los pega
lote.py, identicos en las 225 imagenes.

Formato: (shot_id, tamano de plano, escena en ingles positivo, lleva host)
Si lleva host, la escena arranca en gerundio: se le antepone "He is".
"""

BLOQUE_01 = [
("SH001","Wide shot",
 "standing at the edge of a lit stage with one hard-edged circle of white light around his feet, "
 "facing a wide dark auditorium that stretches away into flat black",True),

("SH002","Close-up",
 "gripping one hand inside the other in front of his chest, the knuckles drawn pale against the grey "
 "sleeve, the background one flat block of dark",True),

("SH003","Medium close-up",
 "standing very still with his shoulders lifted toward his cap, one hard band of cold blue tone "
 "across his chest and a warm cream tone on his face above it",True),

("SH004","Medium shot",
 "turning his head slowly to one side, the navy cap in profile, rows of dark seats opening out in "
 "front of him",True),

("SH005","Wide shot",
 "a wall of pale cream oval head shapes filling the whole frame in even rows, each one carrying two "
 "small flat black oval marks, all of them facing the same direction",False),

("SH006","Medium shot",
 "standing at the head of a long conference table in a flat modern office, six simplified seated grey "
 "colleagues around it, all of their heads turned toward him",True),

("SH007","Wide shot",
 "a small child-sized grey figure standing alone in a wide classroom doorway, tall adult legs and "
 "chairs around it, the room bright and flat",False),

("SH008","Medium shot",
 "a tall wall covered in a grid of empty framed rectangles, and one small grey figure standing far "
 "below it looking up",False),

("SH009","Close-up",
 "a plain blank paper label pinned to the chest of a grey hoodie, the surface of the label smooth and "
 "empty, one flat block of light across it",False),

("SH010","Wide shot",
 "three simplified human figures standing side by side on flat ground: the first one covered in thick "
 "dark fur, the second with thin patchy fur, the third with smooth bare skin",False),

("SH011","Medium close-up",
 "standing in flat darkness with one hard-edged circle of bright white light landing directly on his "
 "face and cap, the rest of the frame solid black",True),

("SH012","Wide shot",
 "standing very small at the centre of a vast empty black space, one narrow beam of light coming "
 "straight down onto him from far above",True),

("SH013","Medium shot",
 "turning his head to look off toward one side of the frame, where a small warm orange glow sits far "
 "away in the flat dark",True),

("SH014","Wide shot",
 "an open savannah at dusk under a deep orange and purple flat sky, a ring of seated grey figures "
 "around one small pool of orange firelight, with a single figure standing upright inside the ring",False),

("SH015","Medium shot",
 "a blue engineer figure standing on a small wooden box with the chest pushed out and both arms held "
 "wide open, lit brightly from the front",False),

("SH016","Close-up",
 "holding a plain flat cream oval mask out at arm's length in both hands, the surface of the mask "
 "smooth and completely blank",True),

("SH017","Medium shot",
 "a blue engineer figure tightening a bolt on a large mechanical heart made of flat metal plates, a "
 "wrench in one hand",False),

("SH018","Wide shot",
 "an enormous flat chart painted on a wall with one thick line climbing steeply upward, and a small "
 "grey figure standing at the bottom looking up at it",False),

("SH019","Medium shot",
 "two simplified figures in white lab coats seated side by side at a wide desk in 1970s style, tall "
 "stacks of paper between them, warm flat lamplight",False),

("SH020","Close-up",
 "a thick paper file lying open on a dark desk, its pages smooth and empty, one flat block of warm "
 "lamplight falling across them",False),
]

BLOQUE_02 = [
("SH021","Wide shot",
 "a row of six standing grey figures side by side, each one holding a different flat object: a "
 "stethoscope, a thick book, a rolled sheet, a beaker, a pointer, a set of keys",False),

("SH022","Medium shot",
 "a wall grid of framed rectangles with smooth empty surfaces inside every frame, lit evenly and flat",False),

("SH023","Close-up",
 "a tall stack of framed rectangles piled one on top of another on a desk, the stack rising past the "
 "top edge of the frame",False),

("SH024","Medium shot",
 "a grey figure standing directly behind that tall stack, so that only the top of a navy cap shows "
 "above the highest frame",False),

("SH025","Wide shot",
 "the large mechanical heart of flat metal plates lying broken apart on a workshop floor, its pieces "
 "spread in a wide flat circle, the wrench abandoned beside them",False),

("SH026","Medium shot",
 "two thick flat vertical bars side by side on a plain background: the left bar short and dim, the "
 "right bar tall and bright, arrows of flat colour rising along the tall one",False),

("SH027","Close-up",
 "a small bright point of light at the centre of the frame with wide concentric rings spreading out "
 "from it in flat bands, filling the whole image",False),

("SH028","Wide shot",
 "an empty bedroom at night with one plain bed, the blanket flat and undisturbed, cold blue moonlight "
 "falling across it in a single hard-edged block",False),

("SH029","Medium shot",
 "a simplified grey figure sleeping calmly on its back in that bed, the blanket smooth, the whole "
 "frame quiet and evenly lit",False),

("SH030","Close-up",
 "a plain wooden box standing open on a dark surface, its inside smooth and completely empty, one "
 "hard block of light falling into it",False),

("SH031","Medium shot",
 "holding a bright glowing trophy shape up in both hands, the light from it throwing one enormous "
 "hard-edged black shadow of him across the wall behind",True),

("SH032","Wide shot",
 "two doors standing side by side in a plain flat wall: the left one small and low, the right one "
 "enormous and reaching past the top of the frame",False),

("SH033","Medium shot",
 "standing still while a disembodied grey hand extends a small bright award toward his chest from the "
 "edge of the frame",True),

("SH034","Wide shot",
 "a very long table stretching across the whole frame, covered end to end with framed rectangles "
 "lying flat, all of their surfaces smooth and empty",False),

("SH035","Medium close-up",
 "standing among all of those framed rectangles with his face flat and unreadable, the frames stacked "
 "around him up to his shoulders",True),

("SH036","Close-up",
 "carrying a heavy bright glowing block on one shoulder, that shoulder pressed down lower than the "
 "other under its weight",True),

("SH037","Wide shot",
 "standing very small at the base of an enormous horizontal beam raised high above him, the beam "
 "stretching across the top of the frame against a pale empty sky",True),

("SH038","Close-up",
 "the sharp edge of a high metal beam with flat empty air beyond it and the ground drawn as a tiny "
 "pattern very far below",False),

("SH039","Medium shot",
 "standing still while a grey figure faces him with one arm raised in a wide open gesture of praise, "
 "the light warm and flat on both of them",True),

("SH040","Close-up",
 "framed so that his face fills the frame, flat and unreadable, lit evenly, holding perfectly still",True),
]

BLOQUES = {1: BLOQUE_01, 2: BLOQUE_02}
