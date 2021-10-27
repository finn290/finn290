#can word 2 be made from word 1

first = (input('word 1'))
sec = (input('word 2'))
lis = []
lis2 = []
for let in first:
    lis.append(let)
found = True
for another in sec:
    lis2.append(another)
for let in lis:
    try:
        lis2.remove(let)

    except ValueError:
        found = False
if found:
    print('work')
if not found:
    print('no work :(')
    

