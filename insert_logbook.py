import os

import requests

from constants import months, month_start_from

url = "https://activity-enrichment.apps.binus.ac.id/LogBook/StudentSave"
cookie = os.environ["COOKIE"]

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': cookie
}


def insert(logbook):
    date = logbook.get("date")
    title = logbook.get("title")
    desc = logbook.get("desc")

    month = int(date.split("-")[1])
    logbook_header_id = months[month - month_start_from]

    payload = f"model%5BID%5D=00000000-0000-0000-0000-000000000000&model%5BLogBookHeaderID%5D={logbook_header_id}&model%5BDate%5D={date}T00%3A00%3A00&model%5BActivity%5D={title}&model%5BClockIn%5D=09%3A00+am&model%5BClockOut%5D=06%3A00+pm&model%5BDescription%5D={desc}&model%5Bflagjulyactive%5D=false"

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
