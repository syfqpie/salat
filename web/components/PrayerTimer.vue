<template lang="pug">
div(class="mt-auto me-auto")
	p(class="text-sm") To next prayer
	p(class="text-lg md:text-4xl mb-0") {{ timeLeft }}
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { LOCALE_TIMER_ARG, LOCALE_TIMER_OPTS } from '~/types/prayer-times'

export default defineComponent({
	name: 'PrayerTimer',
	props: {
		nextPrayer: {
			type: Date,
			default: null
		}
	},
	emits: [
		'onEndTimer'
	],
	data () {
		return {
			timeDistance: null as number | null
		}
	},
	computed: {
		hoursLeft (): string {
			if (this.timeDistance !== null && this.timeDistance >= 0) {
				const msToHour = (this.timeDistance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
				return Math.floor(msToHour).toLocaleString(LOCALE_TIMER_ARG, LOCALE_TIMER_OPTS)
			}

			return '--'
		},
		minutesLeft (): string {
			if (this.timeDistance !== null && this.timeDistance >= 0) {
				const msToMin = (this.timeDistance % (1000 * 60 * 60)) / (1000 * 60)
				return Math.floor(msToMin).toLocaleString(LOCALE_TIMER_ARG, LOCALE_TIMER_OPTS)
			}

			return '--'
		},
		secondsLeft (): string {
			if (this.timeDistance !== null && this.timeDistance >= 0) {
				const msToSec = (this.timeDistance % (1000 * 60)) / 1000
				return Math.floor(msToSec).toLocaleString(LOCALE_TIMER_ARG, LOCALE_TIMER_OPTS)
			}

			return '--'
		},
		timeLeft (): string {
			return String(`${this.hoursLeft}:${this.minutesLeft}:${this.secondsLeft}`)
		}
	},
	watch: {
		nextPrayer: {
			handler (value: Date | null) {
				if (value) {
					this.startTimer()
				}
			}
		}
	},
	methods: {
		startTimer () {
			const currentInterval = setInterval(() => {
				const currentMs = new Date().getTime()
				const targetMs = this.nextPrayer.getTime()
				const currentDistance = Math.round(targetMs - currentMs)

				if (currentDistance === 0 || currentDistance < 0) {
					this.timeDistance = 0
					this.$emit('onEndTimer')
					clearInterval(currentInterval)
				} else {
					this.timeDistance = (Math.round(targetMs - currentMs))
				}
			}, 1000)
		}
	}
})
</script>
