Highcharts.chart('temp_chart', {

    title: {
        text: 'IoTubes sensor values'
    },

    subtitle: {
        text: 'Sensor 1'
    },

    yAxis: {
        title: {
            text: 'Units (S)'
        }
    },
    xAxis: {
        type: 'datetime',
        dateTimeLabelFormats: { // don't display the dummy year
            month: '%e. %b',
            year: '%b'
        },
        title: {
            text: 'Date'
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },

        }
    },

    series: [{
        name: 'Installation',
        data: [[Date.UTC(1970, 10, 25,0), 0],
            [Date.UTC(1970, 10, 25,1), 0.25],
            [Date.UTC(1970, 10, 25,3), 1.41],
            [Date.UTC(1970, 10, 25,8), 1.64]]
    }],
    //series: [{
    //    name: 'Installation',
    //    data:
    //        {{ result.time }}
    //}],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});