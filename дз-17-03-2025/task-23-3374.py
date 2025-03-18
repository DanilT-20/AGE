def f(num, end, ans=[]):
    if num == end:
         return 1
    if num< -50 or num > 50 or num in ans:
        return 0
    return f(num+2,end,ans+[num])+f(num-3,end,ans+[num])
print(f(1,30))