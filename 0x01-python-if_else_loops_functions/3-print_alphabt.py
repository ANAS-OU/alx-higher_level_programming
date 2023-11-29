#!/usr/bin/python3
for c in range(97, 123):
    if c not in [ord('q'), ord('e')]:
        print("{:c}".format(c), end="")
