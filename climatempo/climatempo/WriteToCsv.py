#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from climatempo import settings


def write_to_csv(item):
    try:
        with open(settings.csv_file_path) as csvfile:
            rows = len(list(csv.reader(csvfile)))
    except:
        rows = 0
    if rows < 100:
        writer = csv.writer(open(settings.csv_file_path, 'a'),
                            lineterminator='\n')
        writer.writerow(item)

class WriteToCsv(object):
    def process_item(self, item, spider):
        for key in item:
            table = item[key]
            minima = min([float(temp.strip('°')) for temp in table[1::4]])
            maxima = max([float(temp.strip('°')) for temp in table[2::4]])
            precipitacao = sum([float(temp) for temp in table[3::4]])
            write_to_csv([key, minima, maxima, precipitacao])
        return item
