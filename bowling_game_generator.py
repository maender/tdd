import random
import sys

def game_generator(frames : int):
    out = list()

    for i in range(frames):
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
    args = sys.argv

    frames = 10
    if len(args) > 1:
        try:
            frames = int(args[1])
            if frames not in range(1, 10):
                print("Bad number of frames, generating with 10 frames")
                frames = 10
        except:
            print("Number of frames must be an integer in [0...10], generating with 10 frames")
            frames = 10
    print(game_generator(frames))
