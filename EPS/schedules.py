import pdfquery as pdfq
import requests
from collections import defaultdict
import pickle
import re

with open('ssids.pickle', 'rb') as handle:
    track = pickle.load(handle)
ids = track.values()
# ids = [4879]
ids = [4855]

url = r"https://four11.eastsideprep.org/registrar/pdf_schedules?color=1&student_id={}&term_id=3&year_id=23"

for _id in ids:
    try:
        x = requests.get(url.format(_id), allow_redirects=True)
        print(str(_id), "worked")
        with open('test.pdf', 'wb') as save_thing:
            pickle.dump(x.content, save_thing)
    except:
        print(str(_id), "failed")
        continue

file = r'EPS/test.pdf'
pdf = pdfq.PDFQuery(file)
pdf.load()
thing = defaultdict(list)
texts = list(pdf.pq('LTTextLineHorizontal:overlaps_bbox("100, 250, 100, 800")'))
for text in texts:
    if '-' in text.text:
        print(text.text)
        thing[text.text].append('user')

print(thing)
