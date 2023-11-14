# translator_project-b-

# step 1
mula mula pergi ke vscode buat folder bernama project_uas
lalu disana kita membuat file translator.py
masukkan kode translator.py dengan cara mengcopy kodenya dari repository github saya
dalam repository saya terpampang jelas ada file bernama translator.py (third commit); salin saja semua kodenya dengan mengklik icon copy
jangan lupa ctrl + s atau save setelah memasukkan kode ke file di vs code
lalu install beberapa aplikasi menggunakan pip di bash ataupun terminal folder project_uas seperti dibawah ini
pip install Flask
pip install googletrans==4.0.0-rc1

# step 2
buat folder baru pertama di folder project_uas :
folder baru pertama : static (ada direpository github saya, klik untuk bisa mengetahui file-file didalamnya)
setelah itu masukan 2 file yaitu dibawah ini:
file pertama : background.avif (di view raw klik saja nanti muncul gambar lalu save as ke folder static)
file kedua : style.css (copy semua codenya melalui ikon copy)
lalu masukkan kode atau gambar yang telah saya upload di repository saya ke masing-masing file tersebut dan jangan lupa save atau ctrl+s

# step 3
buat folder baru kedua di folder project_uas 
folder baru kedua : templates (ada di repository github saya klik saja untuk mengetahui file-file didalamnya)
setelah itu masukan 3 file yaitu dibawah ini:
file pertama : index.html (klik filenya lalu copy semua code menggunakan ikon copy)
file kedua : history.html (klik filenya lalu copy semua code menggunakan ikon copy)
file ketiga : result.html (klik filenya lalu copy semua code menggunakan ikon copy)
lalu masukkan kode yang telah saya upload di repository saya ke masing-masing file tersebut di vs code dan jangan lupa save atau ctrl+s

# step 4
di step ini anda harus open integrated terminal dari folder project_uas
lalu ketikan di terminal py translator.py
anda akan disajikan output berupa link seperti dibawah ini:
 * Serving Flask app 'translator'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 122-621-969

anda harus mengklik link diatas yaitu : http://127.0.0.1:5000
atau anda juga bisa mengcopynya lalu menyalinnya di url chrome

# step 5
untuk mencoba pemfungsian program ini anda hanya tinggal memasukkan kalimat bahasa indonesia seperti "aku suka melon" lalu centang bagian kotak (en,de,zh-CN,es,fr,ar,pt,ja)
lalu ia akan memberikan out put hasil terjemahan seperti dibawah ini:

Hasil Terjemahan

Original Text: aku suka melon

    Terjemahan Bahasa Indonesia ke Bahasa Inggris: I like melons
    Terjemahan Bahasa Indonesia ke Bahasa Jerman: Ich mag Melonen
    Terjemahan Bahasa Indonesia ke Bahasa Cina (Mandarin): 我喜欢瓜
    Terjemahan Bahasa Indonesia ke Bahasa Spanyol: Me gustan los melones
    Terjemahan Bahasa Indonesia ke Bahasa Prancis: J'aime les melons
    Terjemahan Bahasa Indonesia ke Bahasa Arab: أنا أحب البطيخ
    Terjemahan Bahasa Indonesia ke Bahasa Portugis: Eu gosto de melões
    Terjemahan Bahasa Indonesia ke Bahasa Jepang: 私はメロンが好きです

note : mungkin terjadi lagging beberapa saat karena ada kemungkin progam terlalu banyak searching google translate dahulu dari 8 bahasa ini sebelum dijalankan.

*sekian dan terimakasih*
