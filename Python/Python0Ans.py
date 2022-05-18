# Question --> https://stackoverflow.com/questions/72270520/how-to-append-data-inside-the-first-list-into-the-second-list

y=[2]
x=[22, 34, 55]

y.extend(x)
print(y) # prints [2, [22, 34, 55]]

y=[2]
y.extend([i for i in x])
print(y) # prints [2, 22, 34, 55]