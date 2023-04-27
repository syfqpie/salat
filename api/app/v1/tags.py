from enum import Enum


class Tags(Enum):
    PRAYER_TIMES = "Prayer times"


tags_metadata = [
    {
        "name": Tags.PRAYER_TIMES.value,
        "description": "Operations with prayer times related",
    }
]
