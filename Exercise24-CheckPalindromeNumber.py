def IsPalindrome(inp):
    inp_str = str(inp)
    str_rev = inp_str[::-1]
    if inp_str == str_rev:
        return True
    else:
        return False

def IsPalindromeIterative(inp):
    rev = 0
    temp = inp
    while(temp > 0):
        lastDigit = temp % 10
        rev = rev*10 + lastDigit
        temp = temp // 10
    
    if inp == rev:
        return True
    else:
        return False

if __name__=='__main__':
    num = int(input("Enter a Number :"))
    print(IsPalindrome(num))
    print(IsPalindromeIterative(num))
    