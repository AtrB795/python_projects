from ics import Calendar
import requests
import arrow


#utc = arrow.utcnow()

url = 'https://esuli.kossuthgyakorlo.unideb.hu/calendar/export_execute.php?userid=2802&authtoken=f80e6c4208472c2b1140c6c91f393dc367f66601&preset_what=all&preset_time=monthnow'
cal = Calendar(requests.get(url).text)
#for event in cal.timeline.on(arrow.get('2021-03-15T21:23:58.970460+07:00')):
for event in cal.timeline.on(arrow.get(2021, 3, 14)):
    text = f'Esemény: {event.name}: \n{event.description}. Ekkor kezdődik: {event.begin}\n És ekkor fejeződik be: {event.end}'
    print(text)
