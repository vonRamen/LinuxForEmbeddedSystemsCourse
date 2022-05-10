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
const graph_ref398445987_context = document.getElementById('chart-Humidity').getContext('2d');
graph_ref398445987_data = {
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
	
graph_ref398445987 = new Chart(graph_ref398445987_context, {
    type: 'line',
    data: graph_ref398445987_data,
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
		
chartIdToData['chart-Humidity'] = graph_ref398445987_data;
chartIdToChart['chart-Humidity'] = graph_ref398445987;
chartIdToChartExtras['chart-Humidity'] = {}
chartIdToChartExtras['chart-Humidity'].colors = [];
    	
chartIdToChartExtras['chart-Humidity'].colors.push('rgba(255, 0, 0, 255)');
        
	
    MQTTConnect(mqtt => {
        // Make vars
var mqtt_topic_1091606371 = 'smart_alarm/data/humidity';
mqtt.subscribe(mqtt_topic_1091606371);

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
            
            
    	        if(message.destinationName == mqtt_topic_1091606371) {
    	        		            graph_ref398445987_data.labels.push(xLabel);
    	        		            graph_ref398445987_data.datasets[0].data.push(message.payloadString);
    	        		            graph_ref398445987.update();
    	        }
        }
    });

	updateChart('chart-Humidity', ['smart_alarm/data/humidity'], Date.now());
});
