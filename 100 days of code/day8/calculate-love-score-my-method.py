# My method

name_1 = input("What's your name? ").lower()
name_2 = input("What's your name? ").lower()
print(f"The name 1 is: {name_1}.")
print(f"The name 2 is: {name_2}.")

# TRUE

letter_t = name_1.count("t") + name_2.count("t")
print(f"T occurs {letter_t} times")
letter_r = name_1.count("r") + name_2.count("r")
print(f"R occurs {letter_r} times")
letter_u = name_1.count("u") + name_2.count("u")
print(f"U occurs {letter_u} times")
letter_e = name_1.count("e") + name_2.count("e")
print(f"E occurs {letter_e} times")

total_true = letter_t + letter_r + letter_u + letter_e
print(total_true)

# LOVE

letter_l = name_1.count("l") + name_2.count("l")
print(f"L occurs {letter_l} times")
letter_o = name_1.count("o") + name_2.count("o")
print(f"O occurs {letter_o} times")
letter_v = name_1.count("v") + name_2.count("v")
print(f"V occurs {letter_v} times")
letter_e = name_1.count("e") + name_2.count("e")
print(f"E occurs {letter_e} times")

total_love = letter_l + letter_o + letter_v + letter_e
print(total_love)

result = str(total_true) + str(total_love)
print(result)
