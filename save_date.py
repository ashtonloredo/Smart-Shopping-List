from datetime import datetime as dt

def formatted_date():
  return dt.now().strftime("%m/%d/%Y %H:%M")
