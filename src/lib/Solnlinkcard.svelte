<script type="ts">
	export let daynum: Number;
	export let status: Boolean[];
	let back_class: string;
	if (daynum <= 10) {
		back_class = "rust enabled"
	}
	else if (status[1]) {
		back_class = "both enabled"
	}
	else if (status[0]) {
		back_class = "part1 enabled"
	}
	else {
		back_class = "none"
	}
</script>

<div class="day_card {back_class}">
	<a href="/solutions/{daynum}">Day {daynum}</a>
</div>

<style>
	@keyframes grow {
		from {
			box-shadow: 0px 0px 4px 0.7px darkcyan;
		}
		to {
			box-shadow: 0px 0px 4px 3px whitesmoke
		}
	}

	.day_card {
		padding: 25px;
		margin: 15px;
		font-size: xx-large;
		border-radius: 10%;
		box-shadow: 0px 0px 4px 0.7px darkcyan;
	}
	.enabled:hover {
		animation-name: grow;
		animation-duration: 0.15s;
		animation-fill-mode: forwards;
	}
	.rust {
		background-color: orangered;
	}
	.both {
		background-color: lightseagreen;
	}
	.part1 {
		background: linear-gradient(
			to bottom right,
			lightseagreen 0%, lightseagreen 50%,
			gray 50%, gray 100%
		);
	}
	.none {
		background-color: gray;
	}
	a {
		color: whitesmoke;
		text-decoration: none;
		text-decoration-style: none;
	}
</style>