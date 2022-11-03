if __name__ == '__main__':

    s = input()
    for i in range(0, len(s), 3):
        print(s[i:i + 3], end=" ")
