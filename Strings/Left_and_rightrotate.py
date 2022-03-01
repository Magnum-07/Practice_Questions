
def rightrotate(s):
    return s[-1:] + s[:len(s) - 1]

def leftrotate(s):
    return s[2:] + s[:2]

input_ls = input().split(",")
for i in input_ls:
    word, num = i.split(":")
    num = int(num)
    val = 0
    while num > 0:
        val += (num % 10) ** 2
        num = num // 10
    res = ""
    if val % 2 == 0:
        res = rightrotate(word)
    else:
        res = leftrotate(word)
    print(res)