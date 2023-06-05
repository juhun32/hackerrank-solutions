thickness = int(input())
char = "H"

for i in range(thickness):
    print(
        (char * i).rjust(thickness - 1, " ")
        + char
        + (char * i).ljust(thickness - 1, " ")
    )

for _ in range(thickness + 1):
    print(
        (char * thickness).center(thickness * 2)
        + (char * thickness).center(thickness * 6)
    )

for _ in range((thickness + 1) // 2):
    print((char * thickness * 5).center(thickness * 6))

for _ in range(thickness + 1):
    print(
        (char * thickness).center(thickness * 2)
        + (char * thickness).center(thickness * 6)
    )

for i in range(thickness):
    print(
        (
            (char * (thickness - i - 1)).rjust(thickness)
            + char
            + (char * (thickness - i - 1)).ljust(thickness)
        ).rjust(thickness * 6)
    )
