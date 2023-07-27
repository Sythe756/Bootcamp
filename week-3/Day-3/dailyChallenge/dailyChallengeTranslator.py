from googletrans import Translator

def translate_words(words_list):
    translator = Translator()
    translated_words = {}

    for word in words_list:
        translation = translator.translate(word, src="fr", dest="en").text
        translated_words[word] = translation

    return translated_words

if __name__ == "__main__":
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    translated_words = translate_words(french_words)

    print(translated_words)
