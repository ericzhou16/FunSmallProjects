import pandas as pd
import pdfquery as pdfq
import re
import requests
import pickle

with open('ssids.pickle', 'rb') as handle:
    track = pickle.load(handle)
ids = list(track.keys())
url = r"https://four11.eastsideprep.org/registrar/pdf_schedules?color=1&student_id={}&term_id=3&year_id=23"
file = r'test.pdf'
# good = {}
removed = {}
with open('cleaned_ssids.pickle', 'rb') as handle:
    good = pickle.load(handle)

for _id in ids:
    if _id < 4200 or _id > 4900:
        try:
            x = requests.get(url.format(_id), allow_redirects=True)
            print(str(_id), "worked")
            with open(file, 'wb') as save_thing:
                pickle.dump(x.content, save_thing)
            pdf = pdfq.PDFQuery(file)
            pdf.load()
            texts = list(pdf.pq('LTTextLineHorizontal:overlaps_bbox("100, 250, 100, 800")'))
            if len(texts) < 5:
                removed[_id] = track[_id]
            else:
                good[_id] = track[_id]
        except:
            print(str(_id), "failed")

with open('cleaned_ssids.pickle', 'wb') as handle:
    pickle.dump(good, handle)

print()
print("Good:")
print(good)
print("Removed:")
print(removed)
