import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

duration = 5  # kayıt saniyeleri
sample_rate = 44100

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
    text = recognizer.recognize_google(audio, language="tr")
    print("Şunu söylediniz:", text)
except sr.UnknownValueError:             # - Google gürültü veya sessizlik nedeniyle konuşmayı anlayamadığında
    print("Konuşma tanınamadı.")
except sr.RequestError as e:             # - İnternet bağlantısı yoksa veya API kullanılamıyorsa
    print(f"Hizmet hatası: {e}")

language = input("Hangi dile çevirmek istersiniz? (örneğin 'es' İspanyolca, 'ru' rusca,'en' english, 'tr' türkce için): ")
# Dil kodlarını ve adlarını eşleştiren dictionary
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
translator = Translator()
translated = translator.translate(text, dest=language)
language_name = language_codes.get(language, language.upper())
print(f"🌍 {language_name}'ye çeviri:", translated.text)

