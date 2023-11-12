from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

translator = Translator()
translation_history = []

@app.route('/')
def index():
    lang_destinations = {
        '1': 'en',
        '2': 'de',
        '3': 'zh-CN',
        '4': 'es',
        '5': 'fr',
        '6': 'ar',
        '7': 'pt',
        '8': 'ja',
    }

    lang_descriptions = {
        'en': 'Inggris',
        'de': 'Jerman',
        'zh-CN': 'Cina (Mandarin)',
        'es': 'Spanyol',
        'fr': 'Prancis',
        'ar': 'Arab',
        'pt': 'Portugis',
        'ja': 'Jepang',
    }

    return render_template('index.html', lang_destinations=lang_destinations, lang_descriptions=lang_descriptions)

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    
    lang_destinations = {
        '1': 'en',
        '2': 'de',
        '3': 'zh-CN',
        '4': 'es',
        '5': 'fr',
        '6': 'ar',
        '7': 'pt',
        '8': 'ja',
    }

    lang_descriptions = {
        'en': 'Inggris',
        'de': 'Jerman',
        'zh-CN': 'Cina (Mandarin)',
        'es': 'Spanyol',
        'fr': 'Prancis',
        'ar': 'Arab',
        'pt': 'Portugis',
        'ja': 'Jepang',
    }

    destination_choices = request.form.getlist('destination')
    translations = []

    for choice in destination_choices:
        if choice not in lang_destinations:
            return render_template('error.html', message=f"Pilihan bahasa tujuan '{choice}' tidak valid. Silakan coba lagi.")

        dest_lang = lang_destinations[choice]
        translated_text = translator.translate(text, src='id', dest=dest_lang)
        translations.append((dest_lang, translated_text.text))

        # Tambahkan terjemahan ke riwayat
        translation_history.append((text, translated_text.text, dest_lang))

    # Tambahkan terjemahan ke bahasa Inggris jika dipilih
    if 'en' in destination_choices:
        english_translation = translator.translate(text, src='id', dest='en')
        translations.append(('en', english_translation.text))
        translation_history.append((text, english_translation.text, 'en'))

    return render_template('result.html', text=text, translations=translations, lang_descriptions=lang_descriptions)

@app.route('/history')
def history():
    return render_template('history.html', translation_history=translation_history)

if __name__ == "__main__":
    app.run(debug=True)
