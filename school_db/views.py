from django.shortcuts import render
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from .models import Student, Instructor, Course, StudentCourse
from .const_data import view_information


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Find all students and print their first_name, last_name, and GPA to the terminal
# Example solution:
def example_solution(request):

    students = Student.objects.all()

    for student in students:
        print(f'First Name: {student.first_name} Last Name: {student.last_name} GPA: {student.gpa}')


    return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#all
"""

# Expected Terminal Response:
"""
First Name: Jake Last Name: Sisko GPA: 4.0
First Name: Keira Last Name: Nerys GPA: 3.5
First Name: Julian Last Name: Bashir GPA: 4.4
First Name: Molly Last Name: OBrien GPA: 3.0
First Name: Keiko Last Name: Ishikawa GPA: 4.2
First Name: Eli Last Name: Garak GPA: 3.0
First Name: Thomas Last Name: Riker GPA: 2.5
First Name: Michael Last Name: Eddington GPA: 3.7
First Name: Beckett Last Name: Mariner GPA: 3.8
First Name: Sam Last Name: Rutherford GPA: 2.0
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
SELECT `school_db_student`.`id`,
       `school_db_student`.`first_name`,
       `school_db_student`.`last_name`,
       `school_db_student`.`year`,
       `school_db_student`.`gpa`
  FROM `school_db_student`
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Find all students who have a GPA greater than 3.0. 
# Order the data by highest GPAs first (descending).
# Print out each student's full name and gpa to the terminal
def problem_one(request):

  students_high_gpa = Student.objects.filter(gpa__gt = 3.0).order_by('-gpa')

  for student in students_high_gpa:
    print(f'Full Name: {student.first_name} {student.last_name} GPA: {student.gpa}')

  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#order-by
"""

# Expected Terminal Response:
"""
Full Name: Julian Bashir GPA: 4.4
Full Name: Keiko Ishikawa GPA: 4.2
Full Name: Jake Sisko GPA: 4.0
Full Name: Beckett Mariner GPA: 3.8
Full Name: Michael Eddington GPA: 3.7
Full Name: Keira Nerys GPA: 3.5
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
SELECT `school_db_student`.`id`,
       `school_db_student`.`first_name`,
       `school_db_student`.`last_name`,
       `school_db_student`.`year`,
       `school_db_student`.`gpa`
  FROM `school_db_student`
 WHERE `school_db_student`.`gpa` > 3.0
 ORDER BY `school_db_student`.`gpa` DESC
"""

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Find all instructors hired prior to 2010
# Order by hire date ascending
# Print out the instructor's full name and hire date to the terminal
def problem_two(request):

  instructors_b4_2010 = Instructor.objects.filter(hire_date__lt = '2010-01-01').order_by('hire_date')

  for instructor in instructors_b4_2010:
    print(f'Full Name: {instructor.first_name} {instructor.last_name}')
    print(f'Hire Date {instructor.hire_date}')

  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#year
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#lt
"""

# Expected Terminal Response: (format print challenge!)
"""
Full Name: Colin Robinson
Hire Date: 2009-04-10

Full Name: Guillermo de la Cruz
Hire Date: 2009-11-18
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
SELECT `school_db_instructor`.`id`,
       `school_db_instructor`.`first_name`,
       `school_db_instructor`.`last_name`,
       `school_db_instructor`.`hire_date`
  FROM `school_db_instructor`
 WHERE `school_db_instructor`.`hire_date` < '2010-01-01'
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Find all courses that belong to the instructor that has the primary key of 2
# Print the instructors name and courses that he belongs to in the terminal 
# (Do not hard code his name in the print)
def problem_three(request):

  instructor_2_courses = Course.objects.filter(instructor_id = 2)
  instructor_2 = Instructor.objects.get(id = 2)

  print(f'Instructor Name {instructor_2.first_name} {instructor_2.last_name}')
  print('Courses:')

  for course in instructor_2_courses:
    print(f'    - {course.name}')

  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#get
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter
"""

# Expected Terminal Response: (format print challenge!)
"""
Instructor Name: Colin Robinson
Courses:
    - Science
    - History
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
# First Query:

SELECT `school_db_instructor`.`id`,
       `school_db_instructor`.`first_name`,
       `school_db_instructor`.`last_name`,
       `school_db_instructor`.`hire_date`
  FROM `school_db_instructor`
 WHERE `school_db_instructor`.`id` = 2
 LIMIT 21

# Second Query:

 SELECT `school_db_course`.`id`,
       `school_db_course`.`name`,
       `school_db_course`.`instructor_id`,
       `school_db_course`.`credits`
  FROM `school_db_course`
 WHERE `school_db_course`.`instructor_id` = 2
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Get the count of students, courses, and instructors and print them in the terminal
def problem_four(request):
  students_count = Student.objects.count()
  courses_count = Course.objects.count()
  instructors_count = Instructor.objects.count()

  print(f'''
  Students Count: {students_count}
  Courses Count: {courses_count}
  Instructors Count: {instructors_count}
  ''')

  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#count
"""

