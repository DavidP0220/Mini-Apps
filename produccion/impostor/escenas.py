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
 "standing directly behind that tall stack of frames, so that only the top of his navy cap shows "
 "above the highest one",True),

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

BLOQUE_03 = [
("SH041","Medium shot",
 "standing still in a bright room while looking away toward one dark corner where a small pile of "
 "crumpled paper sits on the floor",True),

("SH042","Wide shot",
 "a wide desk seen from above with two white dice resting on one side of a sheet of paper, and a "
 "second grey hand entering from the edge of the frame to rest on the same sheet",False),

("SH043","Close-up",
 "holding a small bright golden award between two fingers, turning it slowly on its side to inspect "
 "the edge, the rest of the frame in flat shadow",True),

("SH044","Medium shot",
 "standing inside a narrow dark gap between two tall flat panels, one panel lit warm and bright and "
 "the other flat grey, the gap running from the top of the frame to the bottom",True),

("SH045","Wide shot",
 "standing straight and evenly lit against a plain flat background with both arms relaxed at his "
 "sides, the whole frame calm and open",True),

("SH046","Medium shot",
 "standing in front of a tall wall covered in small flat screens, each screen showing one plain grey "
 "human silhouette, the glow falling cold on his cap and shoulders",True),

("SH047","Close-up",
 "two plain cream oval mask shapes lying side by side on a dark surface, the left one polished and "
 "brightly lit, the right one dull and matte",False),

("SH048","Wide shot",
 "the broken metal pieces of a mechanical heart swept into one corner of a workshop floor, and on the "
 "far wall a door standing open with flat white light pouring through it",False),

("SH049","Medium shot",
 "holding a phone up in front of his chest, its screen a bright grid of small glowing rectangles, the "
 "room around him flat and dark",True),

("SH050","Wide shot",
 "a long row of small brightly lit stages side by side, one posed figure standing on each, and at the "
 "far right end one dim ordinary room with a plain chair in it",False),

("SH051","Close-up",
 "a rectangular glowing screen with a row of sharp flat triangular teeth running along its bottom "
 "edge, lit hard from one side",False),

("SH052","Medium shot",
 "a grey hand pointing at one spot on a long horizontal line painted across a plain wall, the line "
 "running out of frame in both directions",False),

("SH053","Wide shot",
 "that same horizontal line continuing far to the left across a rough cave wall covered in simple "
 "ochre handprints and animal figures",False),

("SH054","Medium shot",
 "a figure in field clothes writing in a small notebook while standing beside a cluster of simple "
 "round huts, warm flat daylight",False),

("SH055","Wide shot",
 "a small village of round huts at dusk under a wide orange sky, a handful of simplified figures "
 "around one fire, and flat empty land all the way to the horizon",False),

("SH056","Medium shot",
 "a small child-sized figure standing frozen in the middle of a circle of seated adults, every adult "
 "head turned toward the child",False),

("SH057","Close-up",
 "that same child figure seen from the side with the head lowered and the shoulders pulled in tight, "
 "making the whole body smaller",False),

("SH058","Wide shot",
 "an enormous plain clock face on a wall with two thick black hands and a smooth empty surface, one "
 "hand sweeping backward",False),

("SH059","Medium shot",
 "two thick flat vertical bars side by side rising to exactly the same height, joined by a dotted "
 "line across their tops",False),

("SH060","Close-up",
 "the same two bars, the left one now short and flat and the right one shooting up past the top edge "
 "of the frame in bright colour",False),
]

