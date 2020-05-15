# Copyright (c) Ac industries All rights reserved
#
# Created by: Andrew Coxall
# Created on: May 15, 2020
# Circumference of circle

import constants


def main():
    # comment

    radius = int(input("Enter radius of the circle (mm): "))
    circumference = constants.TAU*radius
    print("")
    print("Circumference is {} mm²".format(circumference))


if __name__ == "__main__":
    main()
