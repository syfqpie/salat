export const LOCALE_ARG: Intl.LocalesArgument = []
export const LOCALE_OPTS: Intl.DateTimeFormatOptions = { hour12: true, hour: 'numeric', minute: 'numeric' }
export const LOCALE_TIMER_ARG: Intl.LocalesArgument = 'en-US'
export const LOCALE_TIMER_OPTS: Intl.NumberFormatOptions = { minimumIntegerDigits: 2, useGrouping: false }

/**
 * Interface for PrayerDaily component
 */
export interface PrayerTimeItem {
    /** Prayer time */
    name: string,

    /** Icon source */
    iconSrc: string,

    time?: string
}

/**
 * Base interface for prayer times
 */
export interface PrayerTime {
    id: number
    zone_code: string
    hijri_date: string
    date: string
    imsak: string
    fajr: string
    syuruk: string
    dhuhr: string
    asr: string
    maghrib: string
    isha: string
}
