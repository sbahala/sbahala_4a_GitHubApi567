# -*- coding: utf-8 -*-
"""
Proram to access te GitHub url and print the repositories and number of commits
@input-GitHub userId
@author: Sushmita bahala
"""



import requests

def getCommits_url(user,name):
    getCommits_url ="https://api.github.com/repos/"+f'{user}' +"/" + name + "/commits"
    commitResp = requests.get(getCommits_url)
    commitResp_json = commitResp.json()
    val=len(commitResp_json);
    return val    


def getResp(user):
    getRepos_url = "https://api.github.com/" + "users" + "/" + f'{user}' + "/repos"
    resp = requests.get(getRepos_url)
    repo_json = resp.json()
    if len(repo_json) != '':
        for i in repo_json:
            num = getCommits_url(f'{user}',f'{i["name"]}')
            print(f'Repo: {i["name"]} and Number of commits: {num}')
        return 'success'    
    else:
        return 'WrongAttempt'

 
def main():
    user = input("Enter the GitHub User Id: ")
    getResp(user)
   

if __name__ == "__main__":
    main()    

