## denary to hexss
#6/10/21
#I made it to be as understandable as possible to the year 10 class I am
#helping out with
denary = int(input('enter denary'))
nums = '0123456789ABCDEF'
hex1 = 0
if denary > 16:
    while denary > 16:
        denary -= 16
        hex1 +=1
hex2 = 0
while denary > 0:
    denary -= 1
    hex2 += 1
output =(nums[hex1] + nums[hex2])
print(output)
