from sys import stdin
from subprocess import run


def build(files):
    one_file = int(input("One file?: 0 (False) / 1 (True): ")) == 1
    show_console = int(input("Show console?: 0 (False) / 1 (True): ")) == 1
    name = input("Enter the file name (without .exe): ")

    command = [
        'pyinstaller',
        '-F' if one_file else '',
        '-w' if not show_console else '',
        f'-n {name}' if len(name) > 0 else ''
    ]

    command = [arg for arg in command if arg]

    command.extend(files)

    run(command)


if __name__ == "__main__":
    print(
        "Enter all the files you want to add, then press", '\n',
        "CTRL + Z + ENTER (Windows) or CTRL + D (UNIX) to finish entering them",
    )

    build([i.strip() for i in stdin])
