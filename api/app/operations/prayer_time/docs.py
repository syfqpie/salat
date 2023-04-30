from fastapi import status


ZONES_DESCRIPTION = "Get all zones or filter by state"
ZONES_PARAMETERS = {
    "state": {"title": "State", "description": "state to filter", "example": "Melaka"}
}
ZONES_EXTRA = {
    "description": ZONES_DESCRIPTION,
    "summary": "Get zones",
    "responses": {
        status.HTTP_200_OK: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "code": "WLY01",
                            "text": "WLY01 - Kuala Lumpur, Putrajaya",
                            "state": "Wilayah Persekutuan",
                            "id": 58,
                            "created_at": "2023-04-26T12:28:47.712847",
                            "updated_at": None,
                        },
                        {
                            "code": "WLY02",
                            "text": "WLY02 - Labuan",
                            "state": "Wilayah Persekutuan",
                            "id": 59,
                            "created_at": "2023-04-26T12:28:47.712851",
                            "updated_at": None,
                        },
                    ]
                }
            },
        }
    },
}


PRAYER_TIMES_DESCRIPTION = "Get all weekly or monthly prayer times for the given zone"
PRAYER_TIMES_PARAMETERS = {
    "zone": {"title": "Zone", "description": "zone to filter", "example": "WLY01"},
    "weekly": {
        "title": "Is getting weekly data?",
        "description": "Flag to specify weekly or monthly data",
        "example": "true",
    },
}
PRAYER_TIMES_EXTRA = {
    "description": PRAYER_TIMES_DESCRIPTION,
    "summary": "Get prayer times",
    "responses": {
        status.HTTP_200_OK: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "hijri_date": "1444-10-03",
                            "date": "2023-04-24",
                            "imsak": "05:35:00",
                            "fajr": "05:45:00",
                            "syuruk": "06:55:00",
                            "dhuhr": "13:03:00",
                            "asr": "16:18:00",
                            "maghrib": "19:07:00",
                            "isha": "20:18:00",
                            "id": 24,
                            "zone_code": "JHR01",
                        },
                        {
                            "hijri_date": "1444-10-04",
                            "date": "2023-04-25",
                            "imsak": "05:35:00",
                            "fajr": "05:45:00",
                            "syuruk": "06:55:00",
                            "dhuhr": "13:03:00",
                            "asr": "16:18:00",
                            "maghrib": "19:07:00",
                            "isha": "20:18:00",
                            "id": 25,
                            "zone_code": "JHR01",
                        },
                    ]
                }
            },
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Bad request",
            "content": {
                "application/json": {"example": {"detail": "Zone is required"}}
            },
        },
    },
}
