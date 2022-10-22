# -*- coding: utf-8 -*-
"""
Test class to test GitHub Api call
@author: Sushmita bahala
"""


import unittest
from unittest.mock import patch
from nose.tools import assert_true
from GitHubApi import getResp
from GitHubApi import getCommits_url
import requests


class TesttestApi(unittest.TestCase):

     @patch('GitHubApi.requests.get')
     def testNumberofRepo(self,mock):##mocked the url directly
         mock.get('https://api.github.com/users/sbahala/repos', text='success')
         self.assertEqual(getResp('https://api.github.com/users/sbahala/repos'), 'success')
         
     @patch('GitHubApi.requests.get')   
     def testNumCommits(self,mock):##mocked the url directly
         mock.get('https://api.github.com/repos/sbahala/Triangle567_2A/commits', 0)
         self.assertEqual(getCommits_url('https://api.github.com/repos/sbahala/Triangle567_2A/commits','scy'), 0)
     
     def testUrlRepo(self):## fetching the response
         response = requests.get('https://api.github.com/users/sbahala/repos')
         assert_true(response.ok)
         
     def testrepoCommits(self):## fetching the response
         response = requests.get('https://api.github.com/repos/sbahala/Triangle567_2A/commits')
         assert_true(response.ok)
                
     @patch('GitHubApi.requests.get')
     def testGetRepo(self,mock):## mocking the function getResp which has the repo url
         mock.get.response = "success"
         response = getResp('sbahala')
         assert_true(response)
      
     @patch('GitHubApi.requests.get')
     def testGetCommit(self,mock):## mocking the function getCommits_url which has the commit url
         mock.get.response = "success"
         response = getCommits_url('sbahala','Triangle567_2A')
         assert_true(response.as_integer_ratio())
          
if __name__ == '__main__':
   unittest.main()
   
