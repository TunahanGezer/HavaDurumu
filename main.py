import requests
import json

# Bunlara başlamadan önce terminaldan 'pip install requests' komutunu çalıştırıp import etmemiz gerekiyor

# OpenWeatherMap API anahtarını alıp buraya gireceğiz
api_key = "956c213ba9310bbec22c6ea65c45a8cc"

# Hava durumunu almak istediğiniz şehrin ismini giriyoruz
city_name = input("Şehir adını girin: ")

# İnternet sitesinden bilgileri aldık
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
response = requests.get(url)

# Hava durumunda ki ingilizce terimleri türkceye ceviriyoruz
desc_sozluk = {
    "clear sky": "Açık",
    "few clouds": "Az bulutlu",
    "scattered clouds": "Parçalı bulutlu",
    "broken clouds": "Bulutlu",
    "overcast clouds": "Kapalı",
    "mist": "Sisli",
    "light rain": "Hafif yağmurlu",
    "moderate rain": "Orta şiddetli yağmurlu",
    "heavy intensity rain": "Şiddetli yağmurlu",
    "very heavy rain": "Çok şiddetli yağmurlu",
    "extreme rain": "Şiddetli yağmurlu",
    "freezing rain": "Dondurucu yağmurlu",
    "light snow": "Hafif kar yağışlı",
    "heavy snow": "Yoğun kar yağışlı",
    "sleet": "Sulu kar",
    "shower rain": "Sağanak yağmurlu",
    "thunderstorm": "Gök gürültülü fırtınalı",
    "haze": "Puslu"
}
# Gelen Verileri işliyoruz
data = response.json()
temperature = data["main"]["temp"]
description_eng = data["weather"][0]["description"]
description_tr = desc_sozluk.get(description_eng, "Atama")

# Hava durumu bilgisini ekrana yazdırın
print(f"{city_name} şehrinin hava durumu: {description_tr}; Sıcaklık: {temperature}°C")


