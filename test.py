import pickle

with open('EPS/all_courses.pickle', 'rb') as handle:
    courses = pickle.load(handle)

print(courses)
