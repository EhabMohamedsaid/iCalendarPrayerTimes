import datetime
import json
import ics

year = str(datetime.date.today().year)

def read_json():
    with open("yearlyCalendarOutput/Calendar" + year +".json") as file:
        data = json.load(file)
    generate_calendar(data)

def generate_calendar(data):
    no_alarm = ics.Calendar()

    for key, value in dict.items(data['times']):
        date = key
        for k, v in dict.items(data['times'][key]):
            if not k == "date":
                if not k == "asr_2":
                    silent_event = ics.Event()

                    prayer_time = date + ' ' + v + ':00'

                    # Replace underscores with spaces
                    name = k.replace("_", " ")

                    # Capitalize every word
                    silent_event.name = name.title()
                    silent_event.begin = prayer_time

                    no_alarm.events.add(silent_event)

    with open('GeneratedCalendar/prayerCalendarNoAlarm' + year + '.ics', 'w') as my_file:
        my_file.writelines(no_alarm)
