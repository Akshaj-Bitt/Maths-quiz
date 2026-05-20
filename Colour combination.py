def mix_colors(c1, p1, c2, p2):
    # Normalize
    total = p1 + p2
    p1 = (p1 / total) * 100
    p2 = (p2 / total) * 100

    # Base color logic
    pair = {c1, c2}

    if pair == {"red", "blue"}:
        base = "Purple"
    elif pair == {"red", "yellow"}:
        base = "Orange"
    elif pair == {"blue", "yellow"}:
        base = "Green"
    elif pair == {"black", "white"}:
        base = "Gray"
    elif c1 == c2:
        base = c1.capitalize()
    else:
        return "Unknown Color", p1, p2

    # Shade naming
    diff = abs(p1 - p2)

    if diff < 10:
        final = "Balanced " + base
    elif p1 > p2:
        final = "Dark " + base
    else:
        final = "Light " + base

    return final, p1, p2


# ---- Main Program ----
c1 = input("Enter first color: ").lower()
p1 = int(input("Enter percentage: "))

c2 = input("Enter second color: ").lower()
p2 = int(input("Enter percentage: "))

result, p1, p2 = mix_colors(c1, p1, c2, p2)

print("\nFinal Color:", result)
print(f"Mix: {c1.capitalize()} {round(p1,1)}% + {c2.capitalize()} {round(p2,1)}%")

input("\nPress Enter to exit...")
