import json
import pandas as pd
from csv import writer
import xlsxwriter
import openpyxl
from openpyxl import load_workbook

def fileprocess(fileExt,method,dict):
    if fileExt.endswith('.csv') and method == "r":
        df = pd.read_csv(fileExt)
        print("main csv read")
        return df

    elif fileExt.endswith('.csv') and method == "w":
        def append_list_as_row(file_name, list_of_elem):
            print(list_of_elem)
            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(list_of_elem)
                write_obj.close()
        append_list_as_row(fileExt, dict)

    elif fileExt.endswith('.json') and method == "r":
        df = pd.read_json(fileExt, lines=True)
        return df

    elif fileExt.endswith(".json") and method=="w":
        def append_list_as_row(file_name, json_data):
            with open(fileExt, "r+") as file:
                data = json.load(file)
                data.update(json_data)
                file.seek(0)
                json.dump(data, file)
        append_list_as_row(fileExt, dict)
    elif fileExt.endswith(".xlsx") and method == "r":
        df_read = pd.read_excel(fileExt)
        return df_read

    elif fileExt.endswith(".xlsx") and method == "w":
        book = load_workbook(fileExt)
        df = pd.DataFrame(dict)
        wb = pd.ExcelWriter(fileExt, engine='openpyxl')
        wb.book = load_workbook(fileExt)
        wb.save()
        wb.close()
        return df

def JsonConversion(fileExt,method,CsvToJson):
    if fileExt.endswith('.csv') and method == "r":
        df = pd.read_csv(fileExt)
        df.to_json(CsvToJson)
        print("read")
        return df











