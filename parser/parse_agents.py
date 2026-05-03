import yaml

def parse_agents_file(content: str):
    try:
        return yaml.safe_load(content)
    except Exception as e:
        raise ValueError(f"Invalid agents.txt format: {e}")
