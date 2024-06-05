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
        id_weather_type = "%02d" % previsao_hoje['idWeatherType']

        weather_type_url = 'meteo/w_ic_d_' + str(id_weather_type) + 'anim.svg'

        contexto = {
            'previsao': previsao_hoje,
            'weather_type_url': weather_type_url,
        }
        return render(request, 'meteo/previsao_lisboa.html', contexto)
    else:
        return render(request, 'meteo/previsao_lisboa.html', {'erro': 'Não foi possível obter os dados da API.'})
