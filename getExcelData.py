import os
import pandas as pd
def getExceldata(parent_dir):
    excel_chart = "PATH_TO_YOUR_EXCEL_FILE"
    excel_file = parent_dir+excel_chart
    df = pd.read_excel(excel_file)
    return df