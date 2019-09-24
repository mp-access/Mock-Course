from unittest import TestCase

from task_2 import UniPerson, Student, Lecturer, UniManagement


class Task2Test(TestCase):

    def setUp(self):
        self.person1 = UniPerson("Person1")

        self.student1 = Student("Student1", 2000, True, 120)
        self.student2 = Student("Student2", 2000, False, 119)
        self.student3 = Student("Student3", 2001, True, 180)

        self.lecturer1 = Lecturer("Lecturer1", "Info1")

        self.mgmt = UniManagement()

    def test_uni_person_init(self):
        self.assertTrue(hasattr(self.person1, "_name"), "You must initialize the _name variable for UniPerson")
        self.assertEqual(self.person1._name, "Person1", "_name seems wrong")

        self.assertTrue(hasattr(self.person1, "_UniPerson__inbox"), "You must initialize __inbox as an empty list")
        self.assertEqual(self.person1._UniPerson__inbox, [], "__inbox seems wrong")

    def test_uni_person_str(self):
        self.assertEqual(self.person1.__str__(), "Name: Person1", "__str__ of UniPerson seems wrong")

    def test_uni_person_email(self):
        self.assertTrue(hasattr(self.person1, "read_emails"), "You must declare read_emails")
        self.assertTrue(hasattr(self.person1, "receive_email"), "You must declare receive_email")

        self.assertEqual(self.person1.read_emails(), [], "Reading emails before receiving any emails should return an empty inbox")

        self.person1.receive_email("Email1")
        self.person1.receive_email("Email2")

        self.assertEqual(self.person1.read_emails(), ["Email1", "Email2"], "Reading emails seems wrong")

        self.assertEqual(self.person1.read_emails(), [], "Reading emails should clear inbox")

    def test_student_init(self):
        self.assertTrue(isinstance(self.student1, UniPerson), "Student must inherit from UniPerson")

        self.assertTrue(hasattr(self.student1, "_name"), "You must initialize the _name variable for Student")
        self.assertEqual(self.student1._name, "Student1", "_name seems wrong")

        self.assertTrue(hasattr(self.student1, "has_graduated"), "You must initialize has_graduated for Student")
        self.assertTrue(self.student1.has_graduated, "has_graduated seems wrong")

        self.assertTrue(hasattr(self.student1, "has_graduated"), "You must initialize __ects for Student")
        self.assertEqual(self.student1._Student__ects, 120, "__ects seems wrong")

    def test_student_legi_nr(self):
        # Create new students to avoid side effects
        s1 = Student("S1", 2015, False, 0)

        for i in range(1500):
            s = Student("", 2015, False, 0)

        s1502 = Student("S1502", 2015, False, 0)

        s3 = Student("S3", 2016, False, 0)

        self.assertTrue(hasattr(s1, "_Student__legi_nr"), "You must initialize __legi_nr for Student")

        self.assertEqual(s1._Student__legi_nr, "2015-00000", "Your implementation of legi_nr seems wrong")
        self.assertEqual(s1502._Student__legi_nr, "2015-01501", "Your implementation of legi_nr seems wrong")
        self.assertEqual(s3._Student__legi_nr, "2016-00000", "Your implementation of legi_nr seems wrong")

    def test_student_str(self):
        self.assertTrue("True" in self.student1.__str__(), "Your __str__ implementation of Student must contain the value of has_graduated")
        self.assertTrue("False" in self.student2.__str__(), "Your __str__ implementation of Student must contain the value of has_graduated")

        self.assertTrue("119" in self.student2.__str__(), "Your __str__ implementation of Student must contain the value of __ects")

        s1 = Student("S1", 2018, False, 0)
        self.assertTrue("2018-00000" in s1.__str__(), "Your __str_ implementation of Student must contain the value of __legi_nr")

    def test_lecturer_init(self):
        self.assertTrue(isinstance(self.lecturer1, UniPerson), "Lecturer must inherit from UniPerson")

        self.assertTrue(hasattr(self.lecturer1, "_name"), "You must initialize the _name variable for Lecturer")
        self.assertEqual(self.lecturer1._name, "Lecturer1", "_name seems wrong")

        self.assertTrue(hasattr(self.lecturer1, "_Lecturer__lecture_name"), "You must initialize the __lecture_name variable for Lecturer")
        self.assertEqual(self.lecturer1._Lecturer__lecture_name, "Info1", "__lecture_name seems wrong")

    def test_lecturer_str(self):
        self.assertTrue("Info1" in self.lecturer1.__str__(), "Your __str__ implementation of Lecturer must contain the value of __lecture_name")

    def test_mgmt_init(self):
        self.assertTrue(hasattr(self.mgmt, "_UniManagement__persons"), "You must initialize __persons for UniManagement")
        self.assertEqual(self.mgmt._UniManagement__persons, [], "__persons seems wrong")

    def test_mgmt_add_person(self):
        self.assertTrue(hasattr(self.mgmt, "add_person"), "You must implement the add_person method for UniManagement")

        self.mgmt.add_person(self.student1)
        self.assertEqual(self.mgmt._UniManagement__persons, [self.student1], "Your implementation of add_person seems wrong")

        self.mgmt.add_person(self.lecturer1)
        self.assertEqual(self.mgmt._UniManagement__persons, [self.student1, self.lecturer1], "Your implementation of add_person seems wrong")

        self.mgmt.add_person("Wrong data type")
        self.assertEqual(self.mgmt._UniManagement__persons, [self.student1, self.lecturer1], "Your implementation of add_person seems wrong; it shouldn't be possible to add a wrong data type")

    def test_mgmt_list_persons(self):
        self.assertTrue(hasattr(self.mgmt, "list_persons"), "You must implement the list_persons method for UniManagement")

        self.assertEqual(self.mgmt.list_persons(), [], "list_persons seems wrong")

        self.mgmt.add_person(self.person1)
        self.mgmt.add_person(self.student1)
        self.mgmt.add_person(self.lecturer1)

        persons = self.mgmt.list_persons()

        self.assertTrue(isinstance(persons, list), "list_persons must return a list")
        self.assertEqual(len(persons), 3, "The length of your list seems wrong")

        self.assertEqual(persons[0], self.person1.__str__(), "The elements of list_persons should be the __str__ representations of the persons")
        self.assertEqual(persons[1], self.student1.__str__(), "The elements of list_persons should be the __str__ representations of the persons")
        self.assertEqual(persons[2], self.lecturer1.__str__(), "The elements of list_persons should be the __str__ representations of the persons")

    def test_mgmt_send_email(self):
        self.assertTrue(hasattr(self.mgmt, "send_email"), "You must implement the send_email method for UniManagement")

        self.mgmt.add_person(self.person1)
        self.mgmt.add_person(self.student1)
        self.mgmt.add_person(self.lecturer1)

        self.mgmt.send_email("Email1")

        self.assertEqual(self.person1.read_emails(), ["Email1"], "send_email seems wrong")
        self.assertEqual(self.student1.read_emails(), ["Email1"], "send_email seems wrong")
        self.assertEqual(self.lecturer1.read_emails(), ["Email1"], "send_email seems wrong")

    def test_mgmt_count_alumni(self):
        self.assertTrue(hasattr(self.mgmt, "count_alumni"), "You must implement the count_alumni method for UniManagement")

        self.assertEqual(self.mgmt.count_alumni(), 0, "count_alumni seems wrong")

        self.mgmt.add_person(self.person1)
        self.mgmt.add_person(self.student1)
        self.mgmt.add_person(self.student2)
        self.mgmt.add_person(self.lecturer1)

        self.assertEqual(self.mgmt.count_alumni(), 1, "count_alumni seems wrong")
        self.mgmt.add_person(self.student3)
        self.assertEqual(self.mgmt.count_alumni(), 2, "count_alumni seems wrong")
