![doctoralia_logo](climatempo.png)

#  Scrappying climatempo.com.br/climatologia/ using scrapy
## Installing scrapy
This code is written on Python 3.6 and uses [scrapy 1.4.0](https://scrapy.org/).

You should install scrapy with pip:
```pip install --user scrapy```

**Note**: on my system, ```python``` points to ```python3.6``` and ```pip``` points to ```pip3```, you should check yours before running.

This spider starts from http://www.doctoralia.com.br/medicos, and goes to the next pages until reach 500 occurrences.

## Usage
To run this spider, open the terminal on this repository, then type:
```
cd climatempo
scrapy crawl climatologia
```

Your csv file with the scrapped data should be on climatologia-clima-tempo/climatempo/climatologia.csv

## Further observations
- This spider was designed for getting only the 100 first occurences, thus it will not scrap the entire web site;
- I have only attached instructions for running this spider localy but we could also use scrapinghub's cloud, which has excellent tools for debugging, and data checking;
- The csv structure should be: 

              ``` <City>, <Minimum temperature>,  <Maximum temperature>, <Accumulated precipitation> ```

where fields are:

| Field | Content and Type |
| ---  | --- |
| City | string with the name of the respective city |
| Minimum temperature | float with the minimum temperature over one year |
| Maximum temperature | float with the maximum temperature over one year |
| Accumulated precipitation | float with the accumulated precipitation over one year |

## Notes on the scraper architecture
- This website relies on java script for changing cities and we cannot navigate on it entirely with scrapy. 
- I usualy use (splash)[https://splash.readthedocs.io/en/stable/] along with scrapy for rendering the java script. However this particularly website makes a lot of requests for its api which makes it is dificult to countour with (scrapy-splash)[https://github.com/scrapy-plugins/scrapy-splash].
- One option was to use (Selenium)[www.seleniumhq.org] which I didn't because it does not work properlly with the scrapy's parallel processing;
- Since I could get acces to climatempo's (api)[http://apiadvisor.climatempo.com.br/], I downloaded a list of cities for the State of São Paulo, which are in the climatempo/cities.json file;
- I did not attach the code for requesting the list of cities because it requires an api token, wich would complicate the reproduction of this code. Hence I lefted the list of cities hardcoded in the climatempo/cities.json file;


![Scrapy-Logo](Scrapy-Logo-Horizontal.png)
