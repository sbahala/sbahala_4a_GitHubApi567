# -*- coding: utf-8 -*-
"""
Test class to test GitHub Api call
@author: Sushmita bahala
"""


import unittest
from nose.tools import assert_true
import requests


class TesttestApi(unittest.TestCase):
     def testUrlRepo(self):
         response = requests.get('https://api.github.com/users/sbahala/repos')
         assert_true(response.ok)
     def testrepoCommits(self):
         response = requests.get('https://api.github.com/repos/sbahala/Triangle567_2A/commits')
         assert_true(response.ok)

if __name__ == '__main__':
   unittest.main()
   
