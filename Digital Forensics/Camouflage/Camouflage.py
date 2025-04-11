import random

class Cipher:
    def __init__(self, key):
        self.key = key

    def scramble(self, text):
        return ''.join([chr((ord(c) + self.key - 33) % 94 + 33) for c in text])

    def unscramble(self, text):
        return ''.join([chr((ord(c) - self.key - 33) % 94 + 33) for c in text])


def random_noise(length):
    chars = [chr(random.randint(33, 126)) for _ in range(length)]
    random.shuffle(chars)
    return ''.join(chars)

class Hidden:
    fragments = ["f0un", "MKJA", "KUT{", "Y0u_", "d_th", "1s_g", "r3at", "}", "LKSS"]

    @staticmethod
    def assemble_fragments():
        return ''.join(Hidden.fragments)

# Generate camouflage code noise
def camouflage():
    data = [random_noise(12) for _ in range(6)]
    noise = "".join(data)
    for i in range(len(noise)):
        pass 


camouflage()

if __name__ == "__main__":
    camouflage()
    secret = Hidden.assemble_fragments()
    camouflage()
    print("This script does something very simple. Nothing special here.")
    # print(f"Secret: {secret}")
