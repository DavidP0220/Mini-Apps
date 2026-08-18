# -*- coding: utf-8 -*-
"""Genera datos/catalogo.json: 3 canales x 20 videos = 60 videos/mes.
Titulos curados en ingles (mercado global = RPM alto), con frecuencia,
duracion, texto de miniatura y tema visual."""
import json, os, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

CANALES = {
 "lakshmi": {
  "nombre": "Maha Lakshmi Sanctuary",
  "handle": "@MahaLakshmiSanctuary",
  "deidad": "Goddess Maha Lakshmi",
  "paleta": ["#FFD700", "#0B132B", "#B8860B"],
  "estetica": "golden lotus temple, coins of light, saffron and gold silk, sacred indian goddess iconography, luminous",
  "bloques": ["Flujo Inagotable", "Ashta Lakshmi", "Pacto Kubera & Lakshmi", "Purificacion de Escasez"],
  "videos": [
   ("The Golden River of Lakshmi", 528, 3, "MONEY FLOWS", "golden river flowing through a lotus temple at sunrise"),
   ("Lakshmi's Infinite Wealth Current", 888, 3, "INFINITE WEALTH", "endless stream of gold coins turning into light"),
   ("Rain of Gold Coins Meditation", 888, 2, "RAIN OF GOLD", "soft rain of golden coins over a marble temple"),
   ("Sacred Lotus of Prosperity", 432, 8, "SACRED LOTUS", "giant blooming lotus over still water, gold reflections"),
   ("The Wealth Gate Opens Tonight", 777, 3, "GATE OPENS", "ornate golden gate opening into radiant light"),
   ("Adi Lakshmi: Primordial Abundance", 963, 3, "PRIMORDIAL", "cosmic goddess silhouette among stars and gold nebula"),
   ("Dhana Lakshmi: Magnet for Money", 888, 2, "MONEY MAGNET", "glowing gold vortex drawing coins inward"),
   ("Dhanya Lakshmi: Abundant Harvest", 432, 3, "HARVEST", "golden wheat fields at dawn with temple silhouette"),
   ("Gaja Lakshmi: Royal Fortune", 528, 3, "ROYAL FORTUNE", "white elephants pouring golden water over the goddess"),
   ("Santana Lakshmi: Blessings of Legacy", 432, 8, "LEGACY", "warm family hearth of light, golden aura, soft temple"),
   ("Kubera's Treasury Unsealed", 777, 3, "TREASURY", "underground vault of gold opening, mystic blue and gold"),
   ("The Kubera Mantra Frequency", 888, 2, "KUBERA CODE", "ancient yantra glowing over gold coins"),
   ("Lakshmi & Kubera: The Wealth Pact", 528, 3, "WEALTH PACT", "two divine figures of light exchanging a golden orb"),
   ("Vault of Endless Riches", 888, 8, "ENDLESS", "infinite hall of golden pillars stretching to horizon"),
   ("Attract Unexpected Money in 7 Days", 777, 3, "7 DAYS", "calendar of light with golden coins falling"),
   ("Burn the Roots of Poverty", 396, 3, "BURN SCARCITY", "dark chains dissolving into golden sparks"),
   ("Cleansing the Money Bloodline", 417, 3, "CLEAR LINEAGE", "ancestral tree of light being cleansed by gold rain"),
   ("Release the Fear of Not Enough", 396, 8, "RELEASE FEAR", "person of light exhaling grey smoke into golden dawn"),
   ("Rewrite Your Money Story Tonight", 528, 8, "REWRITE", "open glowing book with golden script, temple at night"),
   ("Sleep Rich: 8 Hours of Lakshmi Grace", 432, 8, "SLEEP RICH", "night sky over a lotus lake, gold moonlight, serene"),
  ]},
 "ganesha": {
  "nombre": "Lord Ganesha 432Hz",
  "handle": "@LordGanesha432Hz",
  "deidad": "Lord Ganesha",
  "paleta": ["#FF7F11", "#0B132B", "#FFD700"],
  "estetica": "orange and gold ganesha iconography, marigold flowers, temple stone, sunrise light, obstacle-breaking symbolism",
  "bloques": ["Corte de Mala Racha", "Exito en Negocios", "Escudo y Sabiduria", "Nuevos Comienzos"],
  "videos": [
   ("Ganesha Removes Every Obstacle Tonight", 432, 3, "OBSTACLES GONE", "stone walls cracking open into golden light"),
   ("Break the Chain of Bad Luck", 396, 3, "BREAK THE CHAIN", "iron chains shattering into orange sparks"),
   ("The Path Opener Frequency", 528, 3, "PATH OPENER", "narrow temple path widening into a sunrise road"),
   ("End of the Losing Streak", 417, 8, "IT ENDS NOW", "storm clouds parting over a marigold temple"),
   ("Cut the Cords That Block You", 396, 3, "CUT THE CORDS", "glowing blade severing grey threads"),
   ("Ganesha for Business Growth", 888, 3, "BUSINESS GROWTH", "rising golden graph made of light over a marketplace"),
   ("Sales Flow Activation 888Hz", 888, 2, "SALES FLOW", "shop doorway glowing, streams of people as light"),
   ("Blessing for New Contracts", 777, 3, "NEW CONTRACTS", "scroll and seal glowing gold on temple stone"),
   ("Prosperity for Entrepreneurs", 528, 8, "ENTREPRENEUR", "sunrise over city skyline with ganesha silhouette"),
   ("The Merchant's Golden Hour", 432, 3, "GOLDEN HOUR", "bazaar at golden hour, warm dust light"),
   ("Shield of Ganesha: Protection Sound", 741, 3, "PROTECTION", "dome of golden light around a meditating figure"),
   ("Remove Envy and Evil Eye", 741, 3, "EVIL EYE OUT", "dark eye dissolving into marigold petals"),
   ("Wisdom to Choose the Right Path", 963, 3, "CLARITY", "two roads, one lit in gold, misty mountains"),
   ("Calm Mind, Clear Decisions", 432, 8, "CLEAR MIND", "still lake mirroring a temple, mist, dawn"),
   ("Guardian of the Home Frequency", 528, 8, "HOME SHIELD", "house glowing with protective gold aura at night"),
   ("New Beginnings Start Today", 528, 3, "NEW BEGINNING", "first sunlight over an open temple gate"),
   ("Ganesha Manifestation Ritual 1111Hz", 1111, 2, "1111 PORTAL", "11:11 portal of light above a lotus"),
   ("Say Yes to the Life You Want", 777, 3, "SAY YES", "figure stepping into a corridor of golden light"),
   ("Move Forward Without Fear", 417, 8, "NO FEAR", "long road through mountains at sunrise"),
   ("Sleep and Wake Up Unblocked", 432, 8, "WAKE UNBLOCKED", "starry night over temple, soft orange glow"),
  ]},
 "uriel": {
  "nombre": "Archangel Uriel Divine Light",
  "handle": "@ArchangelUrielLight",
  "deidad": "Archangel Uriel",
  "paleta": ["#FFD700", "#9B111E", "#1B1035"],
  "estetica": "gold and ruby flame, celestial cathedral clouds, angelic wings of light, cosmic violet sky, ethereal",
  "bloques": ["Rayo Oro-Rubi", "Angeles de Abundancia", "Paz y Sanacion", "Codigos Sagrados"],
  "videos": [
   ("Uriel's Gold and Ruby Flame", 528, 3, "GOLD RUBY FLAME", "gold and ruby flame rising in a cathedral of clouds"),
   ("Divine Provision Never Fails", 777, 3, "DIVINE PROVISION", "angelic hands offering a bowl of golden light"),
   ("The Angel of Wealth Is With You", 888, 3, "ANGEL OF WEALTH", "vast winged silhouette over a golden horizon"),
   ("Uriel Illuminates Your Way", 963, 8, "ILLUMINATE", "beam of light cutting through dark clouds to a path"),
   ("Receive What Heaven Sent You", 528, 3, "RECEIVE IT", "open palms catching descending golden particles"),
   ("Abundia: Goddess of the Overflowing Horn", 888, 3, "OVERFLOW", "cornucopia overflowing with golden light"),
   ("Choir of Abundance Angels", 432, 8, "ANGEL CHOIR", "ring of luminous angelic figures above clouds"),
   ("Ask, and It Is Given 777Hz", 777, 3, "ASK & RECEIVE", "prayer of light rising, answer descending in gold"),
   ("Angelic Money Blessing While You Sleep", 888, 8, "SLEEP BLESSING", "sleeping figure under a canopy of gold stars"),
   ("Signs from Your Guardian Angel", 963, 3, "SEE THE SIGNS", "feather of light falling through a sunbeam"),
   ("Peace That Money Cannot Buy", 432, 8, "DEEP PEACE", "calm violet sky over a sea of clouds"),
   ("Heal the Anxiety of Lack", 396, 3, "HEAL LACK", "grey knot in the chest dissolving into gold"),
   ("Uriel's Healing Light 528Hz", 528, 3, "HEALING LIGHT", "ruby-gold light bathing a resting figure"),
   ("Forgive and Unlock Your Flow", 417, 3, "FORGIVE", "chains falling from wrists into a river of light"),
   ("Deep Sleep Under Angel Wings", 432, 8, "ANGEL WINGS", "immense soft wings over a night landscape"),
   ("Sacred Code 71588: Money Now", 888, 2, "CODE 71588", "glowing numeric code floating over cosmic gold"),
   ("Sacred Code 897: Open Roads", 777, 2, "CODE 897", "roads of light branching across a violet sky"),
   ("11:11 Portal of Divine Wealth", 1111, 3, "11:11 PORTAL", "11:11 glowing gate in a starfield"),
   ("Manifest Before Sunrise", 963, 8, "BEFORE SUNRISE", "first light over mountains, celestial glow"),
   ("8 Hours in Uriel's Golden Field", 432, 8, "GOLDEN FIELD", "endless field of golden light under violet stars"),
  ]},
}

