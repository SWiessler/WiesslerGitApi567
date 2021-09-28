import requests
import json

def getRepo(user):
    # retrieves repositories of given user 
    repos = requests.get("https://api.github.com/users/" + user + "/repos").json()
    repo_list = []
    for obj in repos:
        repo_list.append(obj['name'])
    return sorted(repo_list)

def getCommits(user, repo):
    # retrieves number of commits of a given user repo
    commits = requests.get("https://api.github.com/repos/" +user+ "/" + repo + "/commits").json()
    return "Number of commits by " + user + " to " + repo + ": " + str(len(commits))
