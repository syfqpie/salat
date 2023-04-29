<template lang="pug">
div
	PrayerDailyHeader(:today-items="todayPrayerTimes" :tomorrow-items="tomorrowPrayerTimes")
	PrayerDailyItem(:today-items="todayPrayerTimes")
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
		}
	},
	mounted () {
		this.$store.dispatch('prayerTimes/getData')
	}
})
</script>
