from fileprocessing_package import ReadWriteFile
# file_extension ='students.csv'
file_extension ='Corp_Chain_poc_csv.csv'
# file_extension ='test.xlsx'
dict = [28,'sravanthi','morning']

# dict=[('Lata',22,45),('Anil',21,56),('John',20,60)]
#
# dict={'locality': ['ongole','vizag','atp','kodur'],
#                    'pin': [232,2632,322,32]}
ReadWriteFile.fileprocess(file_extension, "r", dict)


              #####CSV to JSON file conversion#####

CsvToJson = 'csv_json.json'

ReadWriteFile.JsonConversion(file_extension, "r", CsvToJson)