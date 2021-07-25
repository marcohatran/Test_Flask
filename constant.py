import pandas as pd

"""
# Constant API_KEY, read mkad_points from file 'mkad.csv'
"""
API_KEY = "a621fc42-6fcb-4a57-932c-7ff8bd852264"

df = pd.read_csv("mkad.csv")
mkad_points = list(df.to_records(index=False))
