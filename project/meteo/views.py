import requests
from django.shortcuts import render
from datetime import date

def previsao_lisboa(request):
    global_id_lisboa = 1110600 
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{global_id_lisboa}.json'
    
    response = requests.get(url)
    if response.status_code == 200:
        dic_dados = response.json()
        hoje = date.today().strftime('%Y-%m-%d')
        previsao_hoje = next((item for item in dic_dados['data'] if item['forecastDate'] == hoje), None)
        id_weather_type = previsao_hoje['idWeatherType']

        contexto = {
            'previsao': previsao_hoje,
            'id_weather_type': id_weather_type,
        }
        return render(request, 'meteo/previsao_lisboa.html', contexto)
    else:
        return render(request, 'meteo/previsao_lisboa.html', {'erro': 'Não foi possível obter os dados da API.'})
