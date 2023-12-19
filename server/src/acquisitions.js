import Chart from 'chart.js/auto'
import moment from 'moment'

const dataModule = require('./tempmodule');

(async function() {
  // const data = [
  //   { time: moment('2012-11-06 23:39:30', moment.ISO_8601), count: 10 },
  //   { time: moment('2015-11-06 23:39:30', moment.ISO_8601), count: 20 },
  //   { time: moment('2016-11-06 23:39:30', moment.ISO_8601), count: 15 },
  //   { time: moment('2017-11-06 23:39:30', moment.ISO_8601), count: 25 },
  //   { time: moment('2018-11-06 23:39:30', moment.ISO_8601), count: 22 },
  //   { time: moment('2019-11-06 23:39:30', moment.ISO_8601), count: 30 },
  //   { time: moment('2020-11-06 23:39:30', moment.ISO_8601), count: 28 },
  //   { time: moment('2021-11-06 23:39:30', moment.ISO_8601), count: 80 },
  // ];

  let data = dataModule.get_data();

  new Chart(
    document.getElementById('acquisitions'),
    {
      type: 'scatter',
      data: {
          labels: data.map(row => row.time),
          datasets: [
            {
            showLine: true,
            label: "Temperature",
            data: data.map(row => row.count)
          }
        ]
      },
      options: {
        scales: {
            x: {
                ticks: {
                    callback: function(value, index, ticks) {
                        return moment(value).format('YYYY-MM-DD (hh.mm.ss)');
                    }
                }
            }
        }
        },
        elements: {
            line: {
                tension: 0.25
            }
        }
    }
  );
})();
