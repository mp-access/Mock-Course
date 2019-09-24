class UniPerson(object):

    def __init__(self, name):
        self._name = name
        self.__inbox = []

    def receive_email(self, text):
        self.__inbox.append(text)

    def read_emails(self):
        emails = self.__inbox
        self.__inbox = []
        return emails

    def __str__(self):
        return f"Name: {self._name}"


class Student(UniPerson):
    yearly_student_counter = {}

    def __init__(self, name, start_year, has_graduated, ects):
        UniPerson.__init__(self, name)

        if start_year not in Student.yearly_student_counter:
            Student.yearly_student_counter[start_year] = 0

        counter = str(Student.yearly_student_counter[start_year]).zfill(5)

        self.__legi_nr = f"{start_year}-{counter}"
        Student.yearly_student_counter[start_year] += 1

        self.has_graduated = has_graduated
        self.__ects = ects

    def __str__(self):
        return UniPerson.__str__(self) + f", legi number: {self.__legi_nr}, graduated: {self.has_graduated}, ects: {self.__ects}"


class Lecturer(UniPerson):

    def __init__(self, name, lecture_name):
        UniPerson.__init__(self, name)
        self.__lecture_name = lecture_name

    def __str__(self):
        return UniPerson.__str__(self) + f", lecture name: {self.__lecture_name}"


class UniManagement(object):

    def __init__(self):
        self.__persons = []

    def add_person(self, person):
        if isinstance(person, UniPerson):
            self.__persons.append(person)

    def list_persons(self):
        # Elegant way with map and lambda
        return list(map(lambda p: p.__str__(), self.__persons))

        # Conventional way with for loop
        # list = []
        # for p in self.__persons:
        #     list.append(p.__str__())
        # return list

    def send_email(self, text):
        for person in self.__persons:
            person.receive_email(text)

    def count_alumni(self):
        # Elegant way with filter and lambda
        return len(list(filter(lambda p: isinstance(p, Student) and p.has_graduated, self.__persons)))

        # Conventional way with for loop
        # number_of_alumni = 0
        # for p in self.__persons:
        #     if isinstance(p, Student) and p.has_graduated:
        #         number_of_alumni += 1
        # return number_of_alumni
