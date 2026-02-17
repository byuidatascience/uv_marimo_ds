# UV + Marimo Data Science Environment

A simple repository that gets students up and running in a Marimo data science environment quickly using UV.

## What You Get

- **Python 3.11+** managed by UV
- **Marimo** - An interactive Python notebook environment
- **Essential Data Science Packages**: pandas, numpy, matplotlib, seaborn, scikit-learn, plotly
- **One-line setup** that works on both Windows and Mac OS

## Quick Start

### 1. Install UV (One-time setup)

**On Mac OS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Download/Clone folder

#### Non-Git users

1. [Download this repository](https://github.com/byuidatascience/uv_marimo_ds/archive/refs/heads/main.zip)
2. Unzip the zipped folder into your desired location

#### Git users

Fork this repository and clone it to your computer.


### 3. Run One-line start up 

After installing UV and downloading/cloning the folder. Open a terminal in the respective folder and run this single command to start work:

```bash
uv run marimo edit example.py
```

If you would like to avoid the not quite errors that get printed you can run

```bash
./run_marimo.sh 
```

That's it! 🎉

## What Just Happened?

When you ran `uv run marimo edit example.py`:
1. UV automatically installed Python 3.11 (if not already present)
2. UV created a virtual environment
3. UV installed all required packages (marimo, polars, plotly, etc.)
4. Marimo started and opened the example notebook in your browser

## Working with the Environment

### Running the Example Notebook
```bash
uv run marimo edit example.py
```

### Creating a New Notebook
```bash
uv run marimo new my_notebook.py
```

### Running a Notebook as an App
```bash
uv run marimo run example.py
```

### Adding More Packages

To add more Python packages, edit `pyproject.toml` and add them to the `dependencies` list:
```toml
dependencies = [
    "marimo>=0.9.0",
    "pandas>=2.2.0",
    # Add your packages here
    "requests>=2.31.0",
]
```

### Configuring your Marimo

- You can move panels between the [Sidebar and the Developer Panel](https://docs.marimo.io/guides/editor_features/panels/?h=sidebar). 
- You can [configure Marimo](https://docs.marimo.io/guides/configuration/#user-configuration) for your specific user needs.
- [Read their user guides](https://docs.marimo.io/guides/)


## What is UV?

[UV](https://github.com/astral-sh/uv) is an extremely fast Python package installer and resolver, written in Rust. It's 10-100x faster than pip and manages Python versions automatically.

## What is Marimo?

[Marimo](https://marimo.io) is a reactive Python notebook that:
- Runs as an interactive web app
- Automatically updates cells when dependencies change
- Can be executed as a Python script
- Is stored as pure Python (.py files)
- Works great with version control (git)

## Troubleshooting

### UV Command Not Found (Mac/Linux)
After installing UV, restart your terminal or run:
```bash
source $HOME/.cargo/env
```

### UV Command Not Found (Windows)
After installing UV, restart PowerShell. If still not working, you may need to add UV to your PATH.

**📖 See our detailed [Windows PATH Setup Guide](WINDOWS_PATH_SETUP.md) for step-by-step instructions.**

Quick fix - Run this in PowerShell as Administrator:
```powershell
$uvPath = "$env:USERPROFILE\.cargo\bin"
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";$uvPath", "User")
```
Then restart PowerShell.

### Python Version Issues
UV will automatically install Python 3.11 as specified in `.python-version`. If you need a different version, edit that file.

## Repository Structure

```
uv_marimo_ds/
├── .python-version         # Specifies Python version (3.11)
├── pyproject.toml          # Project dependencies and metadata
├── example.py              # Example Marimo notebook
├── README.md               # This file
└── WINDOWS_PATH_SETUP.md   # Windows PATH troubleshooting guide
```

## Learning Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [Marimo Documentation](https://docs.marimo.io/)
- [Marimo Tutorial](https://docs.marimo.io/getting_started/tutorial.html)
