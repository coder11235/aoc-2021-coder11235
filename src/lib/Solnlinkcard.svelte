<script type="ts">
	export let daynum: Number;
	export let status: Boolean[];
</script>

<a href="/day{daynum}">
	<span>
		day: {daynum}
		status: {status}
	</span>
</a>

<style>
	span {
		width: 100%;
		height: 30px;
		color: azure;
	}
</style>