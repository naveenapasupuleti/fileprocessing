import json
from csv import writer


def append_list_as_row(file_name, mode="a+", list_of_elem=[]):
    with open(file_name, mode, newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
        write_obj.close()


def append_list_as_row_json(file_name, mode="r+", json_data={}):
    with open(file_name, mode) as file:
        json.dump(json_data, file)

