import requests
import json
import time
import datetime as dt

def save_data(date):
    url = f'https://www.elprisetjustnu.se/api/v1/prices/2023/{date_today}.json'
    r = requests.get(url, allow_redirects=True)
    open(file_name_today, 'wb').write(r.content)

    f = open(file_name_today)
    lines = json.load(f)
    f.close()

if "__main__" in __name__:
    a = True
    while a:
        a = False
        print("Running main function")

        # data_name = '11-27_SE3'
        date_today = dt.date.today().strftime("%m-%d_SE3")
        day_today = int(dt.date.today().strftime("%d"))
        day_tomorrow = '0' + str(day_today + 1) if (day_today + 1) < 10 else str(day_today + 1)
        date_tomorrow = dt.date.today().strftime(f'%m-{day_tomorrow}_SE3')
        print(f'today: {day_today}, date_today: {date_today}, date_tomorrow: {date_tomorrow}')
        file_name_today = f'../data/price/{date_today}.json'
        file_name_tomorrow = f'../data/price/{date_tomorrow}.json'

        url = f'https://www.elprisetjustnu.se/api/v1/prices/2023/{date_today}.json'
        r = requests.get(url, allow_redirects=True)
        fh = open(file_name_today, 'wb')
        fh.write(r.content)
        fh.close()

        f = open(file_name_today)
        lines = json.load(f)
        f.close()

        try:
            url = f'https://www.elprisetjustnu.se/api/v1/prices/2023/{date_tomorrow}.json'
            r = requests.get(url, allow_redirects=True)
            fh = open(file_name_tomorrow, 'wb')
            fh.write(r.content)
            fh.close()

            f = open(file_name_tomorrow)
            lines_tomorrow = json.load(f)
            f.close()

            for line in lines_tomorrow:
                lines.append(line)
        except:
            print(f'Tomorrow is not yet available ({file_name_tomorrow})')


        print(type(lines))

        x_axis = []
        price = []
        js = []
        for line in lines:
            # print(line)
            date_time = dt.datetime.fromisoformat(line["time_start"])
            print(line["time_start"])
            print(f'{date_time.strftime("%Y-%m-%d:%H")}: {line["SEK_per_kWh"]}')
            # x_axis.append(mdates.date2num(date_time))
            x_axis.append(date_time)
            price.append(line["SEK_per_kWh"])
            js.append((date_time, line["SEK_per_kWh"]))

        f_js = open('../server/src/datamodule.js', 'w')
        f_js.write('''import moment from 'moment'
const data = [
''')
        for (x, y) in js:
            f_js.write(f"   {{time: moment('{x}', moment.ISO_8601), count: {y}}},\n")

        f_js.write('''];

module.exports = {
    get_data: function() {
        return data;
    },
    get_data_name: function() {
        return "Electrical price";
    },
''')
        f_js.write(f'get_update_time: function() {{\n\t\treturn \"{dt.datetime.today().strftime("%Y-%m-%d %H.%M.%S")}\";\n\t}}\n}}')
        f_js.close()

        # Temperature data
        data_name = 'temperature'
        file_name = f'../data/temp/{data_name}.json'

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
        js_temp = []
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
                    js_temp.append((date_time, param["values"][0]))
                # if vindhastighet
                # if regn (nederbörd)
                # if molnighet (total cloud cover)

        f_js = open('../server/src/tempmodule.js', 'w')
        f_js.write('''import moment from 'moment'
const data = [
''')
        for (x, y) in js_temp:
            f_js.write(f"   {{time: moment('{x}', \"YYYY-MM-DD hh:mm:ss\"), count: {y}}},\n")

        f_js.write('''];

module.exports = {
    get_data: function() {
        return data;
    },
    get_data_name: function() {
        return "Temperature";
    }
}
''')
        f_js.close()


        # plt.ion()
        # plt.subplot(2,1,1)
        # plt.grid()
        # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d (%H.00)'))
        # plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour=[7,19]))
        # plt.gcf().autofmt_xdate()
        # plt.plot(hour, temperature, '.-')
        # # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d (%H.00)'))
        # # plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour=[7,19]))

        # plt.subplot(2,1,2)
        # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d (%H.00)'))
        # plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour=[7,19]))
        # plt.gcf().autofmt_xdate()
        # plt.plot(x_axis, price, '.-')
        # plt.grid()

        # plt.pause(3600)
        # plt.close()

        #time.sleep(3600)
        print("let's do it again")
