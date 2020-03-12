"""Connection settings."""
import os
from pathlib import Path

import ibis
import pandas as pd
from pyspark.sql import SparkSession
import pyspark.sql.types as pt
import numpy as np


data_directory = Path(
    os.path.join(
        os.path.dirname(ibis.__path__[0]),
        'ci',
        'ibis-testing-data'
    )
)

# connection settings
conf = {}

# omniscidb
conf['omniscidb'] = dict(
    host='localhost', port=6274, 
    user='admin', password='HyperInteractive', 
    database='ibis_testing'
)

# pandas
conf['pandas'] = {
    'dictionary': {
        'functional_alltypes': pd.read_csv(
            str(data_directory / 'functional_alltypes.csv'),
            index_col=None,
            dtype={'bool_col': bool, 'string_col': str},
            parse_dates=['timestamp_col'],
            encoding='utf-8',
        ),
        'batting': pd.read_csv(str(data_directory / 'batting.csv')),
        'awards_players': pd.read_csv(
            str(data_directory / 'awards_players.csv')
        ),
    }
}

# csv
conf['csv'] = {'path': data_directory}

# parquet
conf['parquet'] = {'dictionary': data_directory }

# sqlite
conf['sqlite'] = {
    'path': str(data_directory / 'ibis_testing.db')
}

# postgres
conf['postgres'] = dict(
    host='localhost',
    port=5432,
    user='postgres',
    password='postgres',
    database='ibis_testing'
)

# mysql
conf['mysql'] = dict(
    host='localhost',
    port=3307,
    user='ibis',
    password='ibis',
    database='ibis_testing'
)

# clickhouse
conf['clickhouse'] = dict(
    host='localhost',
    port=9000,
    user='default',
    password='',
    database='ibis_testing'
)

# impala
_hdfs_client = ibis.hdfs_connect(
    host='impala',
    port=50070,
    auth_mechanism='NOSASL',
    verify=True,
    user='hdfs',
)
conf['impala'] = dict(
    host='localhost',
    port=21050,
    auth_mechanism='NOSASL',
    hdfs_client=_hdfs_client,
    database='ibis_testing',
)

# spark
conf['pyspark'] = dict(
    session=SparkSession.builder.getOrCreate()
)
conf['spark'] = dict(
    spark_session=SparkSession.builder.getOrCreate()
)


