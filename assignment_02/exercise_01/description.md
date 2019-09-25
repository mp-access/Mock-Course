# Task: University Management (5 Points)

To familiarize yourself further with the concept of inheritance, in this task you will implement a simple university management software that manages students (enrolled and alumni) and lecturers.
Before you start coding, also read the detailed instructions carefully. It is important that you follow the instructions precisely and name your classes, variables and methods exactly as indicated.

**Instructions:**
Update to description
- Create a class UniPerson:
    * It must be initialized with a name argument. Store the name as a protected instance variable (for reference, see lecture slides page 62). Also create a private instance variable `__inbox` which is an empty list.
    * Define a method receive_email(text) which just stores (i.e., appends) the received text in the inbox.
    * Define a method read_emails which returns a list of all stored emails and empties the inbox. See the code for examples.
    * Overwrite the `__str__` method to return `Name: xyz`. See the code for examples.

- Create a class Student:
    * It must inherit from `UniPerson` and take the argument's `name, start_year, has_graduated` and `ects`. Call the constructor of the superclass. Initialize a public variable `has_graduated` and a private variable `__ects`.
    * Also in the constructor, initialize a private variable `__legi_nr`. It must be a string with the following format: `<start_year>-<five digit number>`. The five digit number must be increased for each new student with the same `start_year`, and start from zero for each student with a new `start_year`. To create a five digit number with zero-padding, check out Python’s string method `zfill1()` [https://docs.python.org/3/library/stdtypes.html?highlight=zfill#str.zfill]. Some examples: The 1st student of 2018 will have 2018-00000, the 5th student will have 2018-00004, the 555th will have 2018-00554, etc. You can assume that your university is rather small, so don’t worry about running out of available five-digits numbers for any given year.
    Hint: You may want to use a class variable that helps you count how many students are created with the same `start_year`.
    * Override the `__str__` method to return a more accurate description, including the superclass’s `__str__` output, the legi number, whether the student has graduated (`True` or `False) and the number of ECTS. You are free to choose a readable format yourself, it just needs to include the above-mentioned information.

- Create a class Lecturer:
    * It must inherit from `UniPerson` and take the arguments name and `lecture_name`. Call the constructor of the superclass and store the lecture name in a private instance variable `__lecture_name`.
    * Override the `__str__` method in a similar way as in the Student class, so that it includes the superclass’s `__str__` output and the lecture name.

- Finally, create a class UniManagement:
    * It must be initialized with no arguments, and an empty list `__persons` must be created upon initialization.
    * Define a method `add_person(person)` that checks whether the argument is an instance of `UniPerson` and if yes, adds it to the persons list.
    * Define a method `list_persons` that returns a list of string descriptions `(__str__)` of all persons in the list.
    * Define a method `send_email(text)` that sends an email to every person in the list.
    * Define a method `count_alumni` that returns the number of students in the list that have already graduated.
