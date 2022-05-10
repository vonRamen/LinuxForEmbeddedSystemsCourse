<!DOCTYPE html>
<html>

<head>
    <title>Smart Alarm Clock</title>
    <?php require $_SERVER['DOCUMENT_ROOT'] . "/header.php" ?>
    <script src="Humidity.js"></script>
</head>

<body>
    <?php require $_SERVER['DOCUMENT_ROOT'] . "/commonBody.php" ?>
    <ul class="flex-container">
<li class="chart-container">
    <div class="centered"><h3>Humidity</h3></div>
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
    </ul>
</body>

</html>
