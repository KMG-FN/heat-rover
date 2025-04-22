<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	let temperature = $state(0);
	let humidity = $state(0);
	let pressure = $state(0);
	let distance = $state(-1);
	let hdop = $state(-1);

	const API_BASE = import.meta.env.VITE_API_BASE;

	function apiGetSensorData(body) {
		// call api to move left forward
		fetch(`${API_BASE}/getSensorData`, {
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

				// distance
				distance = data.distance;
				if (distance != -1) {
					distanceData = [
						...distanceData,
						{ x: new Date().toLocaleTimeString(), y: data.distance }
					];
					distChart.data.datasets[0].data = distanceData;
					distChart.update();
				}

				// hdop
				hdop = data.hdop;
			});
	}

	let logs = $state([]);
	function apiGetListOfLogs() {
		fetch(`${API_BASE}/getListOfLogs`, {
			method: 'GET'
		})
			.then((response) => {
				return response.json();
			})
			.then((data) => {
				logs = data.sort();
			});
	}

	function apiDownloadLog() {
		fetch(`${API_BASE}/downloadLog?log=${selectedLog}`, {
			method: 'GET'
		})
			.then((response) => {
				if (response.ok) {
					return response.blob();
				} else {
					throw new Error('Network response was not ok');
				}
			})
			.then((blob) => {
				const url = window.URL.createObjectURL(blob);
				const a = document.createElement('a');
				a.href = url;
				a.download = selectedLog;
				document.body.appendChild(a);
				a.click();
				a.remove();
			})
			.catch((error) => {
				console.error('There was a problem with the fetch operation:', error);
			});
	}

	let temperatureData = [];
	let tempChart = null;

	let humidityData = [];
	let humChart = null;

	let pressureData = [];
	let presChart = null;

	let distanceData = [];
	let distChart = null;

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

		distChart = new Chart(document.getElementById('distanceChart').getContext('2d'), {
			type: 'line',
			data: {
				datasets: [
					{
						label: 'Distance',
						data: distanceData
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

		apiGetListOfLogs();

		return () => clearInterval(interval);
	});

	let selectedLog = $state('');
</script>

<h1>Data</h1>
<div class="data">
	<div class="group">
		<div>Temperature: <span class="live-data">{temperature} °C</span></div>
		<div class="chart">
			<canvas id="temperatureChart"></canvas>
		</div>
	</div>

	<div class="group">
		<div>Humidity: <span class="live-data">{humidity} %</span></div>
		<div class="chart">
			<canvas id="humidityChart"></canvas>
		</div>
	</div>

	<div class="group">
		<div>Pressure: <span class="live-data">{pressure} hPa</span></div>
		<div class="chart">
			<canvas id="pressureChart"></canvas>
		</div>
	</div>

	<div class="group">
		<div>
			Distance:
			<span class="live-data">
				{#if distance == -1}
					<em>No GPS found yet</em>
				{:else}
					{distance} m
				{/if}
			</span><br />
			HDOP (Accuracy: lower is better!):
			<span class="live-data">
				{#if hdop == -1}
					<em>No GPS found yet</em>
				{:else}
					{hdop}
				{/if}
			</span><br />
		</div>
		<div class="chart">
			<canvas id="distanceChart"></canvas>
		</div>
	</div>

	<div class="group">
		<h3>Log-Files</h3>
		<div class="dropdown">
			<select bind:value={selectedLog}>
				{#each logs as log}
					<option value={log}>{log}</option>
				{/each}
			</select>
			<button class="reloadBtn" onclick={() => apiGetListOfLogs()}
				><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
					><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
						d="M463.5 224l8.5 0c13.3 0 24-10.7 24-24l0-128c0-9.7-5.8-18.5-14.8-22.2s-19.3-1.7-26.2 5.2L413.4 96.6c-87.6-86.5-228.7-86.2-315.8 1c-87.5 87.5-87.5 229.3 0 316.8s229.3 87.5 316.8 0c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0c-62.5 62.5-163.8 62.5-226.3 0s-62.5-163.8 0-226.3c62.2-62.2 162.7-62.5 225.3-1L327 183c-6.9 6.9-8.9 17.2-5.2 26.2s12.5 14.8 22.2 14.8l119.5 0z"
					/></svg
				></button
			>
		</div>
		<button onclick={() => apiDownloadLog()}>Download</button>
	</div>
</div>

<style>
	.live-data {
		font-weight: bold;
		color: #801d1d;
	}

	.dropdown {
		display: flex;
		flex-direction: row;
		gap: 10px;
	}

	select {
		background-color: #ea7300;
		border: none;
		margin: 4px 0px;
		border-radius: 7px;
	}

	button > svg {
		width: 20px;
		height: 20px;
	}

	.reloadBtn {
		padding: 10px 10px;
	}

	button {
		background-color: #ea7300;
		border: none;
		color: black;
		padding: 10px 20px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 16px;
		margin: 4px 2px;
		cursor: pointer;
		border-radius: 7px;
	}

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
