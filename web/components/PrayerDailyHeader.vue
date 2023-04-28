<template lang="pug">
div(class="p-3 rounded-lg mb-4")
	div(class="grid grid-cols-6 grid-flow-col-dense")
		div(class="col-span-1 p-1")
			img(src="@/assets/icons/drum-lineal.png" class="h-16")
		div(class="col-span-2 flex p-1")
			PrayerTimer(:next-prayer="nextPrayer.date")
		div(class="col-span-3 flex items-end p-1")
			div(class="ms-auto")
				p(class="text-xs") Next prayer
				p(class="text-3xl font-semibold mb-0") {{ nextPrayer.name }}:
					span(class="ms-2") {{ nextPrayer.time }}
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { NextPrayerItem, PrayerTime, LOCALE_ARG, LOCALE_TDIGIT_OPTS } from '~/types/prayer-times'

export default defineComponent({
	name: 'PrayerDailyHeader',
	props: {
		todayPrayerTimes: {
			type: Object as () => PrayerTime | null,
			default: null
		}
	},
	computed: {
		nextPrayer () {
			let nextName = '--'
			const currentDT = new Date()
			const checkerDT = new Date()
			const isNext = (strTime: string) => {
				checkerDT.setHours(Number(strTime.slice(0, 2)))
				checkerDT.setMinutes(Number(strTime.slice(3, 5)))
				checkerDT.setSeconds(Number(strTime.slice(6, 8)))
				return checkerDT.getTime() > currentDT.getTime()
			}

			if (this.todayPrayerTimes) {
				if (isNext(this.todayPrayerTimes.imsak)) {
					nextName = 'Imsak'
				} else if (isNext(this.todayPrayerTimes.imsak)) {
					nextName = 'Imsak'
				} else if (isNext(this.todayPrayerTimes.fajr)) {
					nextName = 'Fajr'
				} else if (isNext(this.todayPrayerTimes.syuruk)) {
					nextName = 'Syuruk'
				} else if (isNext(this.todayPrayerTimes.dhuhr)) {
					nextName = 'Dhuhr'
				} else if (isNext(this.todayPrayerTimes.asr)) {
					nextName = 'Asr'
				} else if (isNext(this.todayPrayerTimes.maghrib)) {
					nextName = 'Maghrib'
				} else if (isNext(this.todayPrayerTimes.isha)) {
					nextName = 'Isha'
				}
			}

			const nextTime: string = this.todayPrayerTimes && nextName !== '--'
				? String(checkerDT.toLocaleTimeString(LOCALE_ARG, LOCALE_TDIGIT_OPTS))
				: '--'

			return {
				name: nextName,
				date: checkerDT,
				time: nextTime
			} as NextPrayerItem
		}
	}
})
</script>
