INPUT_NUM = input("Select Number in a range 0 - 255 : ")
INPUT_NUM = eval(INPUT_NUM) #transfer type
print("Number is %d" %(INPUT_NUM))

#二進位
bistring = ""
binvalue = INPUT_NUM
while binvalue != 0:
    j = binvalue % 2
    bistring = str(j) + bistring
    binvalue = binvalue // 2
print ("Transfer to Binary : %s" %(bistring))



#十六進位
hexstring = ""
hexvalue = INPUT_NUM
while hexvalue != 0:
    k = hexvalue % 16
    hexstring = str(k) + hexstring
    hexvalue = hexvalue // 16
#商    
hex_num = int(INPUT_NUM)
if hex_num // 16 == 15:
    hex_letter = "F"
elif hex_num // 16 == 14:
    hex_letter = "E"
elif hex_num // 16 == 13:
    hex_letter = "D"
elif hex_num // 16 == 12:
    hex_letter = "C"
elif hex_num // 16 == 11:
    hex_letter = "B"
elif hex_num // 16 == 10:
    hex_letter = "A"
else:
    hex_letter = hex_num // 16

#餘
if hex_num % 16 == 15:
    hex_end_letter = "F"
elif hex_num % 16 == 14:
    hex_end_letter = "E"
elif hex_num % 16 == 13:
    hex_end_letter = "D"
elif hex_num % 16 == 12:
    hex_end_letter = "C"
elif hex_num % 16 == 11:
    hex_end_letter = "B"
elif hex_num % 16 == 10:
    hex_end_letter = "A"
else:
    hex_end_letter = hex_num % 16
    
print ("Transfer to hexadecimal :" , str(hexstring),",", hex_letter,hex_end_letter)