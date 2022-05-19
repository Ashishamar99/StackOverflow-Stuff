# Question: https://stackoverflow.com/questions/72307565/could-not-convert-string-to-float-due-the-minus-symbol/72307957
revenueChange = ['3.00%', '-5.25%']
for i in revenueChange: 
	res = float(i.strip('%'))/100
	print(res)