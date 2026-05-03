# agents.txt

A minimal, machine-readable capability declaration for AI agents interacting with websites.

## Why

Agents currently scrape HTML, guess workflows, and hallucinate capabilities. That breaks real-world workflows (like field ops, tokenized uploads, phone-only booking, etc.).

`agents.txt` flips that:

> The site declares capabilities, the agent adapts behavior.

## Usage

Place a file at:

https://yoursite.com/agents.txt

Agents should:
1. Fetch `/agents.txt`
2. Parse capabilities
3. Adapt behavior (prefer structured endpoints over scraping)

## Example

User-Agent: *
Allow: /

Capabilities:
  - photo-upload: /api/upload-photo
  - voice-upload: /api/upload-voice
  - vault-queue: /api/queue

Booking:
  method: phone-only
  phone_number: "724-555-1234"
  required-info: [name, date, service]

Rate-Limits:
  upload: "10/min"

Preferred-Interaction:
  - fetch agents.txt first
  - use structured endpoints
  - avoid scraping UI

## Parser / CLI

Install:

pip install -r requirements.txt

Parse a file:

python -c "from parser.parse_agents import parse_agents_file; print(parse_agents_file(open('examples/basic.txt').read()))"

Fetch + parse from a site:

python cli/agents-cli.py https://yoursite.com

## Status

Experimental. Pragmatic. Working. Contributions welcome.
