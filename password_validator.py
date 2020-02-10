from string import punctuation
def Validator(x):
    n = (i for i in range(0,11))
    if (("" not in x) and (len(x) >= 5 and len(x) <= 15)):
        for k in n:
            if (str(k) in x):
                for i in punctuation:
                    if i in x:
                        return True
            return False
password = input("Enter your Password: ")
print(f"{password} is a valid Password: {Validator(password)}")
