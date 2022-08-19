# Author: Guilherme Mendes
# Extrating all .ext files from directory and subdirectories and store them into a excel file

import os
import sys
import search_files as sf
import store_to_excel as se

def check_extension_format(extension):
    return extension[0] == '.'

def check_valid_diretory(directory):
    return os.path.isdir(directory)

def check_valid_filename(filename):
    return not os.path.isfile(filename + ".xlsx")
       
def main():
    if len(sys.argv) != 4:
        print("Error: Incorrect usage.")
        print("Must be: python extract_files.py <extension> <directory> <excel_filename>")
        print("Example: python extract_files.py .pdf C:\\Path\\Dir or C:/Path/Dir filename")
        return 1
    
    extension = sys.argv[1]
    directory = sys.argv[2]
    excel_filename = sys.argv[3]

    if not check_extension_format(extension):
        print("Error: Invalid extension format. Must be .<extension>")
        print("Example: .pdf, .py, .js")
        return 2

    if not check_valid_diretory(directory):
        print("Error: The respective directory does not exist.")
        print("Please introduce a valid directory.")
        print("Example: C:\\Path\\Dir or C:/Path/Dir")
        return 3

    if not check_valid_filename(excel_filename):
        print("Error: The file with the respective name already exist.")
        print("Please introduce a different name.")
        return 3
    
    print("> Extract Files by Extension application")

    try:
        print("> Extrating data...")
        (data, length) = sf.search_files(extension, directory)
    except:
        print(f"> Something went wrong when search by {extension} files...")
    finally:
        print(data)
        print(f"> Number of '{extension}' files found: {(length)}")

    try:
        se.import_json_to_excel(data, excel_filename)
    except:
        print(f"> Something went wrong when exporting to excel file...")
    finally:
        print("\n> Done.")
        print(f"> All the data was stored into {excel_filename}.xlsx")

    return 0

if __name__ == "__main__":
    main()