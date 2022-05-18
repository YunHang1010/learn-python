# Account words 
# in txt

file = open('filePath.txt','r')
txt = file.read()
txt = txt.lower()


for cha in '‘’“”#$%&()*+-,.;:<=>?@[\\]^_"{|}':
    txt = txt.replace(cha,' ')

words = txt.split()
# len(words)
set(words)
# len(set(words))

counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
# items

# for i in range(20):
#    print(items[i][0],items[i][1])
    
# for i in range(20):
#     word,count = items[i]
#     print('{0:<10}{1:>5}'.format(word,count))