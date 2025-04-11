<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	let temperature = $state(0);
	let humidity = $state(0);
	let pressure = $state(0);

	function apiGetSensorData(body) {
		// call api to move left forward
		fetch('http://heat.local:8000/api/getSensorData', {
			method: 'GET'
		})
			.then((response) => {
				return response.json();
			})
			.then((data) => {
				// temperature
				temperature = data.temperature;
				temperatureData = [
					...temperatureData,
					{ x: new Date().toLocaleTimeString(), y: data.temperature }
				];
				tempChart.data.datasets[0].data = temperatureData;
				tempChart.update();

				// humidity
				humidity = data.humidity;
				humidityData = [...humidityData, { x: new Date().toLocaleTimeString(), y: data.humidity }];
				humChart.data.datasets[0].data = humidityData;
				humChart.update();

				// pressure
				pressure = data.pressure;
				pressureData = [...pressureData, { x: new Date().toLocaleTimeString(), y: data.pressure }];
				presChart.data.datasets[0].data = pressureData;
				presChart.update();
			});
	}

	let temperatureData = [];
	let tempChart = null;

	let humidityData = [];
	let humChart = null;

	let pressureData = [];
	let presChart = null;

	onMount(() => {
		tempChart = new Chart(document.getElementById('temperatureChart').getContext('2d'), {
			type: 'line',
			data: {
				datasets: [
					{
						label: 'Temperature',
						data: temperatureData
					}
				]
			},
			options: {
				responsive: true,
				scales: {
					y: {
						beginAtZero: true
					}
				},
				animation: false,
				plugins: {
					legend: {
						display: false
					}
				}
			}
		});

		humChart = new Chart(document.getElementById('humidityChart').getContext('2d'), {
			type: 'line',
			data: {
				datasets: [
					{
						label: 'Humidity',
						data: humidityData
					}
				]
			},
			options: {
				responsive: true,
				scales: {
					y: {
						beginAtZero: true
					}
				},
				animation: false,
				plugins: {
					legend: {
						display: false
					}
				}
			}
		});

		presChart = new Chart(document.getElementById('pressureChart').getContext('2d'), {
			type: 'line',
			data: {
				datasets: [
					{
						label: 'Pressure',
						data: pressureData
					}
				]
			},
			options: {
				responsive: true,
				scales: {
					y: {
						beginAtZero: true
					}
				},
				animation: false,
				plugins: {
					legend: {
						display: false
					}
				}
			}
		});

		apiGetSensorData();
		const interval = setInterval(() => {
			apiGetSensorData();
		}, 1000);

		return () => clearInterval(interval);
	});
</script>

<h1>Data</h1>
<div class="data">
	<div class="group">
		Temperature: {temperature} °C
		<div class="chart">
			<canvas id="temperatureChart"></canvas>
		</div>
	</div>

	<div class="group">
		Humidity: {humidity} %
		<div class="chart">
			<canvas id="humidityChart"></canvas>
		</div>
	</div>

	<div class="group">
		Pressure: {pressure} hPa
		<div class="chart">
			<canvas id="pressureChart"></canvas>
		</div>
	</div>
</div>

<style>
	@media (min-width: 850px) {
		.data {
			flex-direction: row !important;
			flex-wrap: wrap !important;
			justify-content: space-around;
			gap: 20px;
		}
	}

	.data {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.chart {
		width: 400px !important;
		max-width: calc(100% - 1rem) !important;
	}

	#temperatureChart {
		width: 100% !important;
		height: 100% !important;
	}

	#humidityChart {
		width: 100% !important;
		height: 100% !important;
	}

	#pressureChart {
		width: 100% !important;
		height: 100% !important;
	}
</style>
