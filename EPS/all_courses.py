import pandas as pd
import pdfquery as pdfq
import re
import requests
import pickle
from collections import defaultdict

with open('cleaned_ssids.pickle', 'rb') as handle:
    track = pickle.load(handle)
ids = list(track.keys())
url = r"https://four11.eastsideprep.org/registrar/pdf_schedules?color=1&student_id={}&term_id=3&year_id=23"
file = r'test.pdf'
courses = defaultdict(list)


for _id in ids:
    try:
        x = requests.get(url.format(_id), allow_redirects=True)
        print(str(track[_id]), "worked")
        with open(file, 'wb') as save_thing:
            pickle.dump(x.content, save_thing)
        pdf = pdfq.PDFQuery(file)
        pdf.load()
        texts = list(pdf.pq('LTTextLineHorizontal:overlaps_bbox("100, 250, 100, 800")'))
        for text in texts:
            if '-' in text.text:
                courses[text.text].append(track[_id])
    except:
        print(str(track[_id]), "failed")

with open('all_courses.pickle', 'wb') as handle:
    pickle.dump(courses, handle)

print(courses)