def post_connection_spark(con):
    _spark_testing_client = con
    s = _spark_testing_client._session

    df_functional_alltypes = s.read.csv(
        path=str(data_directory / 'functional_alltypes.csv'),
        schema=pt.StructType(
            [
                pt.StructField('index', pt.IntegerType(), True),
                pt.StructField('Unnamed: 0', pt.IntegerType(), True),
                pt.StructField('id', pt.IntegerType(), True),
                # cast below, Spark can't read 0/1 as bool
                pt.StructField('bool_col', pt.ByteType(), True),
                pt.StructField('tinyint_col', pt.ByteType(), True),
                pt.StructField('smallint_col', pt.ShortType(), True),
                pt.StructField('int_col', pt.IntegerType(), True),
                pt.StructField('bigint_col', pt.LongType(), True),
                pt.StructField('float_col', pt.FloatType(), True),
                pt.StructField('double_col', pt.DoubleType(), True),
                pt.StructField('date_string_col', pt.StringType(), True),
                pt.StructField('string_col', pt.StringType(), True),
                pt.StructField('timestamp_col', pt.TimestampType(), True),
                pt.StructField('year', pt.IntegerType(), True),
                pt.StructField('month', pt.IntegerType(), True),
            ]
        ),
        mode='FAILFAST',
        header=True,
    )
    df_functional_alltypes = df_functional_alltypes.withColumn(
        "bool_col", df_functional_alltypes["bool_col"].cast("boolean")
    )
    df_functional_alltypes.createOrReplaceTempView('functional_alltypes')

    df_batting = s.read.csv(
        path=str(data_directory / 'batting.csv'),
        schema=pt.StructType(
            [
                pt.StructField('playerID', pt.StringType(), True),
                pt.StructField('yearID', pt.IntegerType(), True),
                pt.StructField('stint', pt.IntegerType(), True),
                pt.StructField('teamID', pt.StringType(), True),
                pt.StructField('lgID', pt.StringType(), True),
                pt.StructField('G', pt.IntegerType(), True),
                pt.StructField('AB', pt.DoubleType(), True),
                pt.StructField('R', pt.DoubleType(), True),
                pt.StructField('H', pt.DoubleType(), True),
                pt.StructField('X2B', pt.DoubleType(), True),
                pt.StructField('X3B', pt.DoubleType(), True),
                pt.StructField('HR', pt.DoubleType(), True),
                pt.StructField('RBI', pt.DoubleType(), True),
                pt.StructField('SB', pt.DoubleType(), True),
                pt.StructField('CS', pt.DoubleType(), True),
                pt.StructField('BB', pt.DoubleType(), True),
                pt.StructField('SO', pt.DoubleType(), True),
                pt.StructField('IBB', pt.DoubleType(), True),
                pt.StructField('HBP', pt.DoubleType(), True),
                pt.StructField('SH', pt.DoubleType(), True),
                pt.StructField('SF', pt.DoubleType(), True),
                pt.StructField('GIDP', pt.DoubleType(), True),
            ]
        ),
        header=True,
    )
    df_batting.createOrReplaceTempView('batting')

    df_awards_players = s.read.csv(
        path=str(data_directory / 'awards_players.csv'),
        schema=pt.StructType(
            [
                pt.StructField('playerID', pt.StringType(), True),
                pt.StructField('awardID', pt.StringType(), True),
                pt.StructField('yearID', pt.IntegerType(), True),
                pt.StructField('lgID', pt.StringType(), True),
                pt.StructField('tie', pt.StringType(), True),
                pt.StructField('notes', pt.StringType(), True),
            ]
        ),
        header=True,
    )
    df_awards_players.createOrReplaceTempView('awards_players')

    df_simple = s.createDataFrame([(1, 'a')], ['foo', 'bar'])
    df_simple.createOrReplaceTempView('simple')

    df_struct = s.createDataFrame([((1, 2, 'a'),)], ['struct_col'])
    df_struct.createOrReplaceTempView('struct')

    df_nested_types = s.createDataFrame(
        [([1, 2], [[3, 4], [5, 6]], {'a': [[2, 4], [3, 5]]})],
        [
            'list_of_ints',
            'list_of_list_of_ints',
            'map_string_list_of_list_of_ints',
        ],
    )
    df_nested_types.createOrReplaceTempView('nested_types')

    df_complicated = s.createDataFrame(
        [({(1, 3): [[2, 4], [3, 5]]},)], ['map_tuple_list_of_list_of_ints']
    )
    df_complicated.createOrReplaceTempView('complicated')

    df_udf = s.createDataFrame(
        [('a', 1, 4.0, 'a'), ('b', 2, 5.0, 'a'), ('c', 3, 6.0, 'b')],
        ['a', 'b', 'c', 'key'],
    )
    df_udf.createOrReplaceTempView('udf')

    df_udf_nan = s.createDataFrame(
        pd.DataFrame(
            {
                'a': np.arange(10, dtype=float),
                'b': [3.0, np.NaN] * 5,
                'key': list('ddeefffggh'),
            }
        )
    )
    df_udf_nan.createOrReplaceTempView('udf_nan')

    df_udf_null = s.createDataFrame(
        [
            (float(i), None if i % 2 else 3.0, 'ddeefffggh'[i])
            for i in range(10)
        ],
        ['a', 'b', 'key'],
    )
    df_udf_null.createOrReplaceTempView('udf_null')

    df_udf_random = s.createDataFrame(
        pd.DataFrame(
            {
                'a': np.arange(4, dtype=float).tolist()
                + np.random.rand(3).tolist(),
                'b': np.arange(4, dtype=float).tolist()
                + np.random.rand(3).tolist(),
                'key': list('ddeefff'),
            }
        )
    )
    df_udf_random.createOrReplaceTempView('udf_random')
    return con