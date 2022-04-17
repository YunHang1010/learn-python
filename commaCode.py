def commaCode(spam):
    string = ' '

    # range(0, ) start from 0
    # end with len(spam)-1
    for i in range(0,len(spam)-1):
        string = string + spam[i] + ' , '
    string = string + 'and '
    string = string + spam[len(spam) - 1]
    return string
    
spam = ['apples', 'bananas', 'tofu', 'cats']

print(commaCode(spam))