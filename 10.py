a = [1]

# calculate 30 values
for i in range(1, 31):
    # a[i] base
    base = str(a[i - 1])
    base_len = len(base)
    result = "0"
    j = 0
    count = 1
    while j + 1 < base_len:
        if base[j + 1] == base[j]:
            count += 1
            j += 1
        else:
            result += str(count)
            result += str(base[j])
            j += 1
            count = 1
    if j + 1 == base_len:
        result += str(count)
        result += str(base[j])
    a.append(int(result))

print(a)
print(len(str(a[30])))
