import unittest
from utils.validation import FIELDS, validate_analysis

class ValidationTests(unittest.TestCase):
    def valid(self): return dict.fromkeys(FIELDS, 'Not clearly stated')
    def test_filename_is_trusted(self):
        value = self.valid(); value['paper_name'] = 'invented.pdf'
        self.assertEqual(validate_analysis(value, 'actual.pdf')['paper_name'], 'actual.pdf')
    def test_missing_field(self):
        value = self.valid(); del value['title']
        with self.assertRaises(ValueError): validate_analysis(value, 'paper.pdf')
    def test_non_object(self):
        with self.assertRaises(ValueError): validate_analysis([], 'paper.pdf')
    def test_nested_value(self):
        value = self.valid(); value['authors'] = ['invented']
        with self.assertRaises(ValueError): validate_analysis(value, 'paper.pdf')
    def test_blank_value(self):
        value = self.valid(); value['year'] = ' '
        with self.assertRaises(ValueError): validate_analysis(value, 'paper.pdf')
    def test_extra_field(self):
        value = self.valid(); value['unexpected'] = 'value'
        with self.assertRaises(ValueError): validate_analysis(value, 'paper.pdf')

if __name__ == '__main__': unittest.main()
