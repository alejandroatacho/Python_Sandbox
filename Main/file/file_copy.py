# copyfile()= copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy() + copies metadata (file's creation and modifaction times)
import shutil

shutil.copyfile("main\\file\\placeholder\\test.txt",
                "main\\file\\placeholder\\copy_test.txt")
