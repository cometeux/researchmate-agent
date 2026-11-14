import unittest
from utils.evidence import validate_answer,render_answer
class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.sources=[{'text':'The study included 120 participants across three universities.', 'paper_name':'paper.pdf','page_number':7}]
        self.claim={'text':'The sample included 120 people.','source_id':'S1','quote':'The study included 120 participants'}
    def test_valid(self): self.assertEqual(validate_answer({'claims':[self.claim]},self.sources)[0]['page_number'],7)
    def test_invented_quote(self):
        self.claim['quote']='The study included 500 participants'
        with self.assertRaises(ValueError):validate_answer({'claims':[self.claim]},self.sources)
    def test_unknown_source(self):
        self.claim['source_id']='S2'
        with self.assertRaises(ValueError):validate_answer({'claims':[self.claim]},self.sources)
    def test_negative_source(self):
        self.claim['source_id']='S0'
        with self.assertRaises(ValueError):validate_answer({'claims':[self.claim]},self.sources)
    def test_tiny_quote(self):
        self.claim['quote']='The'
        with self.assertRaises(ValueError):validate_answer({'claims':[self.claim]},self.sources)
    def test_empty_evidence(self):self.assertIn('not provide enough evidence',render_answer(validate_answer({'claims':[]},[])))
    def test_unstructured(self):
        with self.assertRaises(ValueError):validate_answer({'answer':'unsupported'},self.sources)
    def test_whitespace(self):
        self.claim['quote']='The study included\n120 participants'
        self.assertEqual(len(validate_answer({'claims':[self.claim]},self.sources)),1)
if __name__=='__main__':unittest.main()
