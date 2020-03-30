from datetime import datetime

import numpy as np
import pandas as pd
import ibis


def _date_generation(year_start: int, year_end : int):
    for d in range(1, 32):
        for m in range(1, 13):
            for y in range(year_start, year_end):
                try:
                    data = y, m, d
                    datetime(*data)
                    yield data
                except ValueError:
                    continue
                    

def salary_date_schema():
    return ibis.schema({
        'last_name': 'string',
        'salary': 'float64',
        'date_of_birth': 'date',
        'timestamp_of_birth': 'timestamp',
    }.items())


def salary_date():
    year_start= 2010
    year_end = 2021
    
    df_salary = pd.DataFrame(
        {
            'last_name': [
                'Name {} {} {}'.format(y, m, d)
                for y, m, d in _date_generation(year_start, year_end)
            ],
            'salary': [
                y * 10000000 + m * 1000 + d
                for y, m, d in _date_generation(year_start, year_end)
            ],
            'date_of_birth': [
                datetime(y, m, d)
                for y, m, d in _date_generation(year_start, year_end)
            ],
            'timestamp_of_birth': [
                np.datetime64(
                    '{}-{}-{}T{}:{}:{}.{}{}{}'.format(
                        y, 
                        str(m).rjust(2, '0'), 
                        str(d).rjust(2, '0'), 
                        str(m).rjust(2, '0'), 
                        str(m).rjust(2, '0'), 
                        str(m).rjust(2, '0'), 
                        str(m).rjust(2, '0'), 
                        str(m).rjust(2, '0'), 
                        str(d).rjust(2, '0'), 
                    )
                )
                for y, m, d in _date_generation(year_start, year_end)
            ],
        }
    )
    df_salary.date_of_birth = df_salary.date_of_birth.dt.date
    return df_salary