import datetime
import json
import ics
import pytz

year = str(datetime.date.today().year)


def read_json():
    with open("./yearlyCalendarOutput/Calendar" + year +".json") as file:
        data = json.load(file)
    generate_calendar(data)


def is_dst(dt,timeZone):
   aware_dt = timeZone.localize(dt)
   return aware_dt.dst() != datetime.timedelta(0,0)


timeZone = pytz.timezone("Europe/London")


def generate_calendar(data):
    no_alarm = ics.Calendar()

    for key, value in dict.items(data['times']):
        date = key
        dt = datetime.datetime.fromisoformat(date)
        for k, v in dict.items(data['times'][key]):
            if not k == "date":
                if not k == "asr_2":
                    silent_event = ics.Event()
                    prayer_time = date + ' ' + v + ':00'

                    # subtracts 1 hour from dst due to overcorrection on calendars
                    if is_dst(dt,timeZone):
                        time = datetime.datetime.strptime(v, '%H:%M')
                        adjusted_time = time - datetime.timedelta(hours=1)
                        timestamp = adjusted_time.time()
                        prayer_time = date + ' ' + timestamp.strftime('%H:%M') + ':00'

                    # Replace underscores with spaces
                    name = k.replace("_", " ")

                    # Capitalize every word
                    silent_event.name = name.title()
                    silent_event.begin = prayer_time

                    no_alarm.events.add(silent_event)

    with open('./GeneratedCalendar/LondonEnglandPrayerCalendar.ics', 'w') as my_file:
        my_file.writelines(no_alarm)
