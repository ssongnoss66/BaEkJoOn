inpt = input()

hpp = inpt.count(":-)")
sd = inpt.count(":-(")

if hpp == sd == 0:
    print("none")
elif hpp == sd:
    print("unsure")
elif hpp > sd:
    print("happy")
else:
    print("sad")