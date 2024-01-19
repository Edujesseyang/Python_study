# ---------- calculate Resistance of a circuit---------
Rt = 0
ipt = 1
while ipt != 0:
    print("Enter 0 to start calculate!")
    R = float(input("Enter the resistance R: "))
    ipt = R
    bool = input("Is is series or parallel, enter 's' / 'p': ")
    if bool == "s":
        Rt = Rt + R
    else:
        R = R + (1 / R)
        Rt = 1 / R
print(f'The total resistance of the circuit is {Rt}')
# ------------------------------------------------------
