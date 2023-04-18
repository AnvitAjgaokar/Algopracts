st1 = "AABAACAADAABAABA"
st1.upper()

pat1 = "AAB"
pat1.upper()


def patternnum(pt):
    pt = pt[::-1]
    dic1 = {chr(i + 64): i for i in range(1, 27)}
    pt_value = 0
    for i in range(len(pt)):
        pt_value += dic1.get(pt[i]) * 10 ** i
    return pt_value


def robinkarp(s1, p1):
    pvalue = patternnum(p1)
    flag = 0
    for i in range(len(s1) - (len(p1)-1)):
        test = ""
        for j in range(i, i + len(p1)):
            test += s1[j]

        tvalue = patternnum(test)

        if pvalue == tvalue:
            print("Pattern found at index", i, "till index", i + (len(p1) - 1))
            flag = 1
            break

    if flag != 1:
        print("Pattern Not found")


robinkarp(st1, pat1)











