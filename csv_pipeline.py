import csv
import json

#def csv_queue(path):

def csv_pipeline(csv, fieldnames):
    csvfile = open('C:\\Users\\lbrad23105\\Desktop\\test.csv', 'r')
    reader = csv.DictReader(csvfile, fieldnames)
    j = []
    for row in reader:
        if test_dictionary(dict(row), fieldnames) is True:
            dumped_row = json.dumps(row)
            j.append(dumped_row)
        else:
            return
    print(j)


def test_dictionary(dictionary, fieldnames):
    for x in range(0, len(fieldnames) - 1):
        if dictionary.get(fieldnames[x]) is "":
            return False
        else:
            return True


def main():
    csv_pipeline(("Width","Height","Length","Area"))

main()

