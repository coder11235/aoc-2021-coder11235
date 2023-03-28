<script context="module" type="ts">
	const rsBmRrl = "https://raw.githubusercontent.com/coder11235/aoc-2021-coder11235/main/optimised-rust-solutions/benchmark.json";
	// currently the rust solutions are in a "i finshed x day i will do the next one only attitude. no idea when that might change"
	const solnstatusurl = "https://raw.githubusercontent.com/coder11235/aoc-2021-coder11235/main/solutions/info.json"
	export async function load({ fetch }: {fetch: ExternalFetch}) {
		// shut up goddamn typescript
		let perfsraw = await fetch(new Request(rsBmRrl));
		let perfsjson = await perfsraw.json();
		let straw = await fetch(new Request(solnstatusurl))
		let stjson = await straw.json();
		if(perfsraw.ok && straw.ok) {
			return {
				props: {
					rsperfsraw: perfsjson.map((perf: string[], day: number) => ({day: day+1,perf: perf})),
					solnst: stjson
				}
			}
		}
		return {
			status: perfsraw.status,
			error: new Error("cant fetch the benchmarks")
		}
	}
</script>

<script lang="ts">
	export let rsperfsraw: {day: number, perf: string[]}[];
	export let solnst: {incomplete: {day: number, first: boolean}[]};
	let solutionstatuses = new Array(25).fill([true, true]).map((val, num) => ({day: num+1, stat: val}))
	// console.log(solutionstatuses)
	solnst.incomplete.forEach(function({day, first}){
		if(first) {
			solutionstatuses[day-1].stat = [true, false]
		}
		else {
			solutionstatuses[day-1].stat = [false, false]
		}
	})
	// console.log(solutionstatuses)
	let rsperfsparts = [rsperfsraw.slice(0, 5), rsperfsraw.slice(5)]
	import tree from '$lib/assets/tree.jpg'
	import type { ExternalFetch } from '@sveltejs/kit';
	import Solnlinkcard from '$lib/Solnlinkcard.svelte';
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
				<tr><th class="tel">day</th><th class="tel">part 1</th><th class="tel">part 2</th></tr>
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
	<div class="section">
		<div class="subheading">
			<span>links for all my solutions</span>
		</div>
		<div class="solns">
			{#each solutionstatuses as solnstat}
				<Solnlinkcard daynum={solnstat.day} status={solnstat.stat}></Solnlinkcard>
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
	.solns {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}
</style>