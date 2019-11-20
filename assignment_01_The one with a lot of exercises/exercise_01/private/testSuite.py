from unittest import TestCase

#from public.script import Aircraft, IntercontinentalAircraft, ShortHaulAircraft, ControlTower

import os
import importlib
import importlib.util
from unittest.mock import patch

devnull = open(os.devnull, 'w')


def reload_module(module, path, user_input=(), outstream=devnull):
    with patch('sys.stdout', outstream):
        with patch('sys.stderr', outstream):
            with patch('builtins.input', side_effect=user_input):
                return load_module_from_file(module, path)


def load_module_from_file(module_name, file_path, input_side_effect=()):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)

    if input_side_effect:
        with patch('builtins.input', side_effect=input_side_effect):
            spec.loader.exec_module(module)
    else:
        spec.loader.exec_module(module)
    return module

class Task1Test(TestCase):

    CTX = ''
    MODULE_NAME = 'public.script'
    TEST_FILE_PATH = './public/script.py'

    def setUp(self):
        print
        self.student_submission = reload_module(self.MODULE_NAME, './public/script.py', [])

    def test_inheritance(self):
        intercontinental_flight = self.student_submission.IntercontinentalAircraft(40, "intercontinental", 100)
        short_haul_flight = self.student_submission.ShortHaulAircraft(90, "short")

        self.assertTrue(isinstance(intercontinental_flight, self.student_submission.Aircraft),
                        "@@IntercontinentalAircraft should inherit from Aircraft@@")
        self.assertTrue(isinstance(short_haul_flight, self.student_submission.Aircraft), "@#@ShortHaulAircraft should inherit from Aircraft@#@")

    def test_aircraft_get_name(self):
        aircraft = self.student_submission.IntercontinentalAircraft(40, "intercontinental", 100)
        self.assertEqual(aircraft.get_name(), "intercontinental")

        aircraft = self.student_submission.ShortHaulAircraft(90, "short")
        self.assertEqual(aircraft.get_name(), "short")

    def test_aircraft_get_number_of_passengers(self):
        aircraft = self.student_submission.IntercontinentalAircraft(40, "intercontinental", 100)
        self.assertEqual(aircraft.get_number_of_passengers(), 40)

        aircraft = self.student_submission.ShortHaulAircraft(90, "short")
        self.assertEqual(aircraft.get_number_of_passengers(), 90)

    def test_calculate_amount_of_fuel_intercontinental(self):
        aircraft = self.student_submission.IntercontinentalAircraft(40, "intercontinental", 100)
        fuel = aircraft.calculate_amount_of_fuel(1000)
        self.assertEqual(fuel, 210000)

    def test_get_manifest_intercontinental(self):
        aircraft = self.student_submission.IntercontinentalAircraft(40, "intercontinental", 100)
        self.assertEqual(aircraft.manifest,
                         f"Intercontinental flight intercontinental: passenger count 40, cargo load 100")

    def test_calculate_amount_of_fuel_short_haul(self):
        aircraft = self.student_submission.ShortHaulAircraft(90, "short")
        fuel = aircraft.calculate_amount_of_fuel(1000)
        self.assertEqual(fuel, 9000)

    def test_get_manifest_short_haul(self):
        aircraft = self.student_submission.ShortHaulAircraft(40, "short")
        serial_number = aircraft.get_serial_number()
        self.assertEqual(aircraft.manifest,
                         f"Short haul flight serial number {serial_number}, name short: passenger count 40")

    def test_list_flights(self):
        intercontinental_flight = self.student_submission.IntercontinentalAircraft(500, "Boeing-747", 100)
        short_haul_flight = self.student_submission.ShortHaulAircraft(110, "Airbus-A220")
        short_haul_flight2 = self.student_submission.ShortHaulAircraft(85, "Airbus-A220")

        tower = self.student_submission.ControlTower()
        tower.add_aircraft(intercontinental_flight)
        tower.add_aircraft(short_haul_flight)
        tower.add_aircraft(short_haul_flight2)

        manifests = tower.get_manifests()
        self.assertEqual(manifests, [
            "Intercontinental flight Boeing-747: passenger count 500, cargo load 100",
            f"Short haul flight serial number {short_haul_flight.get_serial_number()}, name Airbus-A220: passenger count 110",
            f"Short haul flight serial number {short_haul_flight2.get_serial_number()}, name Airbus-A220: passenger count 85"])
