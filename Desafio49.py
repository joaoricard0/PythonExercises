num = int(input("TABUADA\nIntroduza um Número:"))
print(f"Tabuada do {num}\n{'='*11}")
for i in range(1,11):
    print(f"{num} x {i:2} = {num*i}")
print(f"{'='*11}")