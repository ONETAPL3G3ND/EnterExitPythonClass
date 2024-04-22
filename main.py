class File:
    def __init__(self, filename):
        print(f"Opening a file: {filename}")

    def __enter__(self):
        print("Entering")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing a file")

    def GetFileDate(self):
        return "simple date"



with File("Test.txt") as f:
    print(f.GetFileDate())
    input()
    b = 7 / 0

