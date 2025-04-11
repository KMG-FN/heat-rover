<script>
	import { SvelteSet } from 'svelte/reactivity';

	let activeButtons = $state(new SvelteSet(''));
	let intervals = {};

	function apiMove(body) {
		// call api to move left forward
		fetch('http://heat.local:8000/api/move', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ ...body })
		})
			.then((response) => {
				return response.json();
			})
			.then((data) => {
				console.log(data.message);
			});
	}

	function apiCrane(body) {
		// call api to move left forward
		fetch('http://heat.local:8000/api/crane', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ ...body })
		})
			.then((response) => {
				return response.json();
			})
			.then((data) => {
				console.log(data.message);
			});
	}

	function startCommand(direction, action, apiFunction) {
		console.log(`start ${direction} ${action}`);
		// set button active
		activeButtons.add(`${direction}-${action}`);

		// clear interval if it exists (should not happen...)
		if (intervals[direction]) {
			clearInterval(intervals[direction]);
		}

		// start interval
		intervals[direction] = setInterval(() => {
			apiFunction({ direction: direction, action: action });
		}, 500);

		apiFunction({ direction: direction, action: action });
	}

	function stopCommand(direction, action, apiFunction) {
		// set button inactive
		activeButtons.delete(`${direction}-${action}`);

		// clear interval
		if (intervals[direction]) {
			clearInterval(intervals[direction]);
			delete intervals[direction];
		}

		apiFunction({ direction: direction, action: 'stop' });
	}
</script>

<div class="control">
	<h1>Drive & Control</h1>

	<div class="group">
		<h2>Rover</h2>
		<div class="rover">
			<div class="btnSlot">
				Left
				<button
					class="ctrlBtn"
					class:active={activeButtons.has('left-forward')}
					onpointerdown={() => startCommand('left', 'forward', apiMove)}
					onpointerup={() => stopCommand('left', 'forward', apiMove)}
					onpointerleave={() => stopCommand('left', 'forward', apiMove)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
						><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
							d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
						/></svg
					>
				</button>
				<button
					class="ctrlBtn"
					class:active={activeButtons.has('left-backward')}
					onpointerdown={() => startCommand('left', 'backward', apiMove)}
					onpointerup={() => stopCommand('left', 'backward', apiMove)}
					onpointerleave={() => stopCommand('left', 'backward', apiMove)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
						><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
							d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"
						/></svg
					>
				</button>
			</div>
			<div class="btnSlot">
				Right
				<button
					class="ctrlBtn"
					class:active={activeButtons.has('right-forward')}
					onpointerdown={() => startCommand('right', 'forward', apiMove)}
					onpointerup={() => stopCommand('right', 'forward', apiMove)}
					onpointerleave={() => stopCommand('right', 'forward', apiMove)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
						><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
							d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
						/></svg
					>
				</button>
				<button
					class="ctrlBtn"
					class:active={activeButtons.has('right-backward')}
					onpointerdown={() => startCommand('right', 'backward', apiMove)}
					onpointerup={() => stopCommand('right', 'backward', apiMove)}
					onpointerleave={() => stopCommand('right', 'backward', apiMove)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
						><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
							d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"
						/></svg
					>
				</button>
			</div>
		</div>
	</div>

	<div class="group">
		<h2>Crane Grabber</h2>
		<div class="rover">
			<div class="btnSlot">
				Up & Down
				<button
					class="ctrlBtn"
					class:active={activeButtons.has('vertical-up')}
					onpointerdown={() => startCommand('vertical', 'up', apiCrane)}
					onpointerup={() => stopCommand('vertical', 'up', apiCrane)}
					onpointerleave={() => stopCommand('vertical', 'up', apiCrane)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
						><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
							d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
						/></svg
					>
				</button>
				<button
					class="ctrlBtn"
					class:active={activeButtons.has('vertical-down')}
					onpointerdown={() => startCommand('vertical', 'down', apiCrane)}
					onpointerup={() => stopCommand('vertical', 'down', apiCrane)}
					onpointerleave={() => stopCommand('vertical', 'down', apiCrane)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
						><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
							d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"
						/></svg
					>
				</button>
			</div>
			<div class="btnSlot">
				Open & Close
				<button
					class="ctrlBtn"
					class:active={activeButtons.has('grabber-open')}
					onpointerdown={() => startCommand('grabber', 'open', apiCrane)}
					onpointerup={() => stopCommand('grabber', 'open', apiCrane)}
					onpointerleave={() => stopCommand('grabber', 'open', apiCrane)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"
						><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
							d="M352 144c0-44.2 35.8-80 80-80s80 35.8 80 80l0 48c0 17.7 14.3 32 32 32s32-14.3 32-32l0-48C576 64.5 511.5 0 432 0S288 64.5 288 144l0 48L64 192c-35.3 0-64 28.7-64 64L0 448c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-192c0-35.3-28.7-64-64-64l-32 0 0-48z"
						/></svg
					>
				</button>
				<button
					class="ctrlBtn"
					class:active={activeButtons.has('grabber-close')}
					onpointerdown={() => startCommand('grabber', 'close', apiCrane)}
					onpointerup={() => stopCommand('grabber', 'close', apiCrane)}
					onpointerleave={() => stopCommand('grabber', 'close', apiCrane)}
				>
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"
						><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
							d="M144 144l0 48 160 0 0-48c0-44.2-35.8-80-80-80s-80 35.8-80 80zM80 192l0-48C80 64.5 144.5 0 224 0s144 64.5 144 144l0 48 16 0c35.3 0 64 28.7 64 64l0 192c0 35.3-28.7 64-64 64L64 512c-35.3 0-64-28.7-64-64L0 256c0-35.3 28.7-64 64-64l16 0z"
						/></svg
					>
				</button>
			</div>
		</div>
	</div>
</div>

<style>
	.btnSlot {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.control {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.rover {
		display: flex;
		flex-direction: row;
		gap: 50px;
	}

	.rover > div {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.ctrlBtn {
		padding: 0.5rem;
		width: 100px;
		height: 100px;
		touch-action: none;
		background-color: #e83f25;
		border: none;
		border-radius: 50%;
	}

	.ctrlBtn.active {
		background-color: #a62c2c;
	}

	.ctrlBtn > svg {
		height: 45px;
	}
</style>
