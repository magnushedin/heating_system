import requests
import json
import time
import datetime
import matplotlib.pyplot as plt
import os

if "__main__" in __name__:
    print("Running main function")

    all_year = []

    plt.figure()

    for file_name in os.listdir('data/price'):

        file_name = f'data/price/{file_name}'
        print(f'Working on file: {file_name}')

        f = open(file_name)
        lines = json.load(f)
        f.close()


        hour = []
        price = []
        for line in lines:
            # print(line)
            dt = datetime.datetime.fromisoformat(line["time_start"])
            # print(f'{dt.strftime("%H")}: {line["SEK_per_kWh"]}')
            hour.append(int(dt.strftime("%H")))
            price.append(line["SEK_per_kWh"])
            all_year.append(line["SEK_per_kWh"])
        

        plt.plot(hour, price, '.-')

    plt.figure()
    plt.plot(all_year, '.-')
    plt.show()