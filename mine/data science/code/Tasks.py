import numpy as np
import pandas as pd

data = {'Name' : ["Alice", "Bob", "Cathy", "David", "Esther", "Fred", "Grace", "Henry"],\
'Gender' : ["F","M","F","M","F","M","F","M"],\
'Subject' : ["Math", "English", "Biology", "Math", "English", "Biology", "Math", "English"],\
"Score" : [85, 56, 92, 45, 74, 61, 59, 88], \
'Hours_Studied' : [5, 2, 6, 1, 3, 4, 2, 5], \
'Passed' : ["Yes", "No", "Yes", "No","Yes", "No","Yes", "No"]}
results = pd.DataFrame(data)
# print(results.to_string(index = False))
results = results.set_index('Name')

print(results)

# printing the first 5 rows
print(results.head(5))
print("Average Score: ", results['Score'].mean())
print("Student who studied more than 3 hours")
print(results[results['Hours_Studied']>3])
# Female students who passed

print(results[(results['Gender']=='F') & (results['Passed']== 'Yes') ])
print(results.loc['Alice'])# info about a particular person
print(results['Score'].describe())
print(results['Name'].describe())