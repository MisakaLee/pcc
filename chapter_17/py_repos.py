import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Staus code:",r.status_code)

response_dict = r.json()
print("Total respositories:",response_dict['total_count'])
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))
repo_dicts = repo_dicts[0]
print("\nSelected information about first repository:")
print('Name:',repo_dicts['name'])
print('Owner:',repo_dicts['owner']['login'])
print('Stars:',repo_dicts['stargazers_count'])
print('Repository:',repo_dicts['html_url'])
print('Created:',repo_dicts['created_at'])
print('Updated:',repo_dicts['updated_at'])
print('Description:',repo_dicts['description'])

