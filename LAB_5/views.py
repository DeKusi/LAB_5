from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    return HttpResponse("Hello, world!")


def indexRender(request):
    return render(request, 'index.html', {})


with open("json_data1.json", 'rb') as read_file_json:
    data = json.load(read_file_json)
    Name = data['Name']
    Rector_name = data['Rector']['Name']
    Rector_surname = data['Rector']['Surname']
    Location_index = data['Location']['index']
    Location_city = data['Location']['city']
    Location_address = data['Location']['address']
    num_administrative = len(data['Subdivision']['Administrative'])
    num_educational = len(data['Subdivision']['Educational'])
    num_faculty = len(data['Subdivision']['Educational'][0]['Faculty'])

    Num_programm = data['Subdivision']['Educational'][0]['Faculty'][0]['Programs'][0]['Num']
    Name_programm = data['Subdivision']['Educational'][0]['Faculty'][0]['Programs'][0]['Name']
    Discipline = data['Subdivision']['Educational'][0]['Faculty'][0]['Programs'][0]['discipline']
    Year = data['Subdivision']['Educational'][0]['Faculty'][0]['Programs'][0]['Year']['year']
    am_group = len(data['Subdivision']['Educational'][0]['Faculty'][0]['Programs'][0]['Year']['groups'])

dict_ITMO = {'Name': Name,
             'Rector': [Rector_name, Rector_surname],
             'Location': {'index': Location_index, 'city': Location_city, 'address': Location_address},
             'num_administrative': num_administrative,
             'num_educational': num_educational,
             'num_faculty': num_faculty
             }
dict_discipline = {'Num_programm': Num_programm,
                   'Name_programm': Name_programm,
                   'Discipline': Discipline,
                   'Year': Year,
                   'am_group': am_group
                   }


def universityInfo(request):
    return render(request, 'universityInfo.html', dict_ITMO)


def disciplineInfo(request):
    return render(request, 'disciplineInfo.html', dict_discipline)
