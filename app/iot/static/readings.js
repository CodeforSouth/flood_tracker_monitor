window.onload = function() {
    getReadings();
  };


function getReadings(){
    //has to be a better way of doing that.
    const deviceID = window.location.pathname.slice(-1);
    const url = `/api/devices/${deviceID}`
    const request = fetch(url);
    request.then((response) => response.json()).then((data) => {
        buildSummary(data.data);
    }).catch((e) => {
        return e;
    })
}

function buildSummary(data){
    const rawPoints = data.map((point) => {
        return { t: new Date(point.reading_reported), y: Math.abs(point.reading_mm)}
    });
    // console.dir(Date.parse(rawPoints[0].t))
    buildGraph(rawPoints);
}

function buildGraph(data){
    var ctx = document.getElementById('myChart').getContext('2d');
    const chartData = {
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data
        }]
    }
    let myChart = new Chart(ctx, {
        type: 'scatter',
        data: chartData,
        options: {
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        unit: 'day'
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