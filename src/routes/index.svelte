<script context="module" type="ts">
	const rsBmRrl = "https://raw.githubusercontent.com/coder11235/aoc-2021-coder11235/main/optimised-rust-solutions/benchmark.json";
	// currently the rust solutions are in a "i finshed x day i will do the next one only attitude. no idea when that might change"
	// const daysRustedUrl = "https://raw.githubusercontent.com/coder11235/aoc-2021-coder11235/main/optimised-rust-solutions/info.json";
	export async function load({ fetch }) {
		let perfsraw = await fetch(rsBmRrl);
		let perfsjson = await perfsraw.json();
		if(perfsraw.ok) {
			return {
				props: {
					rsperfsraw: perfsjson.map((perf: string[], day: number) => ({day: day+1,perf: perf}))
				}
			}
		}
		return {
			status: perfsraw.status,
			error: new Error("cant fetch the benchmarks")
		}
	}
</script>

<script type="ts">
	export let rsperfsraw: object[];
	let rsperfsparts = [rsperfsraw.slice(0, 5), rsperfsraw.slice(5)]
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
		<span class="smol">basically how long my code took to finsh each problem</span>
		<div class="tablepar">
			{#each rsperfsparts as rsperfs}
			<table>
				<tr><th class="tel">day</th><th class="tel">soln 1</th><th class="tel">soln 2</th></tr>
				{#each rsperfs as perf}
					<tr>
						<td class="tel">day {perf.day}</td>
						<td class="tel">{perf.perf[0]}</td>
						<td class="tel">{perf.perf[1]}</td>
					</tr>
				{/each}
			</table>
			{/each}
		</div>
	</div>
</main>

<style>
	table {
		margin: 40px;
	}
	.smol {
		font-style: italic;
		size: 20px;
		color: gainsboro;
		display: flex;
		justify-content: center;
	}
	.tablepar {
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.tel {
		color: whitesmoke;
		font-size: 30px;
		padding: 20px;
	}
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