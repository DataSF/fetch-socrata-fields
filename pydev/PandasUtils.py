# coding: utf-8
#!/usr/bin/env python

import pandas as pd
from pandas.io.json import json_normalize
import json

class PandasUtils:

  @staticmethod
  def loadCsv(fullpath):
    df = None
    try:
      df = pd.read_csv(fullpath)
    except Exception, e:
      print str(e)
    return df

  @staticmethod
  def convertDfToDictrows(df):
    return df.to_dict(orient='records')

  @staticmethod
  def mapFieldNames(df, field_mapping_dict):
    return df.rename(columns=field_mapping_dict)

  @staticmethod
  def groupbyCountStar(df, group_by_list):
    return df.groupby(group_by_list).size().reset_index(name='count')

  @staticmethod
  def renameCols(df, colMappingDict):
    df = df.rename(columns=colMappingDict)
    return df

  @staticmethod
  def groupbyCountStar(df, group_by_list):
    return df.groupby(group_by_list).size().reset_index(name='count')

  @staticmethod
  def makeLookupDictOnTwo(df, key_col, val_col):
      return dict(zip(df[key_col], df[val_col]))

  @staticmethod
  def makeDfFromJson(json_obj):
    df = json_normalize(json_obj)
    return df

  @staticmethod
  def fillNaWithBlank(df):
    return df.fillna("")


if __name__ == "__main__":
    main()
