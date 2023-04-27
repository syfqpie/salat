<template lang="pug">
div
	div(class="grid grid-rows-7 grid-flow-col gap-4")
		template(v-for="xx in [0, 1, 2, 3, 4, 5, 6]")
			div(class="p-6 border-dashed border-green-300 border rounded-lg")
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'PrayerDailyItem'
})
</script>
