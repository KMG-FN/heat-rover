<script>
	import { page } from '$app/stores';
	let { children } = $props();

	const API_BASE = import.meta.env.VITE_API_BASE;

	let shutdownToggle = $state(false);
</script>

<header>
	<h1>H.E.A.T. Rover</h1>
	<nav>
		<a href="/drive" class:active={$page.url.pathname === '/drive'}>
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"
				><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
					d="M288 64l0 64 128 0L368 64l-80 0zM419.2 25.6L496 128l80 0c17.7 0 32 14.3 32 32l0 64c17.7 0 32 14.3 32 32s-14.3 32-32 32c-29.2-38.9-75.7-64-128-64s-98.8 25.1-128 64l-64 0c-29.2-38.9-75.7-64-128-64s-98.8 25.1-128 64c-17.7 0-32-14.3-32-32s14.3-32 32-32l0-64c0-17.7 14.3-32 32-32l160 0 0-80c0-26.5 21.5-48 48-48l96 0c20.1 0 39.1 9.5 51.2 25.6zM152 256l16 0c12.1 0 22.1 8.9 23.8 20.6c7.6 2.2 14.9 5.3 21.7 9c9.4-7 22.8-6.3 31.3 2.3l11.3 11.3c8.6 8.6 9.3 21.9 2.3 31.3c3.7 6.8 6.8 14.1 9 21.7c11.6 1.7 20.6 11.7 20.6 23.8l0 16c0 12.1-8.9 22.1-20.6 23.8c-2.2 7.6-5.3 14.9-9 21.7c7 9.4 6.3 22.8-2.3 31.3l-11.3 11.3c-8.6 8.6-21.9 9.3-31.3 2.2c-6.8 3.7-14.1 6.8-21.7 9C190.1 503.1 180.1 512 168 512l-16 0c-12.1 0-22.1-8.9-23.8-20.6c-7.6-2.2-14.9-5.3-21.7-9c-9.4 7.1-22.8 6.3-31.3-2.2L63.8 468.9c-8.6-8.6-9.3-21.9-2.3-31.3c-3.7-6.9-6.8-14.1-9-21.8C40.9 414.1 32 404.1 32 392l0-16c0-12.1 8.9-22.1 20.6-23.8c2.2-7.6 5.3-14.9 9-21.8c-7-9.4-6.3-22.8 2.3-31.3l11.3-11.3c8.6-8.6 21.9-9.3 31.3-2.3c6.8-3.7 14.1-6.8 21.7-9c1.7-11.6 11.7-20.6 23.8-20.6zm8 176a48 48 0 1 0 0-96 48 48 0 1 0 0 96zM448.2 276.6c1.7-11.6 11.7-20.6 23.8-20.6l16 0c12.1 0 22.1 8.9 23.8 20.6c7.6 2.2 14.9 5.3 21.8 9c9.4-7 22.8-6.3 31.3 2.3l11.3 11.3c8.6 8.6 9.3 21.9 2.2 31.3c3.7 6.8 6.8 14.1 9 21.7c11.6 1.7 20.6 11.7 20.6 23.8l0 16c0 12.1-8.9 22.1-20.6 23.8c-2.2 7.6-5.3 14.9-9 21.7c7 9.4 6.3 22.8-2.2 31.3l-11.3 11.3c-8.6 8.6-21.9 9.3-31.3 2.2c-6.9 3.7-14.1 6.8-21.8 9C510.1 503.1 500.1 512 488 512l-16 0c-12.1 0-22.1-8.9-23.8-20.6c-7.6-2.2-14.9-5.3-21.7-9c-9.4 7.1-22.8 6.3-31.3-2.2l-11.3-11.3c-8.6-8.6-9.3-21.9-2.2-31.3c-3.7-6.9-6.8-14.1-9-21.8C360.9 414.1 352 404.1 352 392l0-16c0-12.1 8.9-22.1 20.6-23.8c2.2-7.6 5.3-14.9 9-21.8c-7-9.4-6.3-22.8 2.2-31.3l11.3-11.3c8.6-8.6 21.9-9.3 31.3-2.3c6.8-3.7 14.1-6.8 21.7-9zM528 384a48 48 0 1 0 -96 0 48 48 0 1 0 96 0z"
				/></svg
			></a
		>
		<a href="/data" class:active={$page.url.pathname === '/data'}
			><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
				><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
					d="M64 64c0-17.7-14.3-32-32-32S0 46.3 0 64L0 400c0 44.2 35.8 80 80 80l400 0c17.7 0 32-14.3 32-32s-14.3-32-32-32L80 416c-8.8 0-16-7.2-16-16L64 64zm406.6 86.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L320 210.7l-57.4-57.4c-12.5-12.5-32.8-12.5-45.3 0l-112 112c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L240 221.3l57.4 57.4c12.5 12.5 32.8 12.5 45.3 0l128-128z"
				/></svg
			></a
		>
	</nav>
