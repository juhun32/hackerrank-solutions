N, M = map(int, input().split())

for i in range(N // 2):
    print(
        "-" * ((M - (3 * (2 * i + 1))) // 2)
        + ".|." * (2 * i + 1)
        + "-" * ((M - (3 * (2 * i + 1))) // 2)
    )

print("-" * ((M - 7) // 2) + "WELCOME" + "-" * ((M - 7) // 2))

for i in reversed(range(N // 2)):
    print(
        "-" * ((M - (3 * (2 * i + 1))) // 2)
        + ".|." * (2 * i + 1)
        + "-" * ((M - (3 * (2 * i + 1))) // 2)
    )