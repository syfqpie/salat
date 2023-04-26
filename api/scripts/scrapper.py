import datetime
import requests
import sqlite3

from enum import Enum
from bs4 import BeautifulSoup

from sqlalchemy import Date


BASE_URL = "https://www.e-solat.gov.my/index.php"
SCHEDULE_PARAM = "?siteId=24&pageId=24"
SQLITE_PATH = "sql_app.db"  # SQLITE path in virtualenv


class Period(Enum):
    """Period option for API"""

    WEEK = "week"
    MONTH = "month"
    YEAR = "year"
    DURATION = "duration"


class PrayerTimeScrapper:
    def __init__(self):
        self.root_search_url = requests.get(f"{BASE_URL}{SCHEDULE_PARAM}")
        self.root_soup = BeautifulSoup(self.root_search_url.content, "html.parser")
        self.zones = []
        self.zones_in_db = []
        self.scrapped = []

    def get_zones(self):
        """Scrapping zones from site search dropdown options"""
        print("\033[94mINFO\033[0m Scrapping zones..")
        zone_res = self.root_soup.find(id="inputZone")
        zone_labels = zone_res.select("optgroup[label]")

        for state in zone_labels:
            zone_state = state.get("label")
            zone_state_opts = state.select("option[value]")
            self.zones = self.zones + [
                {"code": zone.get("value"), "text": zone.text, "state": zone_state}
                for zone in zone_state_opts
            ]

        return self.zones

    def get_prayer_time(self, period=Period.MONTH.value):
        """Scrapping prayer times from site API"""
        print("\033[94mINFO\033[0m Scrapping prayer times..")
        # https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period={period}&zone={zone}
        base_req_url = f"{BASE_URL}?r=esolatApi/takwimsolat&period={period}&zone="

        for by_zone in self.zones:
            cur_zone = by_zone["code"]
            cur_req_url = f"{base_req_url}{cur_zone}"
            cur_res = requests.get(cur_req_url)
            cur_res_json = cur_res.json()

            if (
                cur_res.status_code == requests.codes.ok
                and cur_res_json["status"] == "OK!"
            ):
                code_key = cur_res_json["zone"]
                self.scrapped = self.scrapped + [
                    {f"{code_key}": cur_res_json["prayerTime"]}
                ]

    def init_db(self):
        conn = None
        try:
            conn = sqlite3.connect(SQLITE_PATH)
        except Exception as e:
            print(e)

        return conn

    def sync_zones(self):
        """
        Sync zones to database, will add new data is code
        doesn't exists in database. If new data is not same,
        will update the data in database
        """
        print("\033[94mINFO\033[0m Syncing zones..")

        def get_db_zones():
            """Fetch zones from database to compare"""
            select_sql = """
                SELECT *
                FROM zones;
            """
            curr = conn.cursor()
            curr.execute(select_sql)

            return curr.fetchall()

        def add_new_zone(new_code, new_text, new_state):
            """Insert new entry to database"""
            insert_sql = """
                INSERT INTO zones (code, text, state, created_at)
                VALUES (?, ?, ?, ?)
            """
            insert_val = (new_code, new_text, new_state, datetime.datetime.utcnow())
            curr = conn.cursor()
            curr.execute(insert_sql, insert_val)

        def patch_zone(new_code, new_text, new_state, id):
            """Patch entry in database"""
            insert_sql = """
                    UPDATE zones
                    SET code = ?,
                        text = ?,
                        state = ?,
                        updated_at = ?
                    WHERE id = ?
                """
            insert_val = (new_code, new_text, new_state, datetime.datetime.utcnow(), id)
            curr = conn.cursor()
            curr.execute(insert_sql, insert_val)

        if self.zones:
            conn = self.init_db()
            zones_in_db = get_db_zones()

            for zo in self.zones:
                from_db = [
                    db_zone for db_zone in zones_in_db if db_zone[1] == zo["code"]
                ]
                is_no_data = not from_db
                is_need_update = is_no_data or (
                    zo["code"] != from_db[0][1]
                    or zo["text"] != from_db[0][2]
                    or zo["state"] != from_db[0][3]
                )
                if not from_db:
                    add_new_zone(zo["code"], zo["text"], zo["state"])
                elif from_db and is_need_update:
                    patch_zone(zo["code"], zo["text"], zo["state"], from_db[0][0])

            conn.commit()
            self.zones_in_db = get_db_zones()
            conn.close()

    def sync_prayer_times(self):
        """
        Sync prayer times to database. Checks current month
        data in database, if current month data is available,
        will not syncs.

        TODO: make it simpler
        """
        print("\033[94mINFO\033[0m Syncing prayer times..")

        def get_db_prayer_times():
            select_sql = """
                SELECT *
                FROM prayer_times
                WHERE strftime('%m', date) = ?;
            """
            curr = conn.cursor()
            current_month_str = f"{datetime.datetime.now().month:02}"
            select_value = (current_month_str,)
            curr.execute(select_sql, select_value)

            return curr.fetchall()

        def add_new_prayer_time(**kwargs):
            insert_sql = """
                INSERT INTO prayer_times (zone_id, hijri_date, date, imsak, fajr, syuruk, dhuhr, asr, maghrib, isha)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            insert_val = (
                kwargs.get("zone_id"),
                kwargs.get("hijri"),
                kwargs.get("date"),
                kwargs.get("imsak"),
                kwargs.get("fajr"),
                kwargs.get("syuruk"),
                kwargs.get("dhuhr"),
                kwargs.get("asr"),
                kwargs.get("maghrib"),
                kwargs.get("isha"),
            )
            curr = conn.cursor()
            curr.execute(insert_sql, insert_val)
            print("\033[96mADDED\033[0m Adding", kwargs.get("zone"), kwargs.get("date"))

        conn = self.init_db()
        current_month_data_db = get_db_prayer_times()

        if not current_month_data_db:
            for by_zone_code in self.scrapped:
                current_zone = list(by_zone_code.keys())[0]
                zone_id = [
                    zdb[0] for zdb in self.zones_in_db if zdb[1] == current_zone
                ][0]

                if not zone_id:
                    continue

                for daily in by_zone_code[current_zone]:
                    converted_date = datetime.datetime.strptime(
                        daily["date"], "%d-%b-%Y"
                    ).strftime("%Y-%m-%d")
                    add_new_prayer_time(
                        zone=current_zone,
                        zone_id=zone_id,
                        hijri=daily["hijri"],
                        date=converted_date,
                        imsak=daily["imsak"],
                        fajr=daily["fajr"],
                        syuruk=daily["syuruk"],
                        dhuhr=daily["dhuhr"],
                        asr=daily["asr"],
                        maghrib=daily["maghrib"],
                        isha=daily["isha"],
                    )

            print("\033[92mDONE\033[0m Completed")
        else:
            print(
                "\033[93mERROR\033[0m!! Data not synced, current month data is already in database"
            )

        conn.commit()
        conn.close()


if __name__ == "__main__":
    """
    TODO: add argument parser
    """
    scrapper = PrayerTimeScrapper()

    # Stage 1: get zones
    scrapper.get_zones()
    scrapper.sync_zones()

    # Stage 2: get prayer time
    scrapper.get_prayer_time()
    scrapper.sync_prayer_times()
