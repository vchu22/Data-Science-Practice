import pandas as pd
data = {'name':pd.Series(['John','Alice','Susan','Tim','James','Dave']),
        'age':pd.Series([19,20,41,18,55,21]),
        'hoursStudied':pd.Series([10,8,10,2,7,6]),
        'grade':pd.Series([88,90,70,58,74,95])
       }
gradebook = pd.DataFrame(data, columns=['name','age','hoursStudied','grade'])
print "Grades for the first exam\n", gradebook
print
passed = gradebook[gradebook.grade>=60][['name','grade']]
print "People who passed the test\n",passed
print
yfailed = gradebook[(gradebook.grade<60) & (gradebook.age<30)][['name','grade']]
print "Young people who failed the test\n",yfailed