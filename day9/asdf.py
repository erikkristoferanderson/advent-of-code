from day9.int_code_comp_9a import compute

with open("input5.txt", "r") as file:
    tape = [int(s) for s in file.read().split(",")]
pass

foo = compute(tape, 1)
print(foo)