# Expected Terminal Response:
"""
Students Count: 10
Courses Count: 10
Instructors Count: 6
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
# First Query:

SELECT COUNT(*) AS `__count`
  FROM `school_db_student`

# Second Query:

SELECT COUNT(*) AS `__count`
  FROM `school_db_course`

# Third Query:

SELECT COUNT(*) AS `__count`
  FROM `school_db_instructor`
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# CRUD Operations (Create, Read, Update, Delete)
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Create a new student in the database. Use your information!
# Print the new student's id, full name, year, and gpa to the terminal
# NOTE every time you execute this function a duplicate student will be created with a different primary key number
def problem_five(request):

  new_student = Student.objects.create(first_name = 'Deysha', last_name = 'Williams', year = 2013, gpa = 3.8)
  
  print(f'''
  Id: {new_student.id}
  Full Name: {new_student.first_name} {new_student.last_name}
  Year: {new_student.year}
  GPA: {new_student.gpa}
  ''')
  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#create
"""

# Expected Terminal Response:
"""
Id: 11
Full Name: Kyle Harwood
Year: 2022
GPA: 3.0
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
INSERT INTO `school_db_student` (`first_name`, `last_name`, `year`, `gpa`)
# NOTE: The information in the values will be what you chose
VALUES ('Kyle', 'Harwood', 2022, 3.0)
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Query the previoiusly created student by the id and update the "gpa" to a new value
# Then query the studets table to get that student by their id
# Print the new student's id, full name, and gpa to the terminal
def problem_six(request):
    
    # Make sure to set this equal to the primary key of the row you just created!
    new_student_update = Student.object.filter(student_id = 11).update(gpa = 3.9)

    print(f'''
    Id: {new_student_update.id}
    Full Name: {new_student_update.first_name} {new_student_update.last_name}
    GPA: {new_student_update.gpa}
    ''')


    return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#update
"""

# Expected Terminal Response:
"""
Id: 11
Full Name: Kyle Harwood
GPA: 3.5
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
# Query One:

UPDATE `school_db_student`
# NOTE: The gpa value will be what you chose
   SET `gpa` = 3.5
 WHERE `school_db_student`.`id` = 11

# Query Two:

SELECT `school_db_student`.`id`,
    `school_db_student`.`first_name`,
    `school_db_student`.`last_name`,
    `school_db_student`.`year`,
    `school_db_student`.`gpa`
FROM `school_db_student`
WHERE `school_db_student`.`id` = 11
LIMIT 21
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Delete the student that you have created and updated
# Check your MySQL Workbench to confirm the student is no longer in the table!
def problem_seven(request):

    # Make sure to set this equal to the primary key of the row you just created!
    deleted_student = Student.objects.delete(student_id = 11)

    try:
        student = Student.objects.get(pk=deleted_student)
    except ObjectDoesNotExist:
        print('Great! It failed and couldnt find the object because we deleted it!')

    return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#delete
"""

# Expected Terminal Response:
"""
Great! It failed and couldnt find the object because we deleted it!
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
# Query One:

SELECT `school_db_student`.`id`,
       `school_db_student`.`first_name`,
       `school_db_student`.`last_name`,
       `school_db_student`.`year`,
       `school_db_student`.`gpa`
  FROM `school_db_student`
 WHERE `school_db_student`.`id` = 15

 # Query Two:

 DELETE
  FROM `school_db_studentcourse`
 WHERE `school_db_studentcourse`.`student_id` IN (15)

 # Query Three: - NOTE this query is included in the starter code. See the query in the try catch

SELECT `school_db_student`.`id`,
       `school_db_student`.`first_name`,
       `school_db_student`.`last_name`,
       `school_db_student`.`year`,
       `school_db_student`.`gpa`
  FROM `school_db_student`
 WHERE `school_db_student`.`id` = 15
 LIMIT 21
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Find all of the instructors that only belong to a single course
# Print out the instructors full name and number of courses to the console
def bonus_problem(request):



    return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#annotate
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#count
"""

# Expected Terminal Response:
"""
Instructor Name: Guillermo de la Cruz
Instructor Name: Brad Baskshi
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
SELECT `school_db_instructor`.`id`,
       `school_db_instructor`.`first_name`,
       `school_db_instructor`.`last_name`,
       `school_db_instructor`.`hire_date`,
       COUNT(`school_db_course`.`id`) AS `course__count`
  FROM `school_db_instructor`
  LEFT OUTER JOIN `school_db_course`
    ON (`school_db_instructor`.`id` = `school_db_course`.`instructor_id`)
 GROUP BY `school_db_instructor`.`id`
HAVING COUNT(`school_db_course`.`id`) = 1
 ORDER BY NULL
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Dont worry about this! You will learn about this in the next class day!
def complete(req):
    context = view_information[req.path]
    return render(req, 'school/index.html', context)