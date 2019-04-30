def res(str):
    pass



str1 = "Let's take LeetCode contest"
arr = []
arr2 = str1.split(' ')
a = len(arr2)

for i in range(a):
   aa = list(arr2[i])
   aa.reverse()
   arr.append("".join(aa))


print(" ".join(arr))


