# following https://realpython.com/testing-third-party-apis-with-mocks/#first-steps
from unittest.mock import Mock, patch
# Third-party imports...
from nose.tools import assert_is_not_none

from Main import getRepoandCommits

@patch('Main.requests.get')
def testgetRepo(mock_get): 
    mock_get.return_value.ok = True
    response = getRepoandCommits("SWiessler")
    assert_is_not_none(response)
    # ['Repo: CS-546 Number of commits: 30', 'Repo: Complexity Number of commits: 30', 'Repo: SSW-423 Number of commits: 1', 'Repo: SSW345 Number of commits: 3', 'Repo: WiesslerGitApi567 Number of commits: 4', 'Repo: express-api Number of commits: 2', 'Repo: ssw423_hw1 Number of commits: 3', 'Repo: wiessler_triangle Number of commits: 12']

