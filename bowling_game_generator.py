import random

def game_generator():
    out = list()

    for i in range(10):
        a = random.randint(0, 10)
        if i < 9:
            b = random.randint(0, 10 - a) if a < 10 else 0
            out.append((a, b))
        else:
            b = random.randint(0, 10 - a) if a < 10 else random.randint(0, 10)
            if a == 10 or a + b == 10:
                c = random.randint(0, 10)
                out.append((a, b, c))
            else:
                out.append((a, b))

    return out


if __name__ == '__main__':
    print(game_generator())