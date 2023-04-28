<template lang="pug">
div
	PrayerDailyHeader(:today-items="todayPrayerTimes" :tomorrow-items="tomorrowPrayerTimes")
	PrayerDailyItem(:today-items="todayPrayerTimes")
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { getters } from '~/store/prayerTimes'
import { PrayerTime } from '~/types/prayer-times'

export default defineComponent({
	name: 'PrayerDaily',
	data () {
		return {
			todayPrayerTimes: null as PrayerTime | null,
			tomorrowPrayerTimes: null as PrayerTime | null
		}
	},
	mounted () {
		this.$store.dispatch('prayerTimes/getData')
			.then(() => {
				this.todayPrayerTimes = this.$store.getters['prayerTimes/today'] as ReturnType<typeof getters['prayerTimes/today']>
				this.tomorrowPrayerTimes = this.$store.getters['prayerTimes/tomorrow'] as ReturnType<typeof getters['prayerTimes/tomorrow']>
			})
	}
})
</script>
