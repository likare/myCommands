def greet():
    options = [
        "\n<============WELCOME TO COMMANDS============>\n",
        "1. `lsd -l` # List content of the current directory",
        "2. `lsd -al` # List content of the current directory including hidden files",
        "3. `chmod +x <file.ext>` # Makes a file executable",
        "4. `rm <file.ext>` # Deletes file",
        "5. `nvim /vi <file editing (advanced txt editors)>`",
        "6. `cd <change directory>`",
        "7. `pwd <print working directory>`",
        "8. `mkdir <make a directory>`",
        "9. `mv <move or rename file and directories>`",
        "10. `rm <remove files or directoies>`",
        "11. `rmdir <remove empty directories>`",
        "12. `touch <change file timestamp or create empty file>`",
        "13. `find <find for a file in a directory hierarchy>`",
        "14. `locate <find files by name>`",
        "15. `tree <Display directories in a tree-like format>`",
        "16. `chown <change file owner and group.`",
        "17. `chgrp <change group ownership>`",
        "18. `stat <display file or file system status>`",
        "19. `cat <concatenate and display file content>`",
        "20. `tac <concatenate and display file content in reverse>`",
        "21. `more <view file content interactivly(page by page)`",
        "22. `less <view file content interactivly (scrollable)`",
        "23.`head <output the first part of a file>`",
        "24. `tail<output the last part of a file>`",
        "25. `nano <text editor (terminal-based>`",
        "26. `emacs <text editor>`",
        "27. `grep <serch text using patterns>`",
        "28. `sed <stream editor for filtering and transforming text>`",
        "29. `awk `<pattern scanning and processing language>`",
        "30. `cut <remove sections from each line of files>`",
        "31. `sort <sort line of text files>`",
        "\n<====================END====================>\n"
    ]

    for i in options:
        print(i)
    return 0


def main():
    greet()
    return 0


if __name__ == "__main__":
    main()
