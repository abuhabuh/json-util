import unittest

import json_util.json_eval


class TestJsonParser(unittest.TestCase):

  def test_parse_normal(self):
    dict1 = {
      'animal': {
        'cat': {
          'names': ['garfield', 'john', 'tiffany']
        }
      }
    }

    self.assertEqual(json_util.json_eval.get_val(dict1, ['asdf']), None)
    self.assertEqual(json_util.json_eval.get_val(dict1, [0]), None)
    self.assertEqual(json_util.json_eval.get_val(dict1, []), None)
    self.assertEqual(json_util.json_eval.get_val(dict1, None), None)
    self.assertEqual(json_util.json_eval.get_val(None, None), None)
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', 0]), 'garfield')
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', 3]), None)
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', -1]), 'tiffany')
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', -4]), None)
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', 'a']), None)
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', 'a', 'b']), None)

  def test_parse_empty(self):
    dict1 = {}

    self.assertEqual(json_util.json_eval.get_val(dict1, ['asdf']), None)
    self.assertEqual(json_util.json_eval.get_val(dict1, [0]), None)
    self.assertEqual(json_util.json_eval.get_val(dict1, []), None)
    self.assertEqual(json_util.json_eval.get_val(dict1, None), None)
    self.assertEqual(json_util.json_eval.get_val(None, None), None)
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', 0]), None)
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', 3]), None)
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', -1]), None)
    self.assertEqual(
      json_util.json_eval.get_val(dict1, ['animal', 'cat', 'names', -4]), None)
