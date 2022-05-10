<!DOCTYPE html>
<html>

<head>
    <title>Smart Alarm Clock</title>
    <?php require $_SERVER['DOCUMENT_ROOT'] . "/header.php" ?>
    <script src="CO2.js"></script>
</head>

<body>
    <?php require $_SERVER['DOCUMENT_ROOT'] . "/commonBody.php" ?>
    <ul class="flex-container">
<li class="chart-container">
    <div class="centered"><h3>CO2</h3></div>
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
