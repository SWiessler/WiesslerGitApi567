import requests
import json

def getRepoandCommits(user):
    # retrieves repositories of given user 
    repos = requests.get("https://api.github.com/users/" + user + "/repos").json()
    repo_list = []
    for obj in repos:
        # retrieves number of commits of a given user repo
        commits = requests.get("https://api.github.com/repos/" +user+ "/" + obj['name'] + "/commits").json()
        repo_list.append('Repo: ' + obj['name'] + ' Number of commits: ' + str(len(commits)))
    return sorted(repo_list)
