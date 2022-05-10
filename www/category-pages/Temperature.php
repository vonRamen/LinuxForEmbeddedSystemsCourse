<!DOCTYPE html>
<html>

<head>
    <title>Smart Alarm Clock</title>
    <?php require $_SERVER['DOCUMENT_ROOT'] . "/header.php" ?>
    <script src="Temperature.js"></script>
</head>

<body>
    <?php require $_SERVER['DOCUMENT_ROOT'] . "/commonBody.php" ?>
    <ul class="flex-container">
<li class="chart-container">
    <div class="centered"><h3>Temperature</h3></div>
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
    </ul>
</body>

</html>
