export const LOCALE_ARG = []
export const LOCALE_OPTS: Intl.DateTimeFormatOptions = { hour12: true, hour: 'numeric', minute: 'numeric' }
export const LOCALE_TDIGIT_OPTS: Intl.DateTimeFormatOptions = { hour: 'numeric', minute: '2-digit' }
export const LOCALE_TIMER_ARG = 'en-US'
export const LOCALE_TIMER_OPTS: Intl.NumberFormatOptions = { minimumIntegerDigits: 2, useGrouping: false }

export interface PrayerTimeItem {
    /** Prayer time */
    name: string,

    /** Icon source */
    iconSrc: string,

    time?: string
}

export interface NextPrayerItem {
    name: string,
    date: Date,
    time: string
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
