# Author: Guilherme Mendes
# Exporting json data to excel file

import pandas as pd

def import_json_to_excel(json_data, excel_filename):
    df = pd.read_json(json_data)
    #print(df)
    excel = df.to_excel(excel_filename + ".xlsx")
    return excel