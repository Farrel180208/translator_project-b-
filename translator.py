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

