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

       from fileprocessing_package import fileprocess, JsonConversion

**Add the below command to test the methods**

If you are Reading/Writting a File:

Example for CSV File:

        fileprocess("filepath","r",{})
        fileprocess("filepath","w",[28,'mouri','vizag'])

If you are converting CSV to Json:

        JsonConversion("filepath","r","Destinationfilepath")
