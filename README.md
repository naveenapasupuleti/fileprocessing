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
- pip3 install xlsxwriter
- pip3 install openpyxl
- pip3 install writer

**Testing the package:**

Create a file to test the package:

**Example:**

   "PackageTestingFile.py"

**Import the file processing package in your file:**

       from FileProcessingPackage import ReadWriteFile

**Add the below code to test the package**

If you are Reading a File pass this parameters:

        ReadWriteFile.fileprocess(file_extension, "r", dict)

**Example:**

  if you are reading csv file follow this code example:
     
        from FileProcessingPackage import ReadWriteFile
        file_extension ='filename.csv' 
        dict = [28,'mouritech','hyderabad'] 
        ReadWriteFile.fileprocess(file_extension, "r", dict)

if you are Writing a file pass this parameters:

        ReadWriteFile.fileprocess(file_extension, "w", dict)

**Example:**

  if you are writing csv file follow this code example:

        from FileProcessingPackage import ReadWriteFile
        file_extension ='filename.csv' 
        dict = [28,'mouritech','hyderabad'] 
        ReadWriteFile.fileprocess(file_extension, "w", dict)

**Run your file:**

     "python(filename).py"







