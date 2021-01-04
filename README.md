**File Processing Package:**

**Getting started:**

By using this package, we can Read and write CSV,XLSX,JSON files.

**Prerequisites:**

We need to install 

- Python 3.6 and above.
- PIP latest version.
- PyCharm

**Imports:**

We need to import following libraries.
- pip3 install pandas
- pip3 install openpyxl
- pip3 install writer

**Testing the package:**

        Run "Python3" in terminal

**Import the file processing package methods in terminal:**

       from fileprocessing_package import FileProcess

**Add the below command to test the methods**

If you are Reading/Writting a File:

Example for CSV File:

        FileProcess.read("filepath")
        FileProcess.write("filepath","a+",[28,'mouri','vizag'])

Example for XLSX file:

        FileProcess.read("filepath")
        FileProcess.write("filepath","a+",[('vzg',22,45),('hyd',21,56),('mouri',20,60)])

Example for XLSX file:

        FileProcess.read("filepath")
        FileProcess.write("filepath","a+",{"ORIGIN_COUNTRY_NAME":"United States","DEST_COUNTRY_NAME":"Poland","count":62})


If you are converting CSV to Json:

        FileProcess.json_conversion("filepath","Destinationfilepath")
