import unittest

from Main import getRepoandCommits

class TestMain(unittest.TestCase):
    def testgetRepo(self): 
        self.assertEqual(getRepoandCommits("SWiessler"),['Repo: CS-546 Number of commits: 30', 'Repo: Complexity Number of commits: 30', 'Repo: SSW-423 Number of commits: 1', 'Repo: SSW345 Number of commits: 3', 'Repo: WiesslerGitApi567 Number of commits: 4', 'Repo: express-api Number of commits: 2', 'Repo: ssw423_hw1 Number of commits: 3', 'Repo: wiessler_triangle Number of commits: 12'])
   
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
