# Security

Project Eden is local-first. That only stays true if we do not
accidentally grow a cloud brain.

## Please report

- Anything that phones home without an explicit user action
- Path traversal in checklist / file writers
- Dependency changes that pull telemetry by default
- Scripts that download weights over plain HTTP without a checksum path

## Do not report here

- "This loss default does not match vendor X" — open a normal issue
- Model quality complaints
- Feature ideas

## How to report

Open a GitHub issue titled `SECURITY:` if there is no private advisory
path available on the account yet, and do not attach customer data.

There is no bug bounty. There is gratitude and a fast patch.
