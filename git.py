import pandas as pd 
import requests
from docx import Document 
import json 

df = pd.read_excel(r'Meerim.xlsx', sheet_name='list')
print(df)

doc = Document('Meerim4.docx')
pars = doc.paragraphs

for i in pars:
    print(i.text)