BLOQUE_04 = [
("SH061","Wide shot",
 "standing at a long wedding table holding a raised glass, frozen in the middle of the motion, twenty "
 "seated figures around the table all turned toward him",True),

("SH062","Medium shot",
 "a phone lying face down on a plain wooden table in flat morning light, one window casting a hard "
 "bright rectangle across it",False),

("SH063","Wide shot",
 "standing alone and very small at the front of an enormous auditorium filled with steep rows of pale "
 "cream head shapes, every row facing him",True),

("SH064","Medium shot",
 "a large flat amplifier box with a round speaker cone and dials on its front, a thick black cable "
 "running out of it and off the edge of the frame",False),

("SH065","Close-up",
 "the end of that thick black cable plugged into a small dark socket set into bare earth, the ground "
 "cracked and dry around it",False),

("SH066","Wide shot",
 "standing in a wide empty landscape under a pale sky with one small distant group of figures far "
 "away and flat open ground everywhere else",True),

("SH067","Medium shot",
 "a tight cluster of about thirty simplified human figures standing close together, shoulders "
 "touching, all of them the same grey tone",False),

("SH068","Close-up",
 "two clasped hands filling the frame, one large and lined and one small and smooth, held firmly "
 "together against a flat dark background",False),

("SH069","Wide shot",
 "one small circle of orange firelight with seated figures around it, and flat solid black filling "
 "every other part of the frame in all directions",False),

("SH070","Medium shot",
 "a single line of footprints pressed into pale dust leading away from a fire and stopping abruptly "
 "at the edge of deep flat darkness",False),

("SH071","Close-up",
 "a stone spear point and a small caught animal laid together on bare ground, lit evenly and plainly, "
 "with nothing else around them",False),

("SH072","Wide shot",
 "a ring of seated figures around a fire with one clear empty gap left open in the circle, the gap "
 "facing the dark",False),

("SH073","Medium shot",
 "that same ring seen closer from just outside it, every face turned inward toward the centre, the "
 "firelight flat orange on all of them",False),

("SH074","Close-up",
 "five pointing hands entering the frame from five different directions, all of their fingers aimed "
 "at the same empty point at the centre",False),

("SH075","Wide shot",
 "a quiet study room with tall shelves of field notebooks and stacked papers, one figure seated at a "
 "desk under a single warm lamp",False),

("SH076","Medium shot",
 "a large flat world map on a wall with small red pins pressed into every continent, lit evenly",False),

("SH077","Close-up",
 "four hands in a row against a dark background, the first pointing, the second cupped beside a "
 "mouth, the third covering a face, the fourth pushing outward with the palm open",False),

("SH078","Wide shot",
 "standing tall and alone at the centre of a ring of seated figures around a fire, every seated head "
 "aimed directly at him",True),

("SH079","Medium shot",
 "a pyramid built of flat stone blocks standing completely upside down, balanced on its single point, "
 "against a plain pale sky",False),

("SH080","Wide shot",
 "a wide plain covered with dozens of those upside-down pyramids, each one balanced on its point, "
 "spread evenly to the horizon",False),
]

BLOQUE_05 = [
("SH081","Medium shot",
 "many grey hands rising together out of a crowd in one even motion, every arm at the same angle, "
 "none of the figures looking at each other",False),

("SH082","Wide shot",
 "a crowd of identical grey figures with one slightly taller figure among them being pressed back "
 "down by many hands flat on his shoulders",False),

("SH083","Medium shot",
 "one brightly glowing figure standing among grey ones while several cupped hands close in around the "
 "glow from every side, dimming it",False),

("SH084","Wide shot",
 "a large flat world map filling the frame with the same small symbol of a ring of seated figures "
 "repeated once on every continent",False),

("SH085","Close-up",
 "holding one empty open palm out flat in front of him against a plain dark background, the hand lit "
 "warm and evenly",True),

("SH086","Medium shot",
 "holding that same open palm out with a modern phone now lying face up on it and glowing bright "
 "blue, the room around him flat and dark",True),

("SH087","Wide shot",
 "a large crowd of grey figures split into two even halves by one clean bright vertical band of light "
 "running from the top of the frame to the bottom",False),

("SH088","Medium shot",
 "a hunter figure holding a large animal up above his head while the seated figures around him wave "
 "their hands low and flat in dismissal",False),

("SH089","Close-up",
 "a large dead animal lying on bare ground with several wide open laughing mouths drawn above it, "
 "seen from just above the ground",False),

("SH090","Medium shot",
 "the same hunter holding the animal out at arm's length with his own shoulders raised in a shrug, "
 "his head tilted down toward it",False),

("SH091","Close-up",
 "two hands passing a stone knife between them directly over the body of the animal, the blade "
 "catching one hard block of light",False),

("SH092","Wide shot",
 "one figure standing with an arm stretched out pointing forward while every other figure in the "
 "frame walks calmly away in a different direction",False),

("SH093","Medium shot",
 "that same figure with his mouth open in speech while every figure around him faces outward, their "
 "backs forming a closed wall",False),

("SH094","Close-up",
 "a row of wide open laughing mouths across the frame, and at the right end one hand cupped beside a "
 "mouth leaning in to whisper",False),

("SH095","Wide shot",
 "a long chain of figures spread across an open landscape, each one leaning toward the next to "
 "whisper, the chain running all the way to the horizon",False),

("SH096","Medium shot",
 "one figure standing alone at the centre while the ring of figures around him steps outward, opening "
 "a wide empty gap of ground between them",False),

("SH097","Close-up",
 "one grey hand lowering slowly onto a plain flat surface, the gesture small and ordinary, lit evenly",False),

("SH098","Wide shot",
 "sitting alone on the ground far outside the reach of a fire at night, facing away from it, while "
 "the whole group eats together inside the ring of light behind him",True),

("SH099","Medium shot",
 "thirty small simplified figures arranged in a neat even grid on flat pale ground, seen from above",False),

("SH100","Close-up",
 "three simplified faces very close together filling the frame, all of them calm and familiar, lit "
 "warm and softly",False),
]

