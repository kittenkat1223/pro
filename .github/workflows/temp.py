import pandas as pd
import numpy as np

df = pd.read_excel('test1.xlsx',
                   header = None,
                   names = ['ref_1','A_1','C_1','G_1','T_1','call_1','ref_2','A_2','C_2','G_2','T_2']
                   )

#print(df)

c1c1 = df.iloc[:,0:6]
c1c2 = df.iloc[:,6:11]

#print(c1c1)
#print(c1c2)
def maxValueIndex():
    try:
        maxValueIndex = df.idxmax(axis = 1)
    except:
        print("header dummy")

print("Max values of row are at following columns :")
print(maxValueIndex(c1c2))


excel_file_path2 = 'test2.xlsx'

df2 = pd.read_excel('test2.xlsx',
                   header = None,
                   names = ['ref_1','A_1','C_1','G_1','T_1','call_1','ref_2','A_2','C_2','G_2','T_2']
                   )

#print(df2)

c2c1 = df2.iloc[:,0:6]
c2c2 = df2.iloc[:,6:11]

#print(c2c1)
#print(c2c2)