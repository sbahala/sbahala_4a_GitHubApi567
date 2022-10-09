# -*- coding: utf-8 -*-
"""
Test class to test GitHub Api call
@author: Sushmita bahala
"""


import unittest
from unittest.mock import patch
from GitHubApi import getResp
from GitHubApi import getCommits_url


class TesttestApi(unittest.TestCase):
    @patch('GitHubApi.requests.get')
   
    def testNumberofRepo(self,mock):
        mock.get('https://api.github.com/users/sbahala/repos', text='success')
        self.assertEqual(getResp('https://api.github.com/users/sbahala/repos'), 'success')
       

    def testCommit(self):
        commits = getCommits_url('sbahala','Triangle567_2A')
        self.assertNotEquals(commits,4)
       

if __name__ == '__main__':
   unittest.main()
   
