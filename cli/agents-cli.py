import requests
from parser.parse_agents import parse_agents_file

def fetch_agents(root_url: str):
    url = root_url.rstrip("/") + "/agents.txt"
    res = requests.get(url, timeout=2)
    res.raise_for_status()
    return parse_agents_file(res.text)

if __name__ == "__main__":
    import sys
    root_url = sys.argv[1]
    print(fetch_agents(root_url))
