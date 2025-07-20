# Contributing

How to propose changes to this repository.

## Installation

Fork the repository and clone it:

```bash
gh repo clone your-name/first-python-notebook-vscode
```

Change into the project directory:

```bash
cd first-python-notebook-vscode
```

Install the dependencies using uv (recommended) or pipenv:

**Using uv:**
```bash
uv sync
```

**Using pipenv:**
```bash
pipenv install
```

## Contributing

To start a test server that previews the site, use the following command:

```bash
make serve
```

Once it starts, visit [localhost:8000](http://localhost:8000) in your browser. Edits made in the `docs/` folder will appear immediately. Commit your changes to a branch and then submit a pull request to the source repository.
