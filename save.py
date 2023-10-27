import csv

def save_to_scv(jobs):
    file = open('jobs.csv', 'w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'town', 'link'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return