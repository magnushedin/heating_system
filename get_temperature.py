import requests
import json
import time
import datetime
import matplotlib.pyplot as plt

if "__main__" in __name__:
    print("Running main function")

    data_name = 'temperature'
    file_name = f'data/temp/{data_name}.json'

    url = 'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/11.86/lat/57.71/data,json'
    r = requests.get(url, allow_redirects=True)
    open(file_name, 'wb').write(r.content)

    f = open(file_name)
    json_dict = json.load(f)
    f.close()

    # print(json_dict['timeSeries'])
    for key in json_dict.keys():
        print(key)

    date = "2023-11-25"
    date = datetime.date.today()
    # Use this to select which day to display

    hour = []
    temperature = []
    for item in json_dict['timeSeries']:
        # print(f'{item["validTime"]}')
        for param in item["parameters"]:
            if param["name"] == "t":
                print(f'{item["validTime"]}: {param["name"]}: {param["values"]}')
                isoTime = (item["validTime"]).replace("Z", "")
                dt = datetime.datetime.fromisoformat(isoTime)
                print(f'{dt.strftime("%H")}: {param["values"][0]}')
                hour.append(int(dt.strftime("%H")))
                temperature.append(param["values"][0])
            # if vindhastighet
            # if regn (nederbörd)
            # if molnighet (total cloud cover)

    # plt.plot(hour, temperature, '.-')
    plt.plot(temperature, '.-')
    plt.show()