import pandas as pd
from openpyxl import load_workbook
from .helper import append_list_as_row, append_list_as_row_json


class FileProcess(object):
    def read(self, file_path):
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
                return df
            elif file_path.endswith('.json'):
                df = pd.read_json(file_path, lines=True)
                return df
            elif file_path.endswith(".xlsx"):
                df = pd.read_excel(file_path)
                return df
            else:
                print("File extension is required")
        except Exception as e:
            print("Couldn't read file and Exception is: ", e)

    def write(self, file_path, mode="", data=None):
        try:
            if file_path.endswith('.csv'):
                append_list_as_row(file_path, mode, data)
            elif file_path.endswith(".json"):
                append_list_as_row_json(file_path, mode, data)
            elif file_path.endswith(".xlsx"):
                wb = load_workbook(file_path)
                page = wb.active
                for info in data:
                    page.append(info)
                wb.save(filename=file_path)
                return wb
            else:
                print("File extension is required")
        except Exception as e:
            print("Unable to fetch the data and Exception is: ", e)

    def json_conversion(self, file_path, csv_to_json):
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
                df.to_json(csv_to_json)
                return df
        except Exception as e:
            print("Unable to read the data and Exception is: ", e)

