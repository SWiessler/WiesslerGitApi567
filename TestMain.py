import unittest

from Main import getRepo
from Main import getCommits

class TestMain(unittest.TestCase):
    def testgetRepo(self): 
        self.assertEqual(getRepo("SWiessler"),['CS-546', 'Complexity', 'SSW-423', 'SSW345', 'WiesslerGitApi567', 'express-api', 'ssw423_hw1', 'wiessler_triangle'])
    def testgetCommits(self):
        self.assertEqual(getCommits("SWiessler", "wiessler_triangle"),'Number of commits by SWiessler to wiessler_triangle: 12')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
