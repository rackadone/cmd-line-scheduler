import unittest
from test_dsp import TestDateStringParser
from test_sm import TestStorageManager

def suite():
    suite = unittest.TestSuite()
    # DateStringParser Tests
    date_string_parser_tests = [
        'test_slash_format',
        'test_dash_format',
        'test_extra_strings',
        'test_leap_year',
        'test_get_ordinal',
    ]
    for tc in date_string_parser_tests:
        suite.addTest(TestDateStringParser(tc))

    # StorageManager Tests
    storage_manager_tests = [
        'test_file_create',
        'test_store_json_object',
        'test_get_json_object',
    ]
    for tc in storage_manager_tests:
        suite.addTest(TestStorageManager(tc))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)