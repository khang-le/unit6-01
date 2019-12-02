#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Dec 2019
# This program uses an array

import random


def main():
    # this function uses an array

    student_marks = []

    # input
    for loop_counter in range(0, 10):
        numbers = random.randint(1, 101)
        student_marks.append(numbers)
    print("")
    print("The random numbers are: ")

    for loop_counter in range(0, 10):
        print("{0} ".format(student_marks[loop_counter]), end="")
    average = (student_marks[0] + student_marks[1] + student_marks[2] +
               student_marks[3] + student_marks[4]
               + student_marks[5] + student_marks[6] + student_marks[7] +
               student_marks[8] + student_marks[9])/10
    print("")
    print("The average of the numbers is: {}".format(average))


if __name__ == "__main__":
    main()
