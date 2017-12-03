![doctoralia_logo](climatempo.png)

#  Scrappying climatempo.com.br/climatologia/* using scrapy

---
## Installing scrapy
This code was written in Python 3.6 and uses [scrapy 1.4.0](https://scrapy.org/).

You should install scrapy with pip:
```pip install --user scrapy```

**Note**: on my system, python points to python3.6 and pip points to pip3, you should check your defaults before running it.

# Usage
To run this spider, open the terminal on this repository, then type:
```
cd climatempo
scrapy crawl climatologia
```

Your csv file with the scrapped data should be on doctoralia.com/doctoralia/doctoralia_data.csv

![Scrapy-Logo](Scrapy-Logo-Horizontal.png)
