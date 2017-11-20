result = "100*100="
ary = []
ary2 = []

i = 100
while i >= 2:
    tmp_ary = []
    result += "("
    result += str(i)
    ary.append(i)
    tmp_ary.append(i)
    result += "+"
    result += str(i - 1)
    ary.append(i - 1)
    tmp_ary.append(i - 1)
    result += "+"
    result += str(i - 1)
    ary.append(i - 1)
    tmp_ary.append(i - 1)
    result += "+"
    result += str(i - 2)
    ary.append(i - 2)
    tmp_ary.append(i - 2)
    result += ")"
    if i != 2:
        result += "+"
    i = i - 2
    ary2.append(tmp_ary)

print(result)
print(ary2)

sum = 0
for i in range(len(ary)):
    sum += ary[i]

print("sum is: {}, and ary's length is: {}".format(sum, len(ary)))

for i in range(len(ary2)):
    sum = 0
    for j in range(len(ary2[i])):
        sum += ary2[i][j]
    print(sum)