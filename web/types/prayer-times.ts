export const LOCALE_ARG = []
export const LOCALE_OPTS: Intl.DateTimeFormatOptions = { hour12: true, hour: 'numeric', minute: 'numeric' }
export const LOCALE_TDIGIT_OPTS: Intl.DateTimeFormatOptions = { hour: 'numeric', minute: '2-digit' }
export const LOCALE_TIMER_ARG = 'en-US'
export const LOCALE_TIMER_OPTS: Intl.NumberFormatOptions = { minimumIntegerDigits: 2, useGrouping: false }

/**
 * Interface for PrayerDaily component
 * @member {string} name Prayer time name (eg: Imsak / Fajr / Syuruk / Dhuhr / Asr / Maghrib / Isha)
 * @member {string} iconSrc Icon source (eg: icons/isha-lineal.png)
 * @member {string} time Prayer time string (eg: --:--)
 */
export interface PrayerTimeItem {
    /** Prayer time name */
    name: string;

    /** Icon source */
    iconSrc: string;

    /** Prayer time string */
    time?: string;
}

/**
 * Interface for PrayerDailyHeader component
 * @member {string} name Prayer time name (eg: Imsak / Fajr / Syuruk / Dhuhr / Asr / Maghrib / Isha)
 * @member {string} date Prayer time in Date (eg: Date Sat Apr 29 2023 05:44:00 GMT+0800 (Malaysia Time))
 * @member {string} time Prayer time string (eg: 5:44 am)
 */
export interface NextPrayerItem {
    /** Prayer time name */
    name: string;

    /** Prayer time in Date */
    date: Date;

    /** Prayer time string */
    time: string;
}

/**
 * Base interface for prayer times
 * @member {number} id Prayer time database ID (eg: 1)
 * @member {string} zone_code Zone code (eg: JHR01)
 * @member {string} hijri_date Prayer time hijri date (eg: 1444-10-03)
 * @member {string} date Prayer time normal date (eg: 2023-04-24)
 * @member {string} imsak Imsak time (eg: 05:35:00)
 * @member {string} fajr Fajr time (eg: 05:45:00)
 * @member {string} syuruk Syuruk time (eg: 06:55:00)
 * @member {string} dhuhr Dhuhr time (eg: 13:03:00)
 * @member {string} asr Asr time (eg: 16:18:00)
 * @member {string} maghrib Maghrib time (eg: 19:07:00)
 * @member {string} isha Isha time (eg: 20:18:00)
 */
export interface PrayerTime {
    /** Prayer time database ID */
    id: number;

    /** Zone code */
    zone_code: string;

    /** Prayer time hijri date */
    hijri_date: string;

    /** Prayer time normal date */
    date: string;

    /** Imsak time */
    imsak: string;

    /** Fajr time */
    fajr: string;

    /** Syuruk time */
    syuruk: string;

    /** Dhuhr time */
    dhuhr: string;

    /** Asr time */
    asr: string;

    /** Maghrib time */
    maghrib: string;

    /** Isha time */
    isha: string;
}

/**
 * Base interface for zones
 * @member {number} id Zone database ID (eg: 1)
 * @member {string} code Zone code (eg: JHR01)
 * @member {string} text Prayer time hijri date (eg: JHR02 - Johor Bahru, Kota Tinggi, Mersing, Kulai)
 * @member {string} state Prayer time normal date (eg: Johor)
 * @member {string} created_at Imsak time (eg: 2023-04-25T14:34:34.328964)
 * @member {string} updated_at Fajr time (eg: 2023-04-25T14:34:34.328964)
 */
export interface Zone {
    /** Zone database ID */
    id: number;

    /** Zone code */
    code: string;

    /** Zone text */
    text: string;

    /** Zone state */
    state: string;

    /** Entry created_at */
    created_at: string;

    /** Entry updated at  */
    updated_at: string | null;
}