# FORMULA V3 - corregida con el canal de referencia real en ingles
# (Wealthy Vibes Melodies, 298k subs, EE.UU.). Sus videos con mas vistas NO
# empiezan por la frecuencia sino por la PROMESA CON URGENCIA, y la frecuencia
# va al final del titulo:
#   "PREPARE NOW! You WILL Become A Millionaire This DECEMBER!"  -> 102.014 vistas
#   "After 3 minutes, You Will Receive a Large Amount of Money"  ->  14.611 vistas
# Estructura: [GANCHO DE URGENCIA] + emoji + [NOMBRE MISTICO] + Hz + duracion.
#
# Nota: los ganadores usan ganchos mas agresivos ("WARNING VERY STRONG",
# "Money Will Transfer To You"). Aqui se usan versiones que prometen el mismo
# beneficio sin AFIRMAR que el dinero llegara, para no exponer el canal a un
# reclamo por promesa economica falsa. Estan ordenados de mas suave a mas fuerte.
GANCHOS = [
 "Money Flows To You Non-Stop After 3 Minutes",
 "Let The Universe Send You Unexpected Money",
 "Big Money Is On Its Way To You Today",
 "Receive Unexpected Money This Week",
 "Everything Starts Changing For You Today",
 "Open The Door To Sudden Abundance Tonight",
 "Your Money Blocks Dissolve In 5 Minutes",
 "Prepare Now, Your Abundance Is Arriving",
 "Wealth Is Being Attracted To You Right Now",
 "Listen Once And Watch Your Luck Change",
]

