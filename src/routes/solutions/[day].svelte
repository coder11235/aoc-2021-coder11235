<script context="module" type="ts">
	import type { ExternalFetch, Page } from "@sveltejs/kit";
	export async function load({fetch, page}: {fetch: ExternalFetch, page: Page}){
		let day = page.params.day;
		
	}
</script>