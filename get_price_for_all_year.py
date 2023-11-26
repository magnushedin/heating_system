import requests
import json
import time
import datetime
import matplotlib.pyplot as plt
import calendar

if "__main__" in __name__:
    print("Running main function")

    year = 2023
    for month in range(1, 10):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            if month < 10:
                month_txt = f'0{month}'
            else:
                month_txt = str(month)
            if day < 10:
                day_txt = f'0{day}'
            else:
                day_txt = str(day)

            print(f'Month: {month_txt}, reading day: {day_txt}')
            data_name = f'{month_txt}-{day_txt}_SE3'
            file_name = f'data/price/{data_name}.json'

            url = f'https://www.elprisetjustnu.se/api/v1/prices/2023/{data_name}.json'
            r = requests.get(url, allow_redirects=True)
            open(file_name, 'wb').write(r.content)
