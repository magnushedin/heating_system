import requests
import json
import time
import datetime
import matplotlib.pyplot as plt

if "__main__" in __name__:
    print("Running main function")

    data_name = '11-27_SE3'
    file_name = f'data/price/{data_name}.json'

    url = f'https://www.elprisetjustnu.se/api/v1/prices/2023/{data_name}.json'
    r = requests.get(url, allow_redirects=True)
    open(file_name, 'wb').write(r.content)

    f = open(file_name)
    lines = json.load(f)
    f.close()


    hour = []
    price = []
    for line in lines:
        # print(line)
        dt = datetime.datetime.fromisoformat(line["time_start"])
        print(line["time_start"])
        print(f'{dt.strftime("%H")}: {line["SEK_per_kWh"]}')
        hour.append(int(dt.strftime("%H")))
        price.append(line["SEK_per_kWh"])
    

    plt.plot(hour, price, '.-')
    plt.show()