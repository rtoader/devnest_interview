import subprocess

# Test with no file attached
from pathlib import Path

data = subprocess.check_output("python binary_reverse.py")
print(data)
assert "Please give input files" in str(data)

data = subprocess.check_output("python binary_reverse.py -h")
assert "python binary_reverse.py file1 [file2, ...]" in str(data)

data = subprocess.check_output("python binary_reverse.py inexistent_file.in")
assert "inexistent_file.in doesn't exist" in str(data)
assert not Path("inexistent_file.in.out").is_file()

data = subprocess.check_output("python binary_reverse.py file.in")
assert "file.in processed" in str(data)
assert Path("file.in.out").is_file()

data = subprocess.check_output("python binary_reverse.py file.in another_file.in")
assert "file.in processed" in str(data)
assert "another_file.in processed" in str(data)
assert Path("file.in.out").is_file()
assert Path("another_file.in.out").is_file()


data = subprocess.check_output("python binary_reverse.py file.in inexistent_file.in")
assert "file.in processed" in str(data)
assert "inexistent_file.in doesn't exist" in str(data)
assert Path("file.in.out").is_file()
assert not Path("inexistent_file.in.out").is_file()