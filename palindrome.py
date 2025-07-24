def is_palindrome(s):
    left,right = 0,len(s)-1
    while left<right:
        if not s[left].isalnum():
            left=left+1
            continue
        if not s[right].isalnum():
            right = right-1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left =left + 1
        right = right-1
    return True

s = "A man, a plan, a canal: Panama"
if is_palindrome(s) :
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")
