import requests
import json
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def save_data(date):
    url = f'https://www.elprisetjustnu.se/api/v1/prices/2023/{date_today}.json'
    r = requests.get(url, allow_redirects=True)
    open(file_name_today, 'wb').write(r.content)

    f = open(file_name_today)
    lines = json.load(f)
    f.close()  

if "__main__" in __name__:
    print("Running main function")

    # data_name = '11-27_SE3'
    date_today = dt.date.today().strftime("%m-%d_SE3")
    day_today = int(dt.date.today().strftime("%d"))
    day_tomorrow = '0' + str(day_today + 1) if (day_today + 1) < 10 else str(day_today + 1)
    date_tomorrow = dt.date.today().strftime(f'%m-{day_tomorrow}_SE3')
    print(f'today: {day_today}, date_today: {date_today}, date_tomorrow: {date_tomorrow}')
    file_name_today = f'data/price/{date_today}.json'
    file_name_tomorrow = f'data/price/{date_tomorrow}.json'

    url = f'https://www.elprisetjustnu.se/api/v1/prices/2023/{date_today}.json'
    r = requests.get(url, allow_redirects=True)
    fh = open(file_name_today, 'wb')
    fh.write(r.content)
    fh.close()
 
    url = f'https://www.elprisetjustnu.se/api/v1/prices/2023/{date_tomorrow}.json'
    r = requests.get(url, allow_redirects=True)
    fh = open(file_name_tomorrow, 'wb')
    fh.write(r.content)
    fh.close()

    f = open(file_name_today)
    lines = json.load(f)
    f.close()

    f = open(file_name_tomorrow)
    lines_tomorrow = json.load(f)
    f.close()

    for line in lines_tomorrow:
        lines.append(line)
    


    print(type(lines))

    x_axis = []
    price = []
    for line in lines:
        # print(line)
        date_time = dt.datetime.fromisoformat(line["time_start"])
        print(line["time_start"])
        print(f'{date_time.strftime("%Y-%m-%d:%H")}: {line["SEK_per_kWh"]}')
        x_axis.append(date_time.strftime("%Y-%m-%d:%H"))
        price.append(line["SEK_per_kWh"])
    

    plt.plot(x_axis, price, '.-')
    plt.gcf().autofmt_xdate()
    plt.show()