<script>
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

	function leftForward() {
		apiMove({ direction: 'left', action: 'forward' });
	}

	function leftForwardStop() {
		apiMove({ direction: 'left', action: 'stop' });
	}

	function rightForward() {
		apiMove({ direction: 'right', action: 'stop' });
	}

	function rightForwardStop() {
		apiMove({ direction: 'right', action: 'stop' });
	}
</script>

<header>
	<h1>HEAT Rover</h1>
</header>
<div class="segments">
	<div class="control">
		<h1>Steuerung</h1>

		<div class="steering-block">
			<h2>Rover</h2>
			<div class="rover">
				<div class="btnSlot">
					Links
					<button
						class="ctrlBtn"
						on:pointerdown={leftForward}
						on:pointerup={leftForwardStop}
						on:pointerleave={leftForwardStop}
					>
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
							><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
								d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
							/></svg
						>
					</button>
					<button class="ctrlBtn">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
							><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
								d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"
							/></svg
						>
					</button>
				</div>
				<div class="btnSlot">
					Rechts
					<button
						class="ctrlBtn"
						on:pointerdown={rightForward}
						on:pointerup={rightForwardStop}
						on:pointerleave={rightForwardStop}
					>
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
							><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
								d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
							/></svg
						>
					</button>
					<button class="ctrlBtn">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
							><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
								d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"
							/></svg
						>
					</button>
				</div>
			</div>
		</div>

		<div class="steering-block">
			<h2>Kran</h2>
			<div class="rover">
				<div class="btnSlot">
					Hoch & runter
					<button
						class="ctrlBtn"
						on:pointerdown={leftForward}
						on:pointerup={leftForwardStop}
						on:pointerleave={leftForwardStop}
					>
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
							><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
								d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
							/></svg
						>
					</button>
					<button class="ctrlBtn">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
							><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
								d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"
							/></svg
						>
					</button>
				</div>
				<div class="btnSlot">
					Rechts
					<button class="ctrlBtn">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
							><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
								d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
							/></svg
						>
					</button>
					<button class="ctrlBtn">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
							><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
								d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"
							/></svg
						>
					</button>
				</div>
			</div>
		</div>
	</div>
	<div class="data">
		<h1>Daten</h1>
	</div>
</div>

<style>
	.btnSlot {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.steering-block {
		background-color: #e5e5e5;
		padding: 1rem;
		border-radius: 15px;
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-bottom: 1rem;
	}

	.segments {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	:global(body) {
		display: flex;
		flex-direction: column;
		gap: 10px;
		align-items: center;
		font-family: sans-serif;
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
		width: 70px;
		height: 70px;
	}

	.ctrlBtn > svg {
		height: 45px;
	}
</style>
