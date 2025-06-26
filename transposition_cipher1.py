'''
This is Block (Single Column) Transposition Cipher
It breaks the message into blocks of equal length
No of columns = no of char in key
'''
import math
message='This is a message'
key='hack'

def encrypt_tranposition_cipher(message,key):
    translated=''
    msg_lst=list(message)       
    key_lst=sorted(list(key))       #sort key list from string
    col=len(key)
    row=int(math.ceil((len(message))/col))          #breaks into no of rows for n columns 

    fill_null=int((row*col)-len(message))    #fill null for spaces left in matrix
    msg_lst.extend('_'*fill_null)               #extend fill null spaces with _

    matrix=[msg_lst[i: i+col] for i in range (0,len(msg_lst), col)]         #make matrix of columns=n
    k_index=0                               #key index
    for _ in range(col):
        curr_ind=key.index(key_lst[k_index])                
        translated+=''.join([row[curr_ind] for row in matrix])       #join rows in matrix with reading column wise
        k_index+=1
    return translated

print(encrypt_tranposition_cipher(message,key))

def decrypt_transposition_cipher(translated):
    msg=''
    msg_lst=list(translated)
    col=len(key)
    row=int(math.ceil((float(len(translated)))/col))
    key_lst=sorted(list(key))
    dec_msg=[]
    for _ in range(row):
        dec_msg+=[[None]*col]
    k_index=0
    msg_index=0
    for _ in range(col):
        curr_ind=key.index(key_lst[k_index])
        for j in range(row):
            dec_msg[j][curr_ind]=msg_lst[msg_index]
            msg_index+=1
        k_index+=1

    try:
        msg=''.join(sum(dec_msg,[]))
    except TypeError:
        raise TypeError("Error in decryption")
    
    null_count=msg.count('_')
    if null_count>0:
        return msg[:-null_count]
    
    return msg

print(decrypt_transposition_cipher(encrypt_tranposition_cipher(message,key)))