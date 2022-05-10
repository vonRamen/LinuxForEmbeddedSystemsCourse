var chartIdToData = {};
var chartIdToChart = {};
var chartIdToChartExtras = {};

async function updateChart(chartId, topics, timeSinceNow) {
    var i = 0;
    chart1 = chartIdToChart[chartId]

    chart1.update();
    var chartExtras = chartIdToChartExtras[chartId]

    for (let i = 0; i < topics.length; i++) {
        var topic = topics[i]
        splitTopic = topic.split("/");
        var response = await _getData(splitTopic[0], splitTopic[1], splitTopic[2], splitTopic[3], Date.now() - timeSinceNow, Date.now());

        var chart1Data = chartIdToData[chartId];

        chart1Data.labels = [];
        chart1Data.datasets[i].data = [];

        chart1Data.datasets[i].borderColor.push(chartExtras.colors[i]);
        response.forEach(res => {
            var date = new Date(res.timestamp);
            var xLabel;
            if (new Date(Date.now()).toISOString().split('T')[0] == date.toISOString().split('T')[0]) {
                xLabel = date.toLocaleTimeString();
            } else {
                xLabel = date.toLocaleDateString() + "T" + date.toLocaleTimeString();
            }

            chart1Data.labels.push(xLabel);
            chart1Data.datasets[i].data.push(res.message);
        });
    }

    chart1.update();
}

$(document).ready(function () {
    const graph_ref1526914054_context = document.getElementById('chart-Temperature').getContext('2d');
    graph_ref1526914054_data = {
        labels: [],
        datasets: [{
            label: 'Temperature',
            data: [],
            borderColor: [
            ],
            borderWidth: 1
        }
        ]
    }

    graph_ref1526914054 = new Chart(graph_ref1526914054_context, {
        type: 'line',
        data: graph_ref1526914054_data,
        options: {
            scales: {
                y: {
                    title: {
                        display: true,
                        text: "Degrees (C)"
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: "Time"
                    }
                }
            }
        }
    });

    chartIdToData['chart-Temperature'] = graph_ref1526914054_data;
    chartIdToChart['chart-Temperature'] = graph_ref1526914054;
    chartIdToChartExtras['chart-Temperature'] = {}
    chartIdToChartExtras['chart-Temperature'].colors = [];

    chartIdToChartExtras['chart-Temperature'].colors.push('rgba(255, 0, 0, 255)');

    const graph_ref1659208572_context = document.getElementById('chart-Humidity').getContext('2d');
    graph_ref1659208572_data = {
        labels: [],
        datasets: [{
            label: 'Humidity',
            data: [],
            borderColor: [
            ],
            borderWidth: 1
        }
        ]
    }

    graph_ref1659208572 = new Chart(graph_ref1659208572_context, {
        type: 'line',
        data: graph_ref1659208572_data,
        options: {
            scales: {
                y: {
                    title: {
                        display: true,
                        text: "RH"
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: "Time"
                    }
                }
            }
        }
    });

    chartIdToData['chart-Humidity'] = graph_ref1659208572_data;
    chartIdToChart['chart-Humidity'] = graph_ref1659208572;
    chartIdToChartExtras['chart-Humidity'] = {}
    chartIdToChartExtras['chart-Humidity'].colors = [];

    chartIdToChartExtras['chart-Humidity'].colors.push('rgba(255, 0, 0, 255)');

    const graph_ref762406221_context = document.getElementById('chart-CO2').getContext('2d');
    graph_ref762406221_data = {
        labels: [],
        datasets: [{
            label: 'CO2',
            data: [],
            borderColor: [
            ],
            borderWidth: 1
        }
        ]
    }

    graph_ref762406221 = new Chart(graph_ref762406221_context, {
        type: 'line',
        data: graph_ref762406221_data,
        options: {
            scales: {
                y: {
                    title: {
                        display: true,
                        text: "ppm"
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: "Time"
                    }
                }
            }
        }
    });

    chartIdToData['chart-CO2'] = graph_ref762406221_data;
    chartIdToChart['chart-CO2'] = graph_ref762406221;
    chartIdToChartExtras['chart-CO2'] = {}
    chartIdToChartExtras['chart-CO2'].colors = [];

    chartIdToChartExtras['chart-CO2'].colors.push('rgba(255, 0, 0, 255)');


    MQTTConnect(mqtt => {
        // Make vars
        var mqtt_topic_165352349 = 'smart_alarm/data/temperature';
        mqtt.subscribe(mqtt_topic_165352349);
        var mqtt_topic_863183686 = 'smart_alarm/data/humidity';
        mqtt.subscribe(mqtt_topic_863183686);
        var mqtt_topic_129108662 = 'smart_alarm/data/co2';
        mqtt.subscribe(mqtt_topic_129108662);

        mqtt.onMessageArrived = function (message) {
            console.log("Message Arrived: " + message.payloadString);
            console.log("Topic:     " + message.destinationName);
            console.log("QoS:       " + message.qos);
            console.log("Retained:  " + message.retained);
            // Read Only, set if message might be a duplicate sent from broker
            console.log("Duplicate: " + message.duplicate);

            var now = Date.now();
            var date = new Date(now);
            xLabel = date.toLocaleTimeString();


            if (message.destinationName == mqtt_topic_165352349) {
                graph_ref1526914054_data.labels.push(xLabel);
                graph_ref1526914054_data.datasets[0].data.push(message.payloadString);
                graph_ref1526914054.update();
            }
            if (message.destinationName == mqtt_topic_863183686) {
                graph_ref1659208572_data.labels.push(xLabel);
                graph_ref1659208572_data.datasets[0].data.push(message.payloadString);
                graph_ref1659208572.update();
            }
            if (message.destinationName == mqtt_topic_129108662) {
                graph_ref762406221_data.labels.push(xLabel);
                graph_ref762406221_data.datasets[0].data.push(message.payloadString);
                graph_ref762406221.update();
            }
        }
    });

    updateChart('chart-Temperature', ['smart_alarm/data/temperature'], Date.now());
    updateChart('chart-Humidity', ['smart_alarm/data/humidity'], Date.now());
    updateChart('chart-CO2', ['smart_alarm/data/co2'], Date.now());
});
