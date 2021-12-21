file  = open('view.txt','r')
word = ""
value = ""
f = 0
i = 0
dt = file.read()
values = []
for d in dt:
    word += d
    if word == 'simpleText':
        f  = 0
        #print(word)
        for j in range(20):
            if dt[i+j] =="\"":
                f += 1
            elif f == 2:
                value += dt[i+j]
            elif f == 3:
                values.append(value)
                break
        value=""
    if d == ' ' or d ==':' or d =="," or d == "\"" or d == "{{" or d== "}}" or d == "[" or d=="]" or d=="=":
        word = ""
    i += 1
    # if i == 10000:
    #     break

v = []
i = 1
for val in values:
    if i%3 == 0:
        v.append(val)
    i += 1
v.pop()

file2 = open("values.txt","w")
for i in values:
    file2.write(i)
    file2.write("\n")
m = 0
s = 0
wor = ""
i  = 1
for val in v:
    wor = ""
    for w in val:
        if w == ":":
            m += int(wor)
            wor=""
        else:
            wor += w
    ms = int(wor)
    s += ms
    m += s//60
    s = s%60
    print( m ,s)