BLOQUE_06 = [
("SH101","Wide shot",
 "thirty figures seated in a wide circle around one large shared pile of food at the centre, the "
 "firelight flat orange across all of them",False),

("SH102","Medium shot",
 "a ring of sleeping figures lying around a low fire under a dark blue sky, with one clear empty gap "
 "left in the ring",False),

("SH103","Close-up",
 "a small woven cradle basket resting empty on bare ground, warm firelight falling into it from one "
 "side",False),

("SH104","Wide shot",
 "flat open land stretching to the horizon in every direction under a black sky, with one small fire "
 "as the only point of light anywhere in the frame",False),

("SH105","Medium shot",
 "sitting slightly hunched at the outer edge of a fire circle, watching the group, his arms wrapped "
 "around his knees",True),

("SH106","Close-up",
 "a small worn stone charm gripped tight inside a closed fist, the knuckles pale, one hard block of "
 "firelight across them",False),

("SH107","Wide shot",
 "an open savannah at midday under a pale flat sky with the whole band spread across it, each figure "
 "busy with a different task",False),

("SH108","Medium shot",
 "standing upright with a large caught animal lying on the ground at his feet, both arms at his "
 "sides, the light flat and bright",True),

("SH109","Wide shot",
 "the whole band standing completely still across the frame with every single face turned toward one "
 "point at the right edge",False),

("SH110","Medium close-up",
 "standing with his chest and shoulders held tight and both hands completely still at his sides, "
 "the light hard on one side of him",True),

("SH111","Wide shot",
 "one figure standing tall and relaxed in the middle of the group with both arms open wide, brighter "
 "than everyone around him",False),

("SH112","Medium shot",
 "that same patch of ground now empty, with the group closed into a tight circle around the bare "
 "space where the figure stood",False),

("SH113","Close-up",
 "two small pebbles resting on a flat stone, with one finger pushing the left pebble off the edge",False),

("SH114","Medium shot",
 "two figures standing side by side, each one holding a large object up above his head, both lit the "
 "same way",False),

("SH115","Close-up",
 "a chest and shoulders filling the frame with one spreading patch of cold blue tone across the "
 "centre of the chest, the rest of the body warm cream",False),

("SH116","Medium shot",
 "one of those two figures handing his object sideways to the person next to him, his shoulders "
 "lowered and his head slightly down",False),

("SH117","Wide shot",
 "the other figure standing tall and bright at the centre of the group with the object still raised, "
 "every face around him turned toward it",False),

("SH118","Medium shot",
 "two long lines of figures receding into the distance side by side, the left line continuing full "
 "and the right line thinning down to a single last figure",False),

("SH119","Wide shot",
 "one single continuous line of figures walking forward out of a distant horizon toward the front of "
 "the frame, growing larger as they come",False),

("SH120","Medium shot",
 "a wide snowfield under a pale grey sky with one set of footprints crossing it and stopping in the "
 "middle of the open white",False),
]

BLOQUES = {1: BLOQUE_01, 2: BLOQUE_02, 3: BLOQUE_03, 4: BLOQUE_04,
           5: BLOQUE_05, 6: BLOQUE_06}
