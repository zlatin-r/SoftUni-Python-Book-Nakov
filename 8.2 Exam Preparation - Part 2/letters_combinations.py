start_letter = input().lower()
stop_letter = input().lower()
pass_letter = input().lower()
counter = 0

for i in range(ord(start_letter), ord(stop_letter) + 1):
    for j in range(ord(start_letter), ord(stop_letter) + 1):
        for h in range(ord(start_letter), ord(stop_letter) + 1):
            if h == ord(pass_letter) or j == ord(pass_letter) or i == ord(pass_letter):
                continue
            else:
                print("".join(chr(i) + chr(j) + chr(h)), end=" ")
                counter += 1
print(counter)
