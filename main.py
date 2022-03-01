import random
bigChar="QWERTYUIOPASDFGHJKLZXCVBNM"
smallChar="qwertyuiopasdfghjklzxcvbnm"
numbers="0123456789"
symbols="./;[]-=<>?{}!@#$%&*()+"
all=bigChar+numbers+symbols+smallChar

length=int(input("Length your password: "))
password="".join(random.sample(all,length))
print("Your password: "+password)