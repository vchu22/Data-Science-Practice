import pandas as pd
data = {'name':pd.Series(['John','Alice','Susan','Tim','James','Dave']),
        'age':pd.Series([19,20,41,18,55,21]),
        'hoursStudied':pd.Series([10,8,10,2,7,6]),
        'grade':pd.Series([88,90,70,58,74,95])
       }
dataframe = pd.DataFrame(data, columns=['name','age','hoursStudied','grade'])
print dataframe