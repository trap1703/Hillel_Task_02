


# First ========================================
print ("First")
print ("=" * 50)
st_name = input ("Input your name: ")
int_age = input ("Input your age: ")
print ("Hello {0}, your age is {1}" . format(st_name, int_age))

# Second ========================================
print ("=" * 50)
print ("Second")
print ("=" * 10)
int_number = input ("Input simple number: ")
int_number = int(int_number) ** 132
uuu = (int_number % 3) #- int_number//3
print ("number to the exponent 132 : {0} , the remainder of dividing by 3 : {1} " . format (int_number, uuu))

# Third ========================================
print ("=" * 50)
print ("Third")
print ("=" * 10)
int_n = input ("Input simple number N : ")
int_n = int(int_n)
int_na = list (range (1, int_n+1))
print ('This is numer :', int_na)
counter = 0
for item in int_na:
    if item % 2 == 0:
        counter = counter +1
print ("Even numbers : " , counter)

# Fourth ========================================
print ("=" * 50)
print ("Fourth")
print ("=" * 10)
int_nt = input ("Input simple number N : ")
arr = []
int_nt = int(int_nt)
import random
arr = [random.randint(0,20) for i in range(int_nt)]
print (arr)
arr.sort()
print ("Mimimal is : ", arr[0])
arr.reverse()
print ("Maximal is : ", arr[0])

# Fifth ========================================
print ("=" * 50)
print ("Fifth")
print ("=" * 10)

ls = []
import random, string
def randomword(lenght):
   leters = string.ascii_lowercase
   return ''.join(random.choice(leters) for i in range(lenght))
# print (randomword(10))
lg = 0
max = 0
min = 50
maxn = 0
minn = 0
for i in range(20):
   nk = int(random.randint(1, 40))
   ls.append(randomword(nk))
   # print ('string -', i, ls[i])
   # print (len(ls[i]))
   lenght_st = len(ls[i])
   if lenght_st >= max:
      maxn = i
      max = lenght_st
   if lenght_st <= min:
      minn = i
      min = lenght_st


# print (ls)
print ('Max symbol ', max, ':String number', maxn)
print ('Min symbol ', min, ':String number', minn)
# print ('T'*10)
# print ('Max string', ls[maxn])
# print ('Min string', ls[minn])
# print ('T'*10)

exch = ls[maxn]
exchmin = ls[minn]
# print ('print exch', exch)
# print ('print exchmin', exchmin)
ls[minn] = exch
ls[maxn] = exchmin
print ('After  Exchange')
print ('max string', ls[minn], ':String number', minn)
print ('min string', ls[maxn], ':String number', maxn)





