import { ActionTree, GetterTree, MutationTree } from 'vuex'

import { RootState } from '~/store'
import { PrayerTime, Zone } from '~/types/prayer-times'

export const state = () => ({
	weekly: [] as PrayerTime[],
	zones: [] as Zone[],
	savedZone: null as Zone | null
})

export type PrayerTimesModuleState = ReturnType<typeof state>

export const getters: GetterTree<PrayerTimesModuleState, RootState> = {
	today: (state) => {
		if (state.weekly.length > 0) {
			const today = new Date()
			const filtered = state.weekly.find(({ date }) => {
				const prayerTimeDate = new Date(date)
				return today.toLocaleDateString() === prayerTimeDate.toLocaleDateString()
			})

			return filtered
		}

		return null
	},
	tomorrow: (state) => {
		if (state.weekly.length > 0) {
			const today = new Date()
			today.setDate(today.getDate() + 1)
			const filtered = state.weekly.find(({ date }) => {
				const prayerTimeDate = new Date(date)
				return today.toLocaleDateString() === prayerTimeDate.toLocaleDateString()
			})

			return filtered
		}
	},
	zoneByState: (state) => {
		const byState: { [key: string]: any } = {}
		if (state.zones) {
			for (const zone of state.zones) {
				if (!(zone.state in byState)) {
					byState[zone.state] = []
				}

				byState[zone.state].push(zone)
			}
		}

		return byState
	}
}

export const mutations: MutationTree<PrayerTimesModuleState> = {
	UPDATE_DATA: (state, newData: PrayerTime[]) => (state.weekly = newData),
	UPDATE_ZONE: (state, newData: Zone[]) => (state.zones = newData),
	UPDATE_DEFAULT_ZONE: (state, newData: Zone) => (state.savedZone = newData)
}

export const actions: ActionTree<PrayerTimesModuleState, RootState> = {
	async getData ({ commit }) {
		try {
			const prayerTimes = await this.$axios.$get('api/v1/prayer-times/?zone=SGR01&weekly=True')
			commit('UPDATE_DATA', prayerTimes)
		} catch (e) {
			// placeholder for error handling
		}

		try {
			const zones = await this.$axios.$get('api/v1/zones/')
			const defaultZone = zones.find((zone: Zone) => zone.code === 'SGR01')
			commit('UPDATE_ZONE', zones)
			commit('UPDATE_DEFAULT_ZONE', defaultZone)
		} catch (e) {
			// placeholder for error handling
		}
	}
}
