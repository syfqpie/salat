<template lang="pug">
div
	PrayerDailyHeader(
		:today-items="todayPrayerTimes"
		:tomorrow-items="tomorrowPrayerTimes"
		:today-dates="todayDates")
	PrayerDailyItem(:today-items="todayPrayerTimes" :today-dates="todayDates")
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { PrayerTime } from '~/types/prayer-times'

export default defineComponent({
	name: 'PrayerDaily',
	computed: {
		todayPrayerTimes (): PrayerTime | null {
			return this.$store.getters['prayerTimes/today']
		},
		tomorrowPrayerTimes (): PrayerTime | null {
			return this.$store.getters['prayerTimes/tomorrow']
		},
		todayDates () {
			return this.$store.getters['prayerTimes/todayDates']
		}
	},
	mounted () {
		this.$store.dispatch('prayerTimes/getData')
	}
})
</script>
