#!/usr/bin/python3
if __name__ == "__main__":
    import sys

count = len(sys.argv) - 1
args = sys.argv

rst = 0
for i in range(1, count + 1):
    rst += int(args[i])

print(rst)
