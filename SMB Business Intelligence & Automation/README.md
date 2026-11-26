# SMB Business Intelligence & Automation

A practical project to help small and medium businesses turn operational data into useful reporting and automate repeatable work.

## Goals

- Make business reporting clearer and more reliable.
- Reduce manual work through useful automation.
- Keep data preparation and AI assisted workflows repeatable.
- Document setup and usage as the project develops.

## Getting started

Install [uv](https://docs.astral.sh/uv/) and use Python 3.12 or newer. From this folder:

```sh
uv sync
uv run smb-business-intelligence-automation
```

The command currently confirms the starter package is installed; business workflows will be added as the first use case is defined.

To check that the lockfile matches the project metadata, run:

```sh
uv lock --check
```

## Commit messages

Use `<type>: [M<number>] - <description>`, for example `feat: [M1] - add business metrics overview`. From the repository root, enable the included check once per clone with:

```sh
git config core.hooksPath .githooks
```
