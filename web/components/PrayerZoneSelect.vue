<template lang="pug">
div(class="rounded-lg absolute top-0 left-0 right-0 h-full p-3 \
	w-full backdrop-blur-[3px] bg-green-300 bg-opacity-70 \
	content-end grid grid-cols-1 transition-all duration-75 ease-in-out")
	div
		label(
			for="zone_select"
			class="block mb-2 text-sm font-medium text-gray-900"
		) Select your location
		select(
			id="zone_select"
			v-model="selectedZoneStr"
			class="bg-gray-50 border border-gray-300 \
			text-gray-900 text-sm rounded-lg focus:ring-green-500 \
			focus:border-green-500 block w-full p-2.5")
			option(selected hidden) Choose a location
			template(v-for="(byState, key) in zoneOpts")
				optgroup(:label="key")
					template(v-for="zone in byState")
						option(:value="zone.code") {{ zone.text }}
	div(class="mt-2 text-end")
		button(
			type="button"
			class="me-1 px-3 py-2 text-xs font-medium text-center \
			text-gray-900 border border-green-500 rounded-lg \
			hover:bg-green-600 hover:text-white focus:shadow-lg"
			@click="onCancel"
		) Cancel
		button(
			type="button"
			class="px-3 py-2 text-xs font-medium text-center \
			text-gray-900 bg-green-500 rounded-lg hover:text-white \
			hover:bg-green-600 focus:shadow-lg"
			@click="onChange"
		) Change
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import { Zone } from '~/types/prayer-times'

export default defineComponent({
	name: 'PrayerZoneSelect',
	props: {
		zones: {
			type: Array as () => Zone[],
			default: () => []
		},
		currentZone: {
			type: Object as () => Zone | null,
			default: null
		},
		zoneOpts: {
			type: Object as () => { [key: string]: any } | null,
			default: null
		}
	},
	emits: [
		'onCancel'
	],
	data () {
		return {
			selected: null as Zone | null,
			selectedZoneStr: null as string | null
		}
	},
	watch: {
		currentZone: {
			handler (val) {
				if (val) {
					this.getSelected(val)
				}
			}
		}
	},
	mounted () {
		if (!this.selectedZoneStr && this.currentZone) {
			this.getSelected(this.currentZone)
		}
	},
	methods: {
		onChange () {
			const toSaveZone = this.zones.find(z => z.code === this.selectedZoneStr)

			if (toSaveZone) {
				this.$store.dispatch('prayerTimes/updateZone', toSaveZone)
			}

			this.$emit('onCancel')
		},
		onCancel () {
			// placeholder for zone change cancel button
			this.$emit('onCancel')
		},
		getSelected (val: Zone) {
			this.selected = val
			for (const zoneState in this.zoneOpts) {
				for (const byZone of this.zoneOpts[zoneState]) {
					if (byZone.code === val.code) {
						this.selectedZoneStr = byZone.code
					}
				}
			}
		}
	}
})
</script>
