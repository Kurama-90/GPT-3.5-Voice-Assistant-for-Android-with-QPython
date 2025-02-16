# Kurama-90 (https://github.com/Kurama-90)

import androidhelper  # Pour les fonctionnalités Android
from apigptcloud import openai  # Pour appeler l'API GPT
import time  # Pour la gestion d'inactivité

# Configuration de l'API GPT
openai.api_key = "your API KEY"
openai.api_base = "https://openai.pgpt.cloud/v1"

# Initialisation des messages avec une instruction pour toujours répondre en français
messages = [
    {"role": "system", "content": "Vous êtes un assistant utile et vous répondez toujours en français."}
]

# Initialiser androidhelper
droid = androidhelper.Android()

print("Assistant GPT : Bonjour Kurama-90 ! Posez-moi une question.")
droid.ttsSpeak("Bonjour Kurama-90 ! Posez-moi une question.")

# Fonction pour diviser les longues réponses en segments pour la synthèse vocale
def speak_text(text):
    max_length = 200  # Limiter la taille du segment
    for i in range(0, len(text), max_length):
        segment = text[i:i + max_length]
        droid.ttsSpeak(segment)

# Fonction pour gérer la reconnaissance vocale
def get_voice_input():
    try:
        result = droid.recognizeSpeech("Parlez maintenant").result
        return result if result else "Je n'ai pas compris."
    except Exception:
        return "Je n'ai pas compris."

# Initialisation du timer pour la gestion de l'inactivité
last_interaction = time.time()

try:
    # Boucle principale
    while True:
        # Vérifier l'inactivité (5 minutes)
        if time.time() - last_interaction > 300:
            print("Assistant GPT : Êtes-vous toujours là ?")
            droid.ttsSpeak("Êtes-vous toujours là ?")
            last_interaction = time.time()
       
        # Demander une entrée utilisateur (texte ou vocale)
        user_input = input("Vous (tapez 'parler' pour utiliser la voix) : ")
        if user_input.lower() in ["exit", "quit"]:
            print("Assistant GPT : Au revoir !")
            droid.ttsSpeak("Au revoir Mohamed !")
            break
       
        if user_input.lower() == "parler":
            user_input = get_voice_input()

        # Ajouter la question de l'utilisateur à l'historique des messages
        messages.append({"role": "user", "content": user_input})

        # Appeler l'API GPT
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=1,
            )

            # Extraire la réponse
            assistant_reply = res['choices'][0]['message']['content']
            print(f"Assistant GPT : {assistant_reply}")

            # Synthèse vocale
            speak_text(assistant_reply)

            # Ajouter à l'historique
            messages.append({"role": "assistant", "content": assistant_reply})

            # Mise à jour du dernier moment d'interaction
            last_interaction = time.time()

        except Exception as e:
            print(f"Erreur : {e}")
            droid.ttsSpeak("Désolé, une erreur est survenue.")

except KeyboardInterrupt:
    print("\nAssistant GPT : Arrêt détecté, au revoir !")
    droid.ttsSpeak("Arrêt détecté, au revoir !")

finally:
    # Arrêter la synthèse vocale si elle est en cours
    droid.ttsStop()
