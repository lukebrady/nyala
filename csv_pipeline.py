import json
import csv


# Pipeline that takes an in-memory CSV object and converts it to Python Dictionary.
# @param csv_obj: In-memory CSV file that will be converted to a Dictionary.
# @param fieldnames: The keys used in the Dictionary document.
# @returns json_array: Array of Dictionary objects that will entered into database.
def csv_to_dict(csv_obj, fieldnames):
    reader = csv.DictReader(csv_obj, fieldnames)
    dict_array = []
    for row in reader:
        if test_dictionary(dict(row), fieldnames) is True:
            dict_array.append(row)
        else:
            return
    print(dict_array)
    return dict_array


# Pipeline that takes an in-memory CSV object and converts it to JSON.
# Pipeline that takes an in-memory CSV object and converts it to JSON.
# @param csv_obj: In-memory CSV file that will be converted to JSON.
# @param fieldnames: The keys used in the JSON document.
# @returns json_array: Array of JSON objects that will entered into database.
def csv_to_json(csv_obj, fieldnames):
    reader = csv.DictReader(csv_obj, fieldnames)
    json_array = []
    for row in reader:
        if test_dictionary(dict(row), fieldnames) is True:
            dumped_row = json.dumps(row)
            json_array.append(dumped_row)
        else:
            return
    print(json_array)
    return json_array


# Helper function that will test if all fields are filled out.
# @param dictionary: The dictionary object that will be tested within the function.
# @param fieldnames: Values that the function will test against to check existence.
# @returns boolean: Returns True if all elements exist. Returns false if not.
def test_dictionary(dictionary, fieldnames):
    for x in range(0, len(fieldnames) - 1):
        if dictionary.get(fieldnames[x]) is None:
            return False
        else:
            return True


def main():
    c = open("C:\\Users\\lbrad23105\\Desktop\\test.csv", "r")
    d = open("C:\\Users\\lbrad23105\\Desktop\\test.csv", "r")
    csv_to_dict(c, ("Width","Height","Length","Area"))
    csv_to_json(d, ("Width", "Height", "Length", "Area"))

main()

