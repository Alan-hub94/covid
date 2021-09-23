from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "24ab7d1635msh2b38fd6c051e573p18d882jsn7c9c2e5cde43"
    }

response = requests.request("GET", url, headers=headers).json()
response = response["response"]

countries = [dato['country'] for dato in response ] # Lista por compresion
#for r in response:
#    countries.append(r['country'])
countries.sort()

def home(request):
    if request.method=='POST':
        pais = request.POST['selectedcountry']
        for i in response:
            if pais == i['country']:
                new = i['cases']['new'] if i['cases']['new'] else '0'
                active = i['cases']['active'] if i['cases']['active'] else '0'
                critical = i['cases']['critical'] if i['cases']['critical'] else '0'
                recovered = i['cases']['recovered'] if i['cases']['recovered'] else '0'
                total = i['cases']['total'] if i['cases']['total'] else '0'
                deaths = int(total) - int(active) - int(recovered)
        contex = {
            'new':new,
            'active':active,
            'critical':critical,
            'recovered':recovered,
            'total':total,
            'deaths':deaths,
            'pais':pais,
            'countries':countries
        }
        return render(request, 'core/index.html', context=contex)
    return render(request, 'core/index.html', {'countries': countries })