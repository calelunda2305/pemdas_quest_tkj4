list_integer = [1, 2, 3, 10, 100, 250]
list_string = ["Dewi", "Nazla", "Lulu"]
list_mix = [20, "Arya", True, "Bryan"]

print("Data sebelum diubah:", list_string)
list_string[0] = "Ilona"
list_string[1] = "Wulan"
print("Data string setelah diubah:", list_string)
print("Data sebelum diubah:", list_mix)
list_mix[0] = "10"
list_mix[1] = "Gina"
list_mix[2] = False
list_mix[3] = "Dino"
print("Data mix setelah diubah:", list_mix)
print("\n")

#perulangan for

x=["Dewi", "Nazla", "Lulu"]
for y in x:
    print(y)
    
print("\n")
for i in list_string:
    print(i)

print("\n")
for o in list_integer:
    print(o)

for c in list_mix:
      print(c)