</header>

{@render children()}

<div class="shutdown">
	{#if shutdownToggle}
		<div>
			Shutdown the Rover?
			<button
				class="confirm"
				onclick={() => {
					fetch(`${API_BASE}/shutdown`, { method: 'GET' });
				}}>Yes</button
			>
			<button
				class="cancel"
				onclick={() => {
					shutdownToggle = false;
				}}>No</button
			>
		</div>
	{/if}
	<!-- svelte-ignore a11y_consider_explicit_label -->
	<button
		onclick={() => {
			shutdownToggle = !shutdownToggle;
		}}
		><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
			><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path
				d="M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 224c0 17.7 14.3 32 32 32s32-14.3 32-32l0-224zM143.5 120.6c13.6-11.3 15.4-31.5 4.1-45.1s-31.5-15.4-45.1-4.1C49.7 115.4 16 181.8 16 256c0 132.5 107.5 240 240 240s240-107.5 240-240c0-74.2-33.8-140.6-86.6-184.6c-13.6-11.3-33.8-9.4-45.1 4.1s-9.4 33.8 4.1 45.1c38.9 32.3 63.5 81 63.5 135.4c0 97.2-78.8 176-176 176s-176-78.8-176-176c0-54.4 24.7-103.1 63.5-135.4z"
			/></svg
		></button
	>
</div>

<style>
	button {
		border: none;
		padding: 0.5rem;
		border-radius: 5px;
	}

	.confirm {
		background-color: #4caf50;
	}

	.cancel {
		background-color: #f44336;
	}

	.shutdown {
		display: flex;
		flex-direction: row;
		margin-left: auto;
		bottom: 0;
		right: 0;
	}

	.shutdown > div {
		margin-bottom: 0.5rem;
	}

	.shutdown > div > button {
		width: 50px;
		height: 40px;
	}

	.shutdown > button {
		width: fit-content;
		margin-left: 0.5rem;
	}

	.shutdown > button > svg {
		width: 30px;
	}

	:global(html) {
		background-color: #d3ca79;
	}

	:global(body) {
		display: flex;
		flex-direction: column;
		gap: 10px;
		align-items: center;
		font-family: sans-serif;
	}

	:global(.group) {
		background-color: #b3b3b3;
		padding: 1rem;
		border-radius: 15px;
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-bottom: 1rem;
		box-shadow: 0 0 5px 3px #959595;
		max-width: calc(100vw - 3rem);
	}

	header {
		background-color: #ea7300;
		padding: 0.5rem;
		border-radius: 15px;
	}

	nav {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		gap: 20px;
	}

	h1 {
		margin: 0.5rem;
	}

	a {
		display: flex;
		flex-direction: column;
		align-items: center;
		text-decoration: none;
		fill: rgba(0, 0, 0, 0.692);
		padding: 0.5rem;
		outline: 1px solid #964d4d93;
		border-radius: 15px;
		transition: all 0.3s ease;
		box-shadow: 0 0 5px 3px #964d4d93;
	}

	a:hover {
		text-decoration: underline;
	}

	a > svg {
		height: 50px;
	}

	a.active > svg {
		fill: #801d1d;
	}

	a.active {
		outline: 1px solid #801d1d !important;
		/* 		border-radius: 15px;
 */
		box-shadow: 0 0 6px 4px #801d1d;
	}
</style>
