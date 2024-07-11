import time

from insert_logbook import insert
import csv


def convert_to_logbook(row):
    return {
        "date": row[0],
        "title": row[1],
        "desc": row[2]
    }


with open('enrichment.csv', mode='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        logbook = convert_to_logbook(lines)
        insert(logbook)
        time.sleep(1)
