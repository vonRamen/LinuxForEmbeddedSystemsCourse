<!DOCTYPE html>
<html>

<head>
    <title>Smart Alarm Clock</title>
    <?php require "header.php" ?>
    <script src="All.js"></script>
</head>

<body>
    <?php require "commonBody.php" ?>
    <ul class="flex-container">
        <li class="chart-container">
            <div class="centered">
                <h3>Temperature</h3>
            </div>
            <canvas id="chart-Temperature"></canvas>
            <div>
                <button id="chart-Temperature-all" class="btn btn-link" onclick="updateChart('chart-Temperature', ['smart_alarm/data/temperature'], Date.now())">All</button>
                <button id="chart-Temperature-year" class="btn btn-link" onclick="updateChart('chart-Temperature', ['smart_alarm/data/temperature'], 12*28*24*60*60*1000)">Last Year</button>
                <button id="chart-Temperature-month" class="btn btn-link" onclick="updateChart('chart-Temperature', ['smart_alarm/data/temperature'], 28*24*60*60*1000)">Last Month</button>
                <button id="chart-Temperature-week" class="btn btn-link" onclick="updateChart('chart-Temperature', ['smart_alarm/data/temperature'], 7*24*60*60*1000)">Last Week</button>
                <button id="chart-Temperature-24-hour" class="btn btn-link" onclick="updateChart('chart-Temperature', ['smart_alarm/data/temperature'], 24*60*60*1000)">24 Hours</button>
                <button id="chart-Temperature-last-hour" class="btn btn-link" onclick="updateChart('chart-Temperature', ['smart_alarm/data/temperature'], 60*60*1000)">Last Hour</button>
            </div>
        </li>
        <li class="chart-container">
            <div class="centered">
                <h3>Humidity</h3>
            </div>
            <canvas id="chart-Humidity"></canvas>
            <div>
                <button id="chart-Humidity-all" class="btn btn-link" onclick="updateChart('chart-Humidity', ['smart_alarm/data/humidity'], Date.now())">All</button>
                <button id="chart-Humidity-year" class="btn btn-link" onclick="updateChart('chart-Humidity', ['smart_alarm/data/humidity'], 12*28*24*60*60*1000)">Last Year</button>
                <button id="chart-Humidity-month" class="btn btn-link" onclick="updateChart('chart-Humidity', ['smart_alarm/data/humidity'], 28*24*60*60*1000)">Last Month</button>
                <button id="chart-Humidity-week" class="btn btn-link" onclick="updateChart('chart-Humidity', ['smart_alarm/data/humidity'], 7*24*60*60*1000)">Last Week</button>
                <button id="chart-Humidity-24-hour" class="btn btn-link" onclick="updateChart('chart-Humidity', ['smart_alarm/data/humidity'], 24*60*60*1000)">24 Hours</button>
                <button id="chart-Humidity-last-hour" class="btn btn-link" onclick="updateChart('chart-Humidity', ['smart_alarm/data/humidity'], 60*60*1000)">Last Hour</button>
            </div>
        </li>
        <li class="chart-container">
            <div class="centered">
                <h3>CO2</h3>
            </div>
            <canvas id="chart-CO2"></canvas>
            <div>
                <button id="chart-CO2-all" class="btn btn-link" onclick="updateChart('chart-CO2', ['smart_alarm/data/co2'], Date.now())">All</button>
                <button id="chart-CO2-year" class="btn btn-link" onclick="updateChart('chart-CO2', ['smart_alarm/data/co2'], 12*28*24*60*60*1000)">Last Year</button>
                <button id="chart-CO2-month" class="btn btn-link" onclick="updateChart('chart-CO2', ['smart_alarm/data/co2'], 28*24*60*60*1000)">Last Month</button>
                <button id="chart-CO2-week" class="btn btn-link" onclick="updateChart('chart-CO2', ['smart_alarm/data/co2'], 7*24*60*60*1000)">Last Week</button>
                <button id="chart-CO2-24-hour" class="btn btn-link" onclick="updateChart('chart-CO2', ['smart_alarm/data/co2'], 24*60*60*1000)">24 Hours</button>
                <button id="chart-CO2-last-hour" class="btn btn-link" onclick="updateChart('chart-CO2', ['smart_alarm/data/co2'], 60*60*1000)">Last Hour</button>
            </div>
        </li>
    </ul>
</body>

</html>