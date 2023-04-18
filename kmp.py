
def lps(pt):
    lps_arr =[0]
    ct1 = 0  # index for the matching sub string
    for i in range(1,len(pt)):
        if pt[ct1] == pt[i]:
            lps_arr.append(lps_arr[i-1] +1)
            ct1 += 1

        else:
            lps_arr.append(0)
            ct1 = 0

    # print(f"The lps array is: {lps_arr}")
    return lps_arr


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    j = 0  # index for pat[]
    count = 1  # counter for the no of times pattern has been found

    lps_arr = lps(pat)

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print(f"Pattern found for {count} time at index {i-j} till index {(i-j)+(len(pat)-1)}")
            j = lps_arr[j - 1]
            count+=1

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps_arr[j - 1]
            else:
                i += 1

string1 =  "ABXABABXAABXABCABXBCCBBAAABXXBA"
pt_str = "ABXABCABX"


KMPSearch(pt_str,string1)

