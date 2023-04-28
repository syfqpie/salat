import { ActionTree, GetterTree, MutationTree } from 'vuex'

import { RootState } from '~/store'
import type { PrayerTime } from '~/types/prayer-times'

export const state = () => ({
	weekly: [] as PrayerTime[]
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
	}
}

export const mutations: MutationTree<PrayerTimesModuleState> = {
	UPDATE_DATA: (state, newData: PrayerTime[]) => (state.weekly = newData)
}

export const actions: ActionTree<PrayerTimesModuleState, RootState> = {
	async getData ({ commit }) {
		const results = await this.$axios.$get('api/v1/prayer-times/?zone=JHR02&weekly=True')
		commit('UPDATE_DATA', results)
	}
}
