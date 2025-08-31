from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

get_files_info_cases = [
    ("calculator", ".", "current directory"),
    ("calculator", "pkg", "'pkg'"),
    ("calculator", "/bin", "'/bin'"),
    ("calculator", "../", "'../'"),
]

get_file_content_cases = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
]

write_file_cases = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
]


def main():
    # for case in get_files_info_cases:
    #     print(f"Result of {case[2]}:")
    #     print(get_files_info(case[0], case[1]))

    # for case in get_file_content_cases:
    #     print(f"Result of {case[1]}")
    #     print(get_file_content(case[0], case[1]))

    for case in write_file_cases:
        print(f"Result of {case[1]}")
        print(write_file(*case))


main()
