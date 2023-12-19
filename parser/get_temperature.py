import requests
import json
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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
    date = dt.date.today()
    # Use this to select which day to display

    hour = []
    temperature = []
    for item in json_dict['timeSeries']:
        # print(f'{item["validTime"]}')
        for param in item["parameters"]:
            if param["name"] == "t":
                print(f'{item["validTime"]}: {param["name"]}: {param["values"]}')
                isoTime = (item["validTime"]).replace("Z", "")
                date_time = dt.datetime.fromisoformat(isoTime)
                print(f'{date_time.strftime("%Y-%m-%d:%H")}: {param["values"][0]}')
                # hour.append(date_time.strftime("%Y-%m-%d:%H"))
                hour.append(date_time)
                temperature.append(param["values"][0])
            # if vindhastighet
            # if regn (nederbörd)
            # if molnighet (total cloud cover)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d (%H.00)'))
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour=[7,19]))
    # x_axis = [mdates.date2num(h) for h in hour]
    plt.plot(hour, temperature, '.-')
    plt.grid()
    plt.gcf().autofmt_xdate()
    plt.show()