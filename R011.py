#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
from datetime import datetime
from datetime import timedelta
dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
df = pd.read_excel('C:\\Users\\mzuev\\PycharmProjects\\pythonProject\\Project\\R011\\195.xls', parse_dates=['Дата документа'],date_parser=dateparse)
DateStart = datetime.fromisoformat(input())
DateFinish = datetime.fromisoformat(input())
df.loc[(df['Тип документа'] == 'ЭНВ') & (df['КБК'] % 1000 == 180) & (df['Дата документа'] >= DateStart - timedelta(days=15)) & (df['Дата документа']<=DateStart)
| (df['Тип документа'] == 'УНУ') & (df['КБК'] % 1000 == 180) & (df['Дата документа'] >= DateStart ) & (df['Дата документа']<=DateFinish)
| (df['Тип документа'] == 'ЭНВ') & (df['КБК'] % 1000 == 180)& (df['Дата документа'] >= DateStart ) & (df['Дата документа']<=DateFinish)
| (df['Тип документа'] == 'ЭДВ') & (df['КБК'] % 1000 == 180)& (df['Дата документа'] >= DateStart ) & (df['Дата документа']<=DateFinish)]


# In[ ]:




