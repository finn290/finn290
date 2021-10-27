#14/7/21
#this "compresses" a string with run length encoding
#however if you enter a normal sentance it makes it longer
#rle should only be used in specific cases.
rle = input('enter uncoded string')
y = rle[0]
len1 = len(rle)
#print (rle[1:])
output = ''
charint = 1
for i in range(len(rle)):
    
    try:
        c1 = rle[i]
    except:
        break
    try:
        c2 = rle[i+1]
    except:
        c2 = ''
    #print(c1,c2)
    if c1 == c2:
        #rle = rle[1:]
        charint += 1
    else:

        
        while charint > 9:
            output = output + ('9'+c1)
            charint -= 9
    
        output = output + (str(charint)+c1)
        charint = 1
print(output)
if len1 > len(output):
    print('the amount of letters you have saved is ',len1- len(output))
elif len(output) > len1:
    print('you have gained number of letters', len(output) - len1,)
else:
    print('they are the same')            
string = output
l = len(string)
while l < 1 or((l % 2) == 1):
    #if not (l % 2) == 1:
    print('odd number of characters')
    string = input('enter an rle string')
    l = len(string)
output = ''
for i in range(0,len(string),2):
    try:
        p = int(string[i])
    except:
        print('character invalid')
        sys.exit()
    for j in range(p):
        output = output + (string[i+1])
print(output)
