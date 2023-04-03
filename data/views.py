from django.shortcuts import render

# Create your views here.
from .models import Data

def res_view(request):
    if request.method == 'POST':
        data = [i for i in Data.objects.all().values()]
        d = {}
        d['data'] = data
        name = request.POST.get('name')
        cgpa = request.POST.get('cgpa')
        gre = request.POST.get('gre')
        toefl = request.POST.get('toefl')
        country = request.POST.get('country')
        d['name'] = name
        d['cgpa'] = cgpa
        d['gre'] = gre
        d['toefl'] = toefl
        d['country'] = country
        gre_data = []
        c_data = []
        t_data = []
        cgpa_data = []
        combined_data = []
        l = []

        if country != '':
            for i in range(len(data)):
                if data[i]['country'] == country:
                    c_data.append(data[i])
            d['c_data'] = c_data

            if gre != '':
                for i in range(len(c_data)):
                    if c_data[i]['gre'] <= int(gre):
                        gre_data.append(c_data[i])
                d['gre_data'] = gre_data

            if toefl != '':
                for i in range(len(c_data)):
                    if c_data[i]['toefl'] <= int(toefl):
                        t_data.append(c_data[i])
                d['t_data'] = t_data

            for i in range(len(c_data)):
                if c_data[i]['cgpa'] <= float(cgpa):
                    cgpa_data.append(c_data[i])
            d['cgpa_data'] = cgpa_data

            for i in gre_data:
                if i not in combined_data:
                    combined_data.append(i)
            
            for i in t_data:
                if i not in combined_data:
                    combined_data.append(i)

            for i in cgpa_data:
                if i not in combined_data:
                    combined_data.append(i)

            combined_data = sorted(combined_data, key=lambda x: x['rank'])
            for i in combined_data:
                t = (i['name'],i['country'])
                l.append(t)

            if len(l) == 0:
                if gre == '':
                    d['gre'] = 'N/A'
                if country == '':
                    d['country'] = 'N/A'
                if toefl == '':
                    d['toefl'] = 'N/A'
                return render(request, 'res_other.html',d)
            elif len(l) <= 10:
                d['l'] = l
            else:
                l = l[:10]
                d['l'] = l

            d['combined_data'] = combined_data

        else:
            if gre != '':
                for i in range(len(data)):
                    if data[i]['gre'] <= int(gre):
                        gre_data.append(data[i])
                d['gre_data'] = gre_data

            if toefl != '':
                for i in range(len(data)):
                    if data[i]['toefl'] <= int(toefl):
                        t_data.append(data[i])
                d['t_data'] = t_data

            for i in range(len(data)):
                if data[i]['cgpa'] <= float(cgpa):
                    cgpa_data.append(data[i])
            d['cgpa_data'] = cgpa_data

            for i in gre_data:
                if i not in combined_data:
                    combined_data.append(i)
            
            for i in t_data:
                if i not in combined_data:
                    combined_data.append(i)

            for i in cgpa_data:
                if i not in combined_data:
                    combined_data.append(i)

            combined_data = sorted(combined_data, key=lambda x: x['rank'])
            for i in combined_data:
                t = (i['name'],i['country'])
                l.append(t)

            if len(l) == 0:
                if gre == '':
                    d['gre'] = 'N/A'
                if country == '':
                    d['country'] = 'N/A'
                if toefl == '':
                    d['toefl'] = 'N/A'
                return render(request, 'res_other.html',d)
            elif len(l) <= 10:
                d['l'] = l
            else:
                l = l[:10]
                d['l'] = l

            d['combined_data'] = combined_data


        if gre == '':
            d['gre'] = 'N/A'
        if country == '':
            d['country'] = 'N/A'
        if toefl == '':
            d['toefl'] = 'N/A'
        return render(request, 'res.html', d)
    
def index_view(request):
    return render(request, 'index.html')