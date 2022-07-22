<script context="module" type="ts">
	export async function load({ fetch }) {
		fetch()
	}
</script>

<script type="ts">
	import tree from '$lib/assets/tree.jpg'
</script>

<main>
	<div class="heading">
		My 2021 <br>
		Advent of Code <br>
		Solutions <br>
	</div>
	<img src="{tree}" alt="christmas tree pic" width="100%">
	<div class="section">
		<div class="subheading">
			<span>optimized rust solution performances</span>
		</div>
	</div>
</main>

<style>
	.subheading {
		color: white;
		font-size: 60px;
		display: flex;
		justify-content: center;
	}
	main {
		background-color: #00001A;
	}
	.heading {
		position: absolute;
		top: 30%;
		left: 13%;
		font-size: 85px;
		color: beige;
	}
	.section {
		margin-top: 7%;
	}
</style>