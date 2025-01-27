import pandas as pd
screen_time = [1,2,3,4,5,4]
stu_name = ["aa","uyf","eh","td","634","63"]
id = [2,3,12,3,33,76]
dict1 = {"screen_time":screen_time,"stu_name": stu_name,"id":id }
print(dict1)
df = pd.DataFrame(dict1)
print(df)

#list comprehension
list  = [1,23,3,4,3]
res = [i+2 for i in list ]
print(res)
#list 
res1 = [x**4 for x in range(1,32)]
print(res)
