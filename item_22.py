#!/usr/bin/env python3

'''Item 22 from Effective Python'''


# Example 1
''' You can define a class to store the names in a dictionary instead of using
a predefined attribute for each student '''
print('Example 1:\n==========')


class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


# Example 2
''' Using the class is simple '''
print('\nExample 2:\n==========')

book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 95)
book.report_grade('Isaac Newton', 85)
print(book.average_grade('Isaac Newton'))


# Example 3
''' Dictionaries are so easy to use that there’s a danger of overextending them
to write brittle code '''
print('\nExample 3:\n==========')

class BySubjectGradebook(object):

    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


# Example 4
''' Using the class remains simple '''
print('\nExample 4:\n==========')

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
print(book.average_grade('Albert Einstein'))


# Example 5
''' instead of mapping subjects (the keys) to grades (the values), I can use
the tuple (score, weight) as values '''
print('\nExample 5:\n==========')

class WeightedGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    ''' Although the changes to report_grade seem simple—just make the value a
    tuple—the average_grade method now has a loop within a loop and is
    difficult to read '''

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count


# Example 6
''' Using the class has also gotten more difficult. It's unclear what all of
the numbers in the positional arguments mean. '''
print('\nExample 6:\n==========')

book = WeightedGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 80, 0.10)
book.report_grade('Albert Einstein', 'Math', 80, 0.10)
book.report_grade('Albert Einstein', 'Math', 70, 0.80)
book.report_grade('Albert Einstein', 'Gym', 100, 0.40)
book.report_grade('Albert Einstein', 'Gym', 85, 0.60)
print(book.average_grade('Albert Einstein'))


# Example 7
''' Refactoring to classes '''
print('\nExample 7:\n==========')

grades = []
grades.append((95, 0.45))
grades.append((85, 0.55))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight
print(average_grade)


# Example 8
''' use _ to capture the third entry in the tuple and just ignore it '''
print('\nExample 8:\n==========')

grades = []
grades.append((95, 0.45, 'Great job'))
grades.append((85, 0.55, 'Better next time'))
total = sum(score * weight for score, weight, _ in grades)
total_weight = sum(weight for _, weight, _ in grades)
average_grade = total / total_weight
print(average_grade)


# Example 9
''' The namedtuple type in the collections module lets you easily define tiny,
immutable data classes '''
print('\nExample 9:\n==========')

import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))


# Example 10
''' write a class to represent a single subject that contains a set of grades
'''
print('\nExample 10:\n==========')

class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


# Example 11
''' write a class to represent a set of subjects that are being studied by a
single student '''
print('\nExample 11:\n==========')

class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


# Example 12
''' write a container for all of the students keyed dynamically by their names
'''
print('\nExample 12:\n==========')

class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


# Example 13
''' The line count of these classes is almost double the previous
implementation's size. But this code is much easier to read. The example
driving the classes is also more clear and extensible '''
print('\nExample 13:\n==========')

book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.10)
math.report_grade(80, 0.10)
math.report_grade(70, 0.80)
gym = albert.subject('Gym')
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade())
