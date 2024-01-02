lis = "\n Geeks for Geeks \n"
string = lis.strip()
print(string)

for i in range(10):
    print(i)

s = "(0010,0010),"
s = s[:-1]
print(s)

text = ["pranav","rao"]
str_text = ''.join(text)
print(str_text)

if 2 <= 3:
    print(6)

s = "300"
print(type(s))

string = "CodeBasics"
print(string.replace("C","&"))
print(string[-4:])
s = "IBM|US|100|5.4"
s = s.split("|")
print(s)

price = 100
eps = 25
print(f"{price/eps}")

news_article = "Hey I am pranav and Tesla is TESLA and tesla"
if "tesla" in news_article.lower():
    print("True")

patient_tags_file = "current_tags.txt"
with open(patient_tags_file,"w") as savedFile:
    savedFile.write("Hey pranav \n\nHow are you")
with open(patient_tags_file, "r") as f:
    finalsavedfile = f.read().replace("\n\n","\n")
with open(patient_tags_file, "w") as currentFile:
    currentFile.write(finalsavedfile)

key="False"
print(type(key))
print(type(eval(key)))
b = True
print(not eval(key))

c1 = False
c2 = False
c3 = False
c4 = False
if c1 or c2 or c3 or c4:
    print("occurrence is there")
else:
    print("No occurrence is there")

patient_info = "<empty series description>, 2017-12-11 <invalid time>.<empty series description>, 2017-12-11 12:17\nCT, ORIGINAL\PRIMARY\AXIAL\n85 Slices, Thickness: 1.25mm, KVP: 120"
print(patient_info.replace("_","\_").replace(".","\.").replace(r'\n','\n'))

startpoint = ['10,20']
startpoint = ' '.join([str(i) for i in startpoint])
print(startpoint)
print(type(startpoint))
res = [eval(i) for i in startpoint.split(',')][0]
print(f"{res, type(res), res}")


n = 5
l = '300,132,451,234,332,324,215,265,235,182'
ans = [eval(i) for i in l.split(',')]
print(f"{ans} {type(ans)}")
MyList = [[] for i in range(n)]
count = 0
for i in range(0,n):
    MyList[i].append(ans[count])
    count+=1
    MyList[i].append(ans[count])
    count+=1
print(f"{len(MyList)-1}")
count = 0
for i,j in MyList:
    if count == len(MyList)-1:
        print(f"ya {i} {j}", end='\n')
        break
    print(f"{i} {j}",end='\n')
    count+=1



