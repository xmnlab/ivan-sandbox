import pandas as pd


def cursor2df(cursor):
    col_names = [c.name for c in cursor.description]
    return pd.DataFrame(cursor.fetchall(), columns=col_names)