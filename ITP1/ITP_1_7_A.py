"""
Grading
Write a program which reads a list of student test scores and evaluates the performance for each student.

The test scores for a student include scores of the midterm examination m (out of 50),
the final examination f (out of 50) and the makeup examination r (out of 100).
If the student does not take the examination, the score is indicated by -1.

The final performance of a student is evaluated by the following procedure:

If the student does not take the midterm or final examination, the student's grade shall be F.
If the total score of the midterm and final examination is greater than or equal to 80, the student's grade shall be A.
If the total score of the midterm and final examination is greater than or equal to 65 and less than 80, the student's grade shall be B.
If the total score of the midterm and final examination is greater than or equal to 50 and less than 65, the student's grade shall be C.
If the total score of the midterm and final examination is greater than or equal to 30 and less than 50, the student's grade shall be D.
However, if the score of the makeup examination is greater than or equal to 50, the grade shall be C.
If the total score of the midterm and final examination is less than 30, the student's grade shall be F.
Input
The input consists of multiple datasets. For each dataset, three integers m, f and r are given in a line.

The input ends with three -1 for m, f and r respectively. Your program should not process for the terminal symbols.

The number of datasets (the number of students) does not exceed 50.

Output
For each dataset, print the grade (A, B, C, D or F) in a line.
"""
while True:
    M, F, R = map(int, input().split())
    if M == -1 and F == -1 and R == -1:
        break
    if M == -1 or F == -1:
        print('F')
    elif M + F >= 80:
        print('A')
    elif M + F >= 65:
        print('B')
    elif M + F >= 50:
        print('C')
    elif M + F >= 30:
        if R >= 50:
            print('C')
        else:
            print('D')
    else:
        print('F')
