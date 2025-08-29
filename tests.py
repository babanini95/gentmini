from functions.get_files_info import get_files_info

cases = [
    ("calculator", ".", "current directory"),
    ("calculator", "pkg", "'pkg'"),
    ("calculator", "/bin", "'/bin'"),
    ("calculator", "../", "'../'"),
]


def main():
    for case in cases:
        print(f"Result of {case[2]}:")
        print(get_files_info(case[0], case[1]))


main()
