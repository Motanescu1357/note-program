"""
MIT License

Copyright (c) [2023] [M.S.Rares]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def main():
    """
    The main program.
    :return:
    """
    deleted = False
    import os.path
    while True:
        filename = input("enter note name or type del to delete a note>>").replace(' ', '_')
        if filename == "del":  # checks if the user wants to delete a note and if so sets the deleted variable to true
            deleted = True
        if os.path.exists(path=rf"C:\Program Files (x86)\Notes data\{filename}.txt") and deleted is False:  # edits a note
            read_note = open(rf"C:\Program Files (x86)\Notes data\{filename}.txt")
            print(read_note.read().replace('_', ' '))
            read_note.close()
            content = input("enter note content or press enter to not change anything>>").replace(' ', '_')
            if content != "":
                note = open(rf"C:\Program Files (x86)\Notes data\{filename}.txt", mode="w")
                note.write(f"{content}")
                note.close()
        elif deleted is False:  # crates a note
            with open(rf"C:\Program Files (x86)\Notes data\{filename}.txt", mode="x") as note:
                content = input("enter note content>>")
                note.write(f"{content}")
                note.close()
        elif deleted is True:  # deletes a note if the deleted variable is true
            true_filename = input("type the note that you want to delete or pres enter to not delete a note>>").replace(' ', '_')
            if not true_filename == "":
                if os.path.isfile(rf"C:\Program Files (x86)\Notes data\{true_filename}.txt"):
                    os.remove(rf"C:\Program Files (x86)\Notes data\{true_filename}.txt")
                else:
                    import sys
                    print(rf"[ERROR]path: 'C:\Program Files (x86)\Notes data\{true_filename.replace(' ', '_')}.txt' is incorrect", file=sys.stderr)
            deleted = False


if __name__ == "__main__":
    main()
