def generator_with_resources():
    print("open generator resource")
    try:
        yield from range(5)
    finally:
        print("close generator resource")

for i in generator_with_resources():
    print(i, 1/(i -2))
