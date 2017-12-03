# -*- coding: utf-8 -*-
import json
from unicodedata import normalize

def removeAccents(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def gen_start_urls():
    with open('cities.json') as data_file:
        config_json = json.load(data_file)['data']

    cities = list()

    url_base = 'https://www.climatempo.com.br/climatologia'
    for city in config_json:
        cities.append('{}/{}/{}-{}'.format(url_base, city['idcity'],
                                           city['city'].lower(),
                                           city['uf'].lower()))

        cities[-1] = removeAccents(cities[-1])
    return cities

