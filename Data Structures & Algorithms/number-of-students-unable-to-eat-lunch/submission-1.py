class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentTracker = len(students)

        while sandwiches != []:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                studentTracker = len(students)
            else:
                student = students.pop(0)
                students.append(student)
                studentTracker -= 1

            if studentTracker == 0:
                return len(students)

        return 0

        