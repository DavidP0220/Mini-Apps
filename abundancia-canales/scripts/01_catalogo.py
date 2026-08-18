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

# Formato de titulo probado: NOMBRE + emoji + BENEFICIO + frecuencia + duracion
GANCHO = {
 396: "{t} \u2728 Release Fear & Dissolve the Roots of Scarcity \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
 417: "{t} \U0001f501 Clear Old Money Patterns & Reset Your Luck \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
 432: "{t} \U0001f331 Deep Calm, Blessings & Abundance While You Sleep \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
 528: "{t} \U0001f4b0 Activate Miracles & Heart-Centered Wealth \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
 741: "{t} \U0001f6e1\ufe0f Cleanse Envy, Evil Eye & Negative Energy \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
 777: "{t} \U0001f340 Open Divine Luck & Unexpected Doors \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
 888: "{t} \U0001f4b8 Awaken Financial Magnetism & Non-Stop Money Flow \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
 963: "{t} \U0001f52e Connect With Divine Wisdom & Higher Guidance \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
 1111:"{t} \U0001f6aa Enter the Manifestation Portal & Seal Your Intention \u2022 {hz} Hz \u2022 {hrs} Hour{plural}",
}

CORTO = {396:"Release Fear & Scarcity",417:"Reset Your Luck",432:"Deep Calm & Blessings",
 528:"Miracles & Wealth",741:"Cleanse Negative Energy",777:"Open Divine Luck",
 888:"Non-Stop Money Flow",963:"Divine Wisdom",1111:"Manifestation Portal"}
EMOJI = {396:"\u2728",417:"\U0001f501",432:"\U0001f331",528:"\U0001f4b0",741:"\U0001f6e1\ufe0f",
 777:"\U0001f340",888:"\U0001f4b8",963:"\U0001f52e",1111:"\U0001f6aa"}

def titulo(t, hz, hrs):
    plural = "" if hrs == 1 else "s"
    """YouTube corta a 100 caracteres: si el titulo largo se pasa, usa el beneficio corto."""
    largo = GANCHO[hz].format(t=t, hz=hz, hrs=hrs, plural=plural)
    if len(largo) <= 100:
        return largo
    corto = f"{t} {EMOJI[hz]} {CORTO[hz]} \u2022 {hz} Hz \u2022 {hrs} Hour{plural}"
    return corto if len(corto) <= 100 else f"{t} {EMOJI[hz]} {hz} Hz \u2022 {hrs} Hour{plural}"[:100]

def duracion(hrs, n):
    """Ajuste con datos reales del nicho (analisis de canales referentes):
    los videos de 1 HORA son los que mas velocidad de vistas tienen hoy.
    Se conservan los de 8 h para la busqueda de sueno y algunos de 3 h."""
    if hrs == 8:
        return 8
    if hrs == 2:
        return 1
    return 1 if n % 2 else 3


def build():
    out = {"generado": "abundancia-canales", "canales": []}
    for slug, c in CANALES.items():
        vids = []
        for i, (t, hz, hrs, thumb, escena) in enumerate(c["videos"], 1):
            hrs = duracion(hrs, i)
            bloque = c["bloques"][(i - 1) // 5]
            vids.append({
                "id": f"{slug}-{i:02d}",
                "n": i,
                "bloque": bloque,
                "titulo_yt": titulo(t, hz, hrs),
                "titulo_corto": t,
                "hz": hz,
                "horas": hrs,
                "miniatura_texto": thumb,
                "escena": escena,
                "estado": "pendiente",
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
