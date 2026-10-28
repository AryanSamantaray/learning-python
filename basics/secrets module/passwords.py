import secrets
print(secrets.choice("123jhbbfdha")) #Picks one random item from a sequence
print(secrets.randbelow(2)) #Random int from 0 to n-1

# wanna make a pass from the group of charecters given
chars = "abcXYZ123@#"
print(secrets.choice(chars)) ## one random char
#we will make a loop where it repeats itself and adds to the pass word
pwd=""
for i in range(12):
    pwd+=secrets.choice(chars)

print(pwd)