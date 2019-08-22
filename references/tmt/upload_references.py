import sys

with open("GITHUB_TOKEN") as f:
    TOKEN=f.read().strip()
from github import Github
g = Github(TOKEN)
repo = g.get_repo("oirlab/tmt-crds-cache")    
release = repo.get_release(sys.argv[1])
release.upload_asset(sys.argv[2])
