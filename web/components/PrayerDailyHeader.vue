<template lang="pug">
div(class="p-3 rounded-lg mb-4 bg-green-300 shadow-lg relative")
	div(class="grid grid-cols-2 md:grid-cols-12")
		div(class="col-span-1 md:col-span-6 order-2 md:order-1 flex items-end p-1")
			div(class="me-auto")
				p(class="text-sm") Next prayer time
				p(class="text-lg md:text-4xl font-semibold mb-0") {{ nextPrayer.name }}:
					span(class="ms-2") {{ nextPrayer.time }}
		div(class="col-span-1 md:col-span-4 order-1 md:order-2 flex p-1")
			PrayerTimer(
				:next-prayer="nextPrayer.date"
				@onEndTimer="refreshHeader"
			)
		div(class="col-span-2 p-1 order-3 hidden md:block")
			img(src="@/assets/icons/drum-lineal.png" class="h-24")
	p(class="mb-0")
		span(
			class="bg-green-100 text-green-800 text-xs \
			font-medium mr-0.5 px-2.5 py-0.5 rounded line-clamp-1 md:line-clamp-none md:inline-block"
		) {{ zoneInfo?.text }}
		a(
			class="px-2.5 py-0.5 text-xs font-medium text-center \
			bg-gray-100 text-gray-800 rounded hover:bg-green-400 \
			focus:shadow cursor-pointer"
			@click="toggleChooseZone"
		) Change
	PrayerZoneSelect(
		:zone-opts="zoneByState"
		:zones="zones"
		:current-zone="zoneInfo"
		@onCancel="toggleChooseZone()"
		v-if="isChooseZone")
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { NextPrayerItem, PrayerTime, Zone, LOCALE_ARG, LOCALE_TDIGIT_OPTS } from '~/types/prayer-times'

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
	data () {
		return {
			isChooseZone: false as boolean,
			checkerDT: new Date() as Date
		}
	},
	computed: {
		nextPrayer () {
			let nextName = '--'
			const currentDT: Date = new Date()
			const checkerDT: Date = new Date(this.checkerDT.getTime())
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
		},
		zoneInfo (): Zone | null {
			return this.$store.state.prayerTimes.savedZone
		},
		zones (): Zone[] {
			return this.$store.state.prayerTimes.zones as Zone[]
		},
		zoneByState (): { [key: string]: any } {
			return this.$store.getters['prayerTimes/zoneByState']
		}
	},
	methods: {
		toggleChooseZone () {
			this.isChooseZone = !this.isChooseZone
		},
		refreshHeader () {
			this.checkerDT = new Date()
		}
	}
})
</script>
