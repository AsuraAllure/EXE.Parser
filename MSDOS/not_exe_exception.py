class NotExeFileException(Exception):
    def __str__(self):
        print("File not executable")
