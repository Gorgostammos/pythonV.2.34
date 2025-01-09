def regn_volum(brede,lengde,høyde ):
    volum = brede * lengde * høyde
    return volum

brede1 = int(input("skriv breden: "))
lengne1 = int(input("skriv lengde: "))
høyde1 = int(input("skriv høyde: "))

volum1 = regn_volum(lengne1, høyde1, lengne1)
print(volum1)



