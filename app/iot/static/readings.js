window.onload = function() {
    const chart = buildChart();
    const minutesFunction = (date) => date.setSeconds(0,0);
    const hoursFunction = (date) => date.setMinutes(0, 0, 0);
    document.getElementById('minutes').addEventListener("click", () => {getReadings(minutesFunction, chart)});
    document.getElementById('hours').addEventListener("click", () => {getReadings(hoursFunction, chart)});
    getReadings(hoursFunction, chart);
  };

function getReadings(scaleOption, chart){
    console.log('rendering')
    //might be a better way of getting deviceID.
    const deviceID = window.location.pathname.slice(-1);
    const url = `/api/devices/${deviceID}`
    const request = fetch(url);
    //might need to move to readableStream if datasets get really big
    request.then((response) => response.json()).then((data) => {
        const dataArray = buildSummary(data.data);
        buildHighLow(dataArray, scaleOption, chart);
    }).catch((e) => {
        return e;
    })
}

function buildSummary(data){
    const rawPoints = data.map((point) => {
        return { t: new Date(point.reading_reported), y: Math.abs(point.reading_mm)}
    });
    // buildGraph(rawPoints);
    return rawPoints;
}

function buildHighLow(data, scaleOption, chart){
    let leadingDate = [];
    let lowDataSet = [];
    let highDataSet = [];
    data.map(element => {
        if (scaleOption){
            scaleOption(element.t);
        }
        if (leadingDate.length > 0 && +leadingDate[leadingDate.length -1] === +element.t) {
            if(element.y < lowDataSet[lowDataSet.length - 1].y){
                lowDataSet[lowDataSet.length - 1]. y = element.y;
            }
            if(element.y > highDataSet[highDataSet.length -1].y){
                highDataSet[highDataSet.length - 1]. y = element.y;

            }
        } else {
            leadingDate.push(element.t);
            lowDataSet.push({
                t: element.t,
                y: element.y
            });
            highDataSet.push({
                t: element.t,
                y: element.y
            });
        }
    });
    chart.data.datasets[0].data = lowDataSet;
    chart.data.datasets[1].data = highDataSet;
    chart.update();
}

function buildChart(high, low){
    var ctx = document.getElementById('myChart').getContext('2d');
    const chartData = {
        datasets: [
            {
            label: 'Low Values',
            backgroundColor: 'rgba(178,34,200,0.2)',
            borderColor: 'rgb(255, 99, 132)',
            data: low,
            fill: 1,
            lineTension: 0,
        },
        {
            label: 'High Values',
            backgroundColor: 'rgb(255, 99, 0)',
            borderColor: 'rgb(255, 99, 132)',
            data: high,
            fill: false,
            lineTension: 0,
        }],
        
    }
    return new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: {
            
            plugins: {
                filler: {
                    propagate: true
                }
            },
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        unit: 'week',
                    },
                    distribution: 'series',
                    ticks: {
                        source: 'data',
                        autoSkip: true
                    }
                }]
            }
        }    
    });

}
