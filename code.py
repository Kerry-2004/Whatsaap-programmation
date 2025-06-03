import pywhatkit
import time

# Liste de numéros (format international)
numeros = [
    "+50937089658",
    "+50942669288",
]

# Message à envoyer
message = "Ou jwenn li"

# Heure de départ
heure = 15
minute = 15

# Boucle sur chaque numéro
for numero in numeros:
    try:
        pywhatkit.sendwhatmsg(numero, message, heure, minute)
        print(f"✅ Message envoyé à {numero} à {heure}:{minute:02d}")
        
        # Incrémenter l'heure pour éviter les conflits
        minute += 2
        if minute >= 60:
            minute = 0
            heure += 1
            
        # Attendre quelques secondes pour que le message soit envoyé avant le suivant
        time.sleep(20)  # Tu peux réduire si ton ordi est rapide

    except Exception as e:
        print(f"❌ Erreur avec {numero} : {e}")