EMOJI = {396:"\u2728",417:"\U0001f501",432:"\U0001f4b0",528:"\U0001f4b0",741:"\U0001f6e1\ufe0f",
 777:"\U0001f340",888:"\U0001f4b8",963:"\U0001f52e",1111:"\U0001f6aa"}


def titulo(t, hz, hrs, n):
    """Gancho de urgencia + nombre mistico + frecuencia al final.
    YouTube corta a 100 caracteres: si no cabe se recorta el nombre mistico,
    nunca el gancho ni la frecuencia (que son lo que trae las visitas)."""
    plural = "" if hrs == 1 else "s"
    gancho = GANCHOS[(n - 1) % len(GANCHOS)]
    cola = f" \u2022 {hz} Hz \u2022 {hrs} Hour{plural}"
    cand = f"{gancho} {EMOJI[hz]} {t}{cola}"
    if len(cand) <= 100:
        return cand
    cand = f"{gancho} {EMOJI[hz]}{cola}"          # sin el nombre mistico
    return cand if len(cand) <= 100 else cand[:100]


def frecuencia(hz, hrs, slug):
    """Reasignacion con datos de la competencia en ingles: 888 Hz domina el nicho
    de dinero, seguido de 777 y 963. 432 Hz se reserva para el contenido de sueno
    (8 h), que es donde realmente rinde."""
    if hrs == 8:
        return hz                      # los de dormir conservan su frecuencia calmante
    if hz == 432:
        return 888                     # 432 no es frecuencia de dinero: la cambiamos
    if hz == 417:
        return 963 if slug == "uriel" else 777
    return hz


