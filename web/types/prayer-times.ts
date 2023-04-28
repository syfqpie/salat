/**
 * Interface for PrayerDaily component
 */
export interface PrayerTimeItem {
    /** Prayer time */
    name: string,

    /** Icon source */
    iconSrc: string
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
