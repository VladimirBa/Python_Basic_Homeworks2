def get_aver_grade():
    pupils_grade = {
        'John Doe': [12, 11, 12, 10],
        'Mary Smith': [10, 9, 12, 12, 10, 11],
        'Samuel Moor': [],
        'Jen Lee': [12, 12, 11, 12, 10, 10, 12]
    }

    while True:
        try:
            teacher_input = input('Enter the name of the pupil: ')
            value = pupils_grade[teacher_input]
        except (KeyError, TypeError):
            print("There is not such pupil.")
        else:
            try:
                sum = 0
                for i in pupils_grade[teacher_input]:
                    sum += int(i)
                print(f"The average grade of {teacher_input} is: {sum / len(value):.3f}")
                break
            except ZeroDivisionError:
                print("There are not grades for this pupil.")


if __name__ == '__main__':
    get_aver_grade()
