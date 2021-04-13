#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
df = pd.read_excel('C:\\Users\\mzuev\\PycharmProjects\\pythonProject\\Project\\414r01.xls')
Total = df.loc[df['Показатель лицевого счета'].str.contains('РЕЗ_ПРШ_ПЕР_НУ|РЕЗ_ПРШ_ПЕР_ВН|ПОСТУПЛЕНИЯ_АУ|ПОСТУПЛЕНИЯ_БУ|ПОСТУПЛЕНИЯ_ВН|ВЫБЫТИЯ_АУ|ВЫБЫТИЯ_БУ|ВЫБЫТИЯ_ВН', case=False) & df['Идентификатор Массива']==1,['Остаток Дт', 'Остаток Кт']].sum()
Total2 = df.loc[df['Показатель лицевого счета'].str.contains('РЕЗ_ПРШ_ПЕР_НУ|РЕЗ_ПРШ_ПЕР_ВН|ПОСТУПЛЕНИЯ_АУ|ПОСТУПЛЕНИЯ_БУ|ПОСТУПЛЕНИЯ_ВН|ВЫБЫТИЯ_АУ|ВЫБЫТИЯ_БУ|ВЫБЫТИЯ_ВН', case=False) & (df['Идентификатор Массива']==1),['Остаток Дт', 'Остаток Кт']].sum()
print('На начало дня =',Total['Остаток Кт']-Total['Остаток Дт'])
print('На конец дня =',Total2['Остаток Кт']-Total2['Остаток Дт'])


# In[21]:


import pandas as pd
df = pd.read_excel('C:\\Users\\mzuev\\PycharmProjects\\pythonProject\\Project\\R01\\439T.xls')
df.loc[df['Показатель лицевого счета'].str.contains('РЕЗ_ПРШ_ПЕР_НУ|РЕЗ_ПРШ_ПЕР_ВН|ПОСТУПЛЕНИЯ_АУ|ПОСТУПЛЕНИЯ_БУ|ПОСТУПЛЕНИЯ_ВН|ВЫБЫТИЯ_АУ|ВЫБЫТИЯ_БУ|ВЫБЫТИЯ_ВН', case=False),['Номер документа юридического лица', 'Дата документа юридического лица','Оборот дебет','Оборот кредит']]


# In[ ]:





# In[ ]:




