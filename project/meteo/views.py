from django.http import JsonResponse
import requests
from django.shortcuts import render
from datetime import date

# Endpoint para obter a lista de cidades
CITIES_URL = 'https://api.ipma.pt/open-data/distrits-islands.json'
# Endpoint para obter a previsão meteorológica de uma cidade
FORECAST_URL = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{}.json'
# Endpoint para obter a descrição do tempo
WEATHER_TYPES_URL = 'https://api.ipma.pt/open-data/weather-type-classes.json'

def previsao(request):
    # Obter a lista de cidades
    response = requests.get(CITIES_URL)
    cities = response.json().get('data', [])
    
    return render(request, 'meteo/previsao.html', {'cities': cities})

def previsao_cidade(request, city_id):
    # Obter a descrição do tempo
    response = requests.get(FORECAST_URL.format(city_id))
    
    if response.status_code == 200:
        dic_dados = response.json()
        hoje = date.today().strftime('%Y-%m-%d')
        previsoes_proximos_dias = []
        for item in dic_dados['data']:
            if item['forecastDate'] >= hoje and len(previsoes_proximos_dias) < 5:
                # id_weather_type = "%02d" % previsao_hoje['idWeatherType']
                # weather_type_url = 'media/meteo/w_ic_d_' + str(id_weather_type) + 'anim.svg'
                previsoes_proximos_dias.append(item)

    return JsonResponse({'forecast': previsoes_proximos_dias})
   
    

def previsao_lisboa(request):
    global_id_lisboa = 1110600 
    
    response = requests.get(FORECAST_URL.format(global_id_lisboa))
    if response.status_code == 200:
        dic_dados = response.json()
        hoje = date.today().strftime('%Y-%m-%d')
        previsao_hoje = None
        for item in dic_dados['data']:
            if item['forecastDate'] == hoje:
                previsao_hoje = item
                break      

        id_weather_type = "%02d" % previsao_hoje['idWeatherType']
        weather_type_url = 'media/meteo/w_ic_d_' + str(id_weather_type) + 'anim.svg'

        contexto = {
            'previsao': previsao_hoje,
            'weather_type_url': weather_type_url,
        }
        return render(request, 'meteo/previsao_lisboa.html', contexto)
    else:
        return render(request, 'meteo/previsao_lisboa.html', {'erro': 'Não foi possível obter os dados da API.'})
