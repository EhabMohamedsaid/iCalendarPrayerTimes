import datetime
import json
import ics

year = str(datetime.date.today().year)

def read_json():
    with open("yearlyCalendarOutput/Calendar" + year +".json") as file:
        data = json.load(file)
    generate_calendar(data)

def generate_calendar(data):
    c = ics.Calendar()
    for key, value in dict.items(data['times']):
        date = key
        for k, v in dict.items(data['times'][key]):
            if not k == "date":
                if not k == "asr_2":
                    e = ics.Event()
                    prayer_time = date + ' ' + v + ':00'
                    e.name = k
                    e.begin = prayer_time
                    c.events.add(e)

    with open('GeneratedCalendar/prayerCalendar' + year + '.ics', 'w') as my_file:
        my_file.writelines(c)
