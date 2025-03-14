"""
bu bir hava durumu gösterme uygulamasıdır.
önce kullanıcıdan şehir ve ilçe bilgisi alınacaktır.
daha sonra verilerimizden şehirdeki hava durumu ekrana gösterilecektir.
openweathermap'ten hava durumu verileri alınmıştır.
"""

import requests

def hava_durumu():
    city = input("Şehir adı giriniz: ")
    district = input("İlçe adı giriniz: ")

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "c48f49f6f76c53fe7e7df29d6afa6b8c"
    full_url = base_url + "q=" + district + "," + city + "&appid=" + api_key + "&units=metric&lang=tr"

    response = requests.get(full_url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"{city} ({district})'de hava durumu: {description}, sıcaklık: {temperature}°C")
        print(f"Nem oranı: {humidity}%")
        print(f"Rüzgar hızı: {wind_speed} m/s")
    else:
        print("Hava durumu verisi alınamadı.")

hava_durumu()
