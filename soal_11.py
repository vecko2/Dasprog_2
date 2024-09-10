substances = float(input("input your data by celcius substances: ")) 

if 100 * 0.95 <= substances <= 100 * 1.05:
    print("substances is Water")

elif 357 * 0.95 <= substances <= 357 * 1.05:
    print("substance is Mercury")

elif 1187 * 0.95 <= substances <= 1187 * 1.05:
    print("substance is Copper")

elif 2193 * 0.95 <= substances <= 2193 * 1.05:
    print("substance is Silver")

elif 2660 * 0.95 <= substances <= 2660 * 1.05:
    print("substance is Gold")
    
else:
    print("substance unknown")