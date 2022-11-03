dictTask = dict()
dictUser = dict()


def exists_user(user):
    if user not in dictUser.keys():
        return False

    return True


def exists_task(task):
    if task not in dictTask.keys():
        return False

    return True


def create(act):
    if act[1] == "USER":
        dictUser[act[2]] = list()

    if act[1] == "TASK":
        dictTask[act[2]] = list()


def assign(act):
    if exists_task(act[2]) and exists_user(act[1]):
        dictTask[act[2]].append(act[1])
        dictUser[act[1]].append(act[2])


def get_list(act):
    if act[1] == "USER":
        if act[2] in dictTask.keys():
            print(dictTask[act[2]])
        else:
            print("task doesnt exist")

    if act[1] == "TASK":
        if act[2] in dictUser.keys():
            print(dictUser[act[2]])
        else:
            print("user doesnt exist")


def solve(act):
    if act[0] == "CREATE":
        create(act)

    if act[0] == "ASSIGN":
        assign(act)

    if act[0] == "LIST":
        get_list(act)

def print_valid_input():
    print('CREATE USER <user name>')
    print('CREATE TASK <task name>')
    print('ASSIGN <user name> <task name>')
    print('LIST USER <task name>')
    print('LIST TASK <user name>')

def main():
    while True:
        act = input()
        act = act.split(" ")
        if act[0][0] == '-':
            if act[0][1] == '-':
                print_valid_input()
            else:
                n = int(act[0][1:])
                for i in range(n):
                    act = input()
                    solve(act)
        else:
            solve(act)

if __name__ == '__main__':
    main()
