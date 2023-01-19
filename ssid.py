import requests
import re
import pickle

# https://four11.eastsideprep.org/registrar/pdf_schedules?color=1&student_id=4880&term_id=1&year_id=23
url_front = r"https://four11.eastsideprep.org/registrar/pdf_schedules?color=1&student_id="
url_back = "&term_id=1&year_id=23"

with open('ssids.pickle', 'rb') as handle:
    track = pickle.load(handle)

# for i in range(4200, 4900):
#     try:
#         x = requests.get(url_front + str(i) + url_back)
#         d = x.headers['content-disposition']
#         fname = re.findall("filename=(.+)", d)[0]
#         name = fname[6:fname.find("_schedule")]
#         track[name] = i
#         print(f"{name}: {i}")
#     except:
#         continue
#
# with open('ssids.pickle', 'wb') as handle:
#     pickle.dump(track, handle)
print(track)


