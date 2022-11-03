import os


def main():
    queue = [os.getcwd()]
    file1 = open("MyFile.txt", "a+")
    while not len(queue) == 0:
        dir_list = os.listdir(queue[0])
        for path in dir_list:
            if os.path.isdir(path):
                queue.append(path)
            else:
                file1.write(path)
                file1.write('\n')
        queue.pop(0)

    file1.close()


if __name__ == '__main__':
    main()
