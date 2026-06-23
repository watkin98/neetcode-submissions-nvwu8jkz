class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCount = 0

        while studentCount < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                studentCount = 0
            else:
                temp = students.pop(0)
                students.append(temp)
                studentCount += 1

            if students == [] and sandwiches == []:
                return 0

        return studentCount
        