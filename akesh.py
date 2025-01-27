dict1 ={"a":12,"b":2}
result = {value:key for key,value in dict1.items()}
print(result)
#
words = ["hf","iuwe","hdsf"]
res = [i for i in words if i==i [::-1]]
print("palindrome strings are ",res)

#another method
def ispalindrome(str):
 
 #main function
 s = input("")
 ans = ispalindrome(s)
 if (ans):
    print("yes")
 else:
        print("no")