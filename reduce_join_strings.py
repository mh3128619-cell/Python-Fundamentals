from functools import reduce

words=["p","y","t","h","o","n"]

result=reduce((lambda word1,word2:word1+word2),words)
print(result)
