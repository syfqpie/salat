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
		todayItems: {
			type: Object as () => PrayerTime | null,
			default: null
		},
		tomorrowItems: {
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

			if (this.todayItems) {
				if (isNext(this.todayItems.imsak)) {
					nextName = 'Imsak'
				} else if (isNext(this.todayItems.imsak)) {
					nextName = 'Imsak'
				} else if (isNext(this.todayItems.fajr)) {
					nextName = 'Fajr'
				} else if (isNext(this.todayItems.syuruk)) {
					nextName = 'Syuruk'
				} else if (isNext(this.todayItems.dhuhr)) {
					nextName = 'Dhuhr'
				} else if (isNext(this.todayItems.asr)) {
					nextName = 'Asr'
				} else if (isNext(this.todayItems.maghrib)) {
					nextName = 'Maghrib'
				} else if (isNext(this.todayItems.isha)) {
					nextName = 'Isha'
				} else if (this.tomorrowItems) {
					// after isha, so we will get tomorrow imsak time
					nextName = 'Imsak'
					isNext(this.tomorrowItems.imsak)
					checkerDT.setDate(checkerDT.getDate() + 1)
				}
			}

			const nextTime: string = this.todayItems && nextName !== '--'
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
