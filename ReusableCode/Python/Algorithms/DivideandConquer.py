strs = ['flow','fl','free']


def conquer(str1,str2): # Conquer portion aka merging
    ans = ''
    for i in range(min(len(str1),len(str2))):
        if str1[i] != str2[i]:
            break
        ans += str1[i]
    return ans

def DivideandConquer(list): # The main function called for divide and conquer, it does the divide part and calls the conquer function before returning the ans
    if len(list) < 2: # when the list only has 1 string it returns it, essential the stop condition for the division portion
        return list[0]
    
    n = len(list) // 2 # keeps splitting the list into 2 until 1 string remains, in which the above if statements handles it

    return conquer(DivideandConquer(list[n:]),DivideandConquer(list[:n])) # the division portion using recursion

print(DivideandConquer(strs))