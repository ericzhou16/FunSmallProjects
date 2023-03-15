import requests
import re
import pickle

url = r"https://four11.eastsideprep.org/registrar/pdf_schedules?color=1&student_id={}&term_id=1&year_id=23"

with open('ssids.pickle', 'rb') as handle:
    track = pickle.load(handle)
# track = {}

# 4200 - 4900 before
# actual range: 2927 - 5342
#  there are some before 2927 (1 - 119, 2206) but those are either staff or really old
for i in range(2927, 5345):
    try:
        x = requests.get(url.format(i))
        d = x.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0]
        name = fname[6:fname.find("_schedule")]
        if name:
            track[i] = name
            print(f"{i}: {name}")
    except:
        continue

with open('ssids.pickle', 'wb') as handle:
    pickle.dump(track, handle)


print(track)