def duracion(hrs, n):
    """Ajuste con datos reales del nicho (analisis de canales referentes):
    los videos de 1 HORA son los que mas velocidad de vistas tienen hoy.
    Se conservan los de 8 h para la busqueda de sueno y algunos de 3 h."""
    if hrs == 8:
        return 8
    if hrs == 2:
        return 1
    return 1 if n % 2 else 3


# El video con mas vistas del canal de referencia en ingles (102.014 vistas)
# es un comodin MENSUAL: "PREPARE NOW! You WILL Become A Millionaire This DECEMBER!"
# Se repite cada mes cambiando solo el nombre del mes. Cada canal lleva el suyo.
MESES = ["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY",
         "AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]

COMODIN = {
 "lakshmi": ("PREPARE NOW! Your Wealthiest {mes} Is About To Begin", 888, 1,
             "THIS {mes}", "golden calendar page turning into a shower of light and coins"),
 "ganesha": ("PREPARE NOW! Every Door Opens For You This {mes}", 777, 1,
             "{mes} OPENS", "sunrise breaking over an opening temple gate, marigold petals"),
 "uriel":   ("PREPARE NOW! Heaven Is Sending Your Provision This {mes}", 963, 1,
             "{mes} GIFT", "angelic hand releasing a golden orb over a sea of clouds"),
}


def comodin_mensual(slug, mes):
    """Genera el video comodin del mes para un canal. Cambias el mes y ya."""
    t, hz, hrs, thumb, escena = COMODIN[slug]
    return {"titulo": t.format(mes=mes.capitalize()), "hz": hz, "horas": hrs,
            "miniatura_texto": thumb.format(mes=mes), "escena": escena}


def build():
    out = {"generado": "abundancia-canales", "canales": []}
    for slug, c in CANALES.items():
        vids = []
        for i, (t, hz, hrs, thumb, escena) in enumerate(c["videos"], 1):
            hrs = duracion(hrs, i)
            hz = frecuencia(hz, hrs, slug)
            bloque = c["bloques"][(i - 1) // 5]
            vids.append({
                "id": f"{slug}-{i:02d}",
                "n": i,
                "bloque": bloque,
                "titulo_yt": titulo(t, hz, hrs, i),
                "titulo_corto": t,
                "hz": hz,
                "horas": hrs,
                "miniatura_texto": thumb,
                "escena": escena,
                "estado": "pendiente",
            })
        # video 21: el comodin mensual (formato mas visto del nicho en ingles)
        c_mes = comodin_mensual(slug, MESES[0])
        vids.append({
            "id": f"{slug}-21", "n": 21, "bloque": "Comodin Mensual",
            "titulo_yt": f"{c_mes['titulo']} \U0001f4b8 \u2022 {c_mes['hz']} Hz \u2022 {c_mes['horas']} Hour",
            "titulo_corto": c_mes["titulo"], "hz": c_mes["hz"], "horas": c_mes["horas"],
            "miniatura_texto": c_mes["miniatura_texto"], "escena": c_mes["escena"],
            "estado": "pendiente", "nota": "Cambia el mes cada vez que lo republiques.",
        })
        out["canales"].append({
            "slug": slug, "nombre": c["nombre"], "handle": c["handle"],
            "deidad": c["deidad"], "paleta": c["paleta"], "estetica": c["estetica"],
            "bloques": c["bloques"], "videos": vids,
        })
    d = BASE / "datos"; d.mkdir(exist_ok=True)
    (d / "catalogo.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK -> datos/catalogo.json ({sum(len(c['videos']) for c in out['canales'])} videos)")

if __name__ == "__main__":
    build()
