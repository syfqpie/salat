<template lang="pug">
div(class="overflow-hidden p-6 text-center")
	div(class="p-8 rounded-lg mb-4 bg-white shadow-lg relative")
		img(
			class="h-24 w-auto mx-auto"
			src="~/assets/icons/lab.png"
		)
		h5(class="mb-1 text-xl font-medium") Welcome to Salat
		p(class="mb-1")
			span(class="text-sm") {{ appVersion }}
		p(class="text-xs") Data is scrapped from
			a(
				href="https://www.e-solat.gov.my/"
			class="ms-0.5 font-semibold text-gray-700 hover:text-green-300 hover:underline") e-solat
		p(class="text-xs") Icons are from
			a(
				href="https://www.flaticon.com/packs/muslim"
				class="ms-1 font-semibold hover:text-green-300 text-gray-700 hover:underline") flaticon
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'AboutPage',
	data () {
		return {
			appVersion: String(process.env.appVersion).replaceAll('"', '')
		}
	}
})
</script>
