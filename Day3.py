# list Comprehension
# for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)
#list comprehension version
print([i for i in range(11)])
#for loop version--> odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i for i in range(11) if i%2!=0])
print([i if i%2!=0 else i**2 for i in range(11)])

# ------------------------------------------------------------------------------------------
# for 1D matrix
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
# for loop version
for i in mat:
    for j in i:
        if j%2!=0:
            result.append(j**2)
        else:
            result.append(j**3)

print(result)
# list comprehension version
print([j**2 if j%2!=0 else j**3 for i in mat for j in i])
# ------------------------------------------------------------------------------------------
# for 2D matrix
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
# for loop version
for i in mat:
    row_data = []
    for j in i:
        if j%2!=0:
            row_data.append(j**2)
        else:
            row_data.append(j**3)
    result.append(row_data)

print(result)
# list comprehension version
print([[j**2 if j%2!=0 else j**3 for j in i] for i in mat])

# ------------------------------------------------------------------------------------------
my_list=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]

for i in list_b:
 result.append((i,my_list.index(i)))
print(result)

print([(i,my_list.index(i)) for i in list_b])
# ------------------------------------------------------------------------------------------

#Dictionary Comprehension

my_list=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result={}

for i in list_b:
 result[i]=my_list.index(i)
print(result)

print({i:my_list.index(i) for i in list_b})

# ------------------------------------------------------------------------------------------

#stopword deletion from the sentences in  a list

sentences = ["a new world recordd was set",
             "in the holy city of ayodhya",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','a','of','the','and','to','in','on','with','was']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print(result)

final=[]
for i in result:
    final.append(' '.join(i))
print(final)

print([[word for word in sentence.split() if word not in stopwords]for sentence in sentences])
print([' '.join(i) for i in result])
# ------------------------------------------------------------------------------------------

#adding the numbers in a string excluding the numbers between the given numbers and concatinating the numbers between the given numbers

str1=input()
s1 = str1.replace(',','')
a=[]
for i in s1:
    a.append(int(i))
print(sum(a[:a.index(5)]+a[a.index(8)+1:]))
b=""
for i in a[a.index(5):a.index(8)+1]:
    b+=str(i)
print(b)
# ------------------------------------------------------------------------------------------
array=list(map(int,input().split(",")))
num1=sum(array[:array.index(5)]+array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
num2=""
for i in l:
    num2+=str(i)
print(num1)
print(num2)
# ------------------------------------------------------------------------------------------

s = input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))

# ------------------------------------------------------------------------------------------



