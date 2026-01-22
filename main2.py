import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
duration = 5  # kayıt saniyeleri
sample_rate = 44100
language_codes = {
    'es': 'İspanyolca',
    'ru': 'Rusça',
    'en': 'İngilizce',
    'tr': 'Türkçe',
    'fr': 'Fransızca',
    'de': 'Almanca',
    'it': 'İtalyanca',
    'pt': 'Portekizce',
    'ja': 'Japonca',
    'zh-cn': 'Çince'
}
kelime_listesi = {
    "kolay": [
        {"tr": "Elma", "en": "Apple"},
        {"tr": "Kedi", "en": "Cat"},
        {"tr": "Su", "en": "Water"},
        {"tr": "Masa", "en": "Table"},
        {"tr": "Mavi", "en": "Blue"},
        {"tr": "Kapı", "en": "Door"},
        {"tr": "Süt", "en": "Milk"},
        {"tr": "Mutlu", "en": "Happy"},
        {"tr": "Kitap", "en": "Book"},
        {"tr": "Okul", "en": "School"}
    ],
    "orta": [
        {"tr": "Bahçe", "en": "Garden"},
        {"tr": "Hava Durumu", "en": "Weather"},
        {"tr": "Macera", "en": "Adventure"},
        {"tr": "Tehlikeli", "en": "Dangerous"},
        {"tr": "Yarın", "en": "Tomorrow"},
        {"tr": "Kütüphane", "en": "Library"},
        {"tr": "Sincap", "en": "Squirrel"},
        {"tr": "Başarılı", "en": "Successful"},
        {"tr": "Çarşamba", "en": "Wednesday"},
        {"tr": "Dil", "en": "Language"}
    ],
    "zor": [
        {"tr": "Albay", "en": "Colonel"},
        {"tr": "Kuyruk", "en": "Queue"},
        {"tr": "Vicdan", "en": "Conscience"},
        {"tr": "Kaos", "en": "Chaos"},
        {"tr": "Program", "en": "Schedule"},
        {"tr": "Girişimci", "en": "Entrepreneur"},
        {"tr": "Psikoloji", "en": "Psychology"},
        {"tr": "Koro", "en": "Choir"},
        {"tr": "Kapsamlı", "en": "Thorough"},
        {"tr": "Hiyerarşi", "en": "Hierarchy"}
    ]
}
puan = 0,
def zorluk_secimi(zorluk): 
        zorluk = input("Zorluk seviyesini yazın: ").lower().strip()
        if zorluk in kelime_listesi:
            return zorluk
        else:
            print("Hatalı giriş! Lütfen 'kolay', 'orta' veya 'zor' yazın.")

while True:
    zorluk_secimi()
    secilen_veri = random.choice(kelime_listesi[zorluk])
    print(f"bu kelimenin ingilizcesini telafuz ediniz: {secilen_veri['tr']} ")
    print("Şimdi konuşun...")
    recording = sd.rec(
    int(duration * sample_rate), # kaydedilecek örnek sayısı
    samplerate=sample_rate,      # örnekleme hızı
    channels=1,                  # 1, mono kayıt anlamına gelir.
    dtype="int16")               # kayıtlı örnekler için veri türü
    sd.wait()  # kayıt bitene kadar beklemek

    wav.write("output.wav", sample_rate, recording)
    print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="en")
    except sr.UnknownValueError:             # - Google gürültü veya sessizlik nedeniyle konuşmayı anlayamadığında
        print("Konuşma tanınamadı.")
    except sr.RequestError as e:             # - İnternet bağlantısı yoksa veya API kullanılamıyorsa
        print(f"Hizmet hatası: {e}")
    if text.lower() == secilen_veri['en'].lower():
        print("Tebrikler! Doğru telaffuz ettiniz:", text)
        puan += 10

    else:
        print(f"Yanlış telaffuz. Doğru cevap: {secilen_veri['en']}, Sizinki: {text}")
    karar=input("Devam etmek istiyor musunuz? (e/h): ").lower()
    if karar !='e':
        print(f"Toplam puanınız: {puan}")
        break
    else:
        continue
    # Dil kodlarını ve adlarını eşleştiren dictionary
