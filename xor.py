#12/7/21
#this program uses xor encryption to encrypt a string and send it to a target
#machine
#in order to protect my ip address I have changed it to input before
#this goes public
from socket import socket,AF_INET, SOCK_DGRAM
key = input('enter the key you want to encrypt the data with (needs to be longer than the message)')
ip = input('enter the ip address of the target')
port = 5001
mysoc = socket(AF_INET, SOCK_DGRAM)
mes = input('enter the message you want to send')
def encrypt(message,key):
    output = ''
    for x in range(len(message)):
        a = ord(message[x])
        b = ord(key[x])
        c = (a ^ b)
        output += str(chr(c))
    return(output)
def decode(enc,key):
    return(encrypt(enc,key))    
x = (encrypt(mes,key))
print(x)
mysoc.sendto(x.encode('utf-8'),(ip,port))


