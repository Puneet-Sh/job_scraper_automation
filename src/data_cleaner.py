import pandas as pd
from datetime import datetime

def clean_and_save(jobs):
    df = pd.DataFrame(jobs)
    df.drop_duplicates(inplace=True)
    filename = f"reports/job_data_{datetime.now().strftime('%Y%m%d')}.csv"
    df.to_csv(filename, index=False)
    return filename
