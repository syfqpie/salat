<template lang="pug">
div(class="bg-green-300 shadow-lg rounded-lg p-2")
	p
		span(
			class="bg-green-100 text-green-800 text-xs \
			font-medium px-2.5 py-0.5 rounded"
		) {{ todayDates?.normal }} / {{  todayDates?.hijri }}
	div(class="grid grid-cols-7")
		template(v-for="item in prayerTime")
			div(class="p-3 w-auto text-center")
				img(:src="require(`@/assets/${item.iconSrc}`)" class="h-16 mb-1 mx-auto")
				p(class="mb-0 text-xs font-semibold") {{ item.name }}
				p(class="mb-0 text-xs") {{ item.time }}
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { PrayerTime, PrayerTimeItem, LOCALE_ARG, LOCALE_OPTS } from '~/types/prayer-times'

export default defineComponent({
	name: 'PrayerDailyItem',
	props: {
		todayItems: {
			type: Object as () => PrayerTime | null,
			default: null
		},
		todayDates: {
			type: Object as () => { normal: string | undefined; hijri: string | undefined; } | undefined,
			default: undefined
		}
	},
	data () {
		return {
			prayerTime: [
				{
					name: 'Imsak',
					iconSrc: 'icons/isha-lineal.png',
					time: '--:--'
				},
				{
					name: 'Fajr',
					iconSrc: 'icons/fajr-lineal.png',
					time: '--:--'
				},
				{
					name: 'Syuruk',
					iconSrc: 'icons/syuruk-lineal.png',
					time: '--:--'
				},
				{
					name: 'Dhuhr',
					iconSrc: 'icons/dhuhr-lineal.png',
					time: '--:--'
				},
				{
					name: 'Asr',
					iconSrc: 'icons/asr-lineal.png',
					time: '--:--'
				},
				{
					name: 'Maghrib',
					iconSrc: 'icons/maghrib-lineal.png',
					time: '--:--'
				},
				{
					name: 'Isha',
					iconSrc: 'icons/isha-lineal.png',
					time: '--:--'
				}
			] as PrayerTimeItem[]
		}
	},
	watch: {
		todayItems: {
			handler (val) {
				if (val) {
					const currentDate = new Date()
					const oldPrayerTime = [...this.prayerTime]
					for (const currentKey in val) {
						const currentTimeIndex = this.prayerTime.findIndex(
							(item) => {
								return String(item.name.toLowerCase()) === String(currentKey)
							}
						)

						if (currentTimeIndex >= 0) {
							currentDate.setHours(Number(val[currentKey].slice(0, 2)))
							currentDate.setMinutes(Number(val[currentKey].slice(3, 5)))
							currentDate.setSeconds(0)
							oldPrayerTime[currentTimeIndex].time = currentDate.toLocaleTimeString(LOCALE_ARG, LOCALE_OPTS)
						}
					}

					this.prayerTime = oldPrayerTime
				}
			}
		}
	}
})
</script>
