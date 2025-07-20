# Visual Studio Code Setup

[Visual Studio Code](https://code.visualstudio.com/) is a free, open-source code editor developed by Microsoft. It has become one of the most popular development environments for Python programming, offering excellent support for data analysis, debugging, and interactive computing.

VS Code provides an integrated experience for Python development that combines the best of traditional code editing with full Jupyter notebook support. You can create and run Jupyter notebooks directly in the editor, write Python scripts with interactive cells, and leverage powerful debugging and version control tools all in one place.

It is used by [data scientists](https://code.visualstudio.com/docs/python/data-science-tutorial), [researchers](https://code.visualstudio.com/docs/python/jupyter-support), [developers](https://code.visualstudio.com/docs/python/python-tutorial), and journalists to analyze data and create reproducible research.

Examples of data journalism projects that could be developed using VS Code include:

* Jupyter notebooks for investigating public records
* Interactive data exploration and analysis
* Automated data processing pipelines
* Version-controlled research projects
* Collaborative data investigations using Git integration

You can find thousands of Python projects on [GitHub](https://github.com/search?q=language%3APython+data+analysis&type=Repositories) that use VS Code for development, including projects by [The New York Times](https://github.com/nytimes), [FiveThirtyEight](https://github.com/fivethirtyeight), [BuzzFeed News](https://github.com/BuzzFeedNews), and many others.

There are several ways to set up Python development in VS Code. Since this tutorial is designed for beginners, we'll show you how to install VS Code and set up a Python environment that includes all the tools you need for data analysis.

```{note}
Advanced users who prefer command-line tools can still follow this tutorial, but may want to use their existing Python environments. The code examples will work in any Python environment with pandas and other data analysis libraries installed.
```

## Install Visual Studio Code

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/VqCgcpAypFQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

The first step is to visit [Visual Studio Code's homepage](https://code.visualstudio.com/) in your web browser.

![VS Code homepage](/_static/vscode-homepage.png)

Click the "Download for [Your Operating System]" button. The website should automatically detect your operating system and show the appropriate download.

The installation file will download to your computer. Find the file in your downloads directory and double-click it to begin the installation process. Follow the instructions presented by the installation wizard, sticking to the default options.

```{warning}
On macOS, you may need to drag VS Code to your Applications folder after downloading. On Windows, the installer will handle everything for you. On Linux, you may need to install via your package manager or using the downloaded .deb/.rpm file.
```

## Install Python Extension

Once VS Code is installed, open it and you'll see the Welcome screen. We need to install the Python extension to get the best Python development experience.

![VS Code welcome screen](/_static/vscode-welcome.png)

1. Click on the Extensions icon in the left sidebar (it looks like four squares)
2. Search for "Python" in the extensions marketplace
3. Find the official Python extension by Microsoft (it should be the first result)
4. Click "Install"

![Python extension](/_static/python-extension.png)

This extension provides:
- IntelliSense (code completion and suggestions)
- Debugging support
- Code formatting and linting
- Jupyter notebook support
- Interactive Python (REPL) support

## Install Jupyter Extension

Since we'll be working with Jupyter notebooks, also install the Jupyter extension:

1. In the Extensions panel, search for "Jupyter"
2. Find the official Jupyter extension by Microsoft
3. Click "Install"

![Jupyter extension](/_static/jupyter-extension.png)

This extension enables:
- Full Jupyter notebook (.ipynb) support directly in VS Code
- Interactive Python cells in .py files
- Variable explorer
- Data viewer for pandas DataFrames
- Notebook diffing and merge capabilities

## Set Up Python Environment

VS Code works with any Python installation on your system. If you don't have Python installed:

### For Beginners: Python from python.org

1. Visit [python.org](https://www.python.org/downloads/)
2. Download Python 3.8 or newer
3. Run the installer and make sure to check "Add Python to PATH"

### For Advanced Users: Anaconda, Miniconda, or uv

If you're familiar with Python environments, you can use:
- [uv](https://docs.astral.sh/uv/) (recommended - fast and modern Python package manager)
- [Anaconda](https://www.anaconda.com/products/distribution) (includes many data science packages)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (minimal installer)
- [pyenv](https://github.com/pyenv/pyenv) for managing multiple Python versions

## Verify Your Setup

Let's verify everything is working:

1. Open VS Code
2. Create a new file by pressing `Ctrl+N` (or `Cmd+N` on Mac)
3. Save it as `test.py` (press `Ctrl+S` or `Cmd+S`)
4. Type the following code:

```python
print("Hello, VS Code!")
```

5. Right-click in the editor and select "Run Python File in Terminal"

You should see "Hello, VS Code!" printed in the integrated terminal at the bottom of the screen.

![First Python program](/_static/vscode-hello-world.png)

## Install Required Packages

We'll need to install some Python packages for data analysis. This tutorial uses [uv](https://docs.astral.sh/uv/), a fast Python package manager that makes dependency management simple and reliable.

First, install uv if you haven't already. Open the integrated terminal in VS Code (`View > Terminal` or `Ctrl+`` `) and run:

**On macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative installation via pip:**
```bash
pip install uv
```

Once uv is installed, create a new Python project and install the required packages:

```bash
uv init first-python-notebook
cd first-python-notebook
uv add pandas matplotlib seaborn jupyter altair
```

This will:
- Create a new Python project with proper dependency management
- Install the required packages:
  - `pandas` for data manipulation
  - `matplotlib` and `seaborn` for plotting  
  - `jupyter` for notebook support
  - `altair` for interactive visualizations
- Create a `pyproject.toml` file to track your dependencies
- Set up a virtual environment automatically

```{note}
uv is much faster than pip and provides better dependency resolution. It automatically manages virtual environments for you, so you don't need to worry about environment conflicts. If you prefer other tools like Anaconda or pip, the code examples will still work, but uv provides a more streamlined experience.
```

## Your First Interactive Session

VS Code supports multiple ways to work with Python and Jupyter notebooks. If you set up your project with uv, make sure you're working in the project directory:

```bash
cd first-python-notebook
```

### Python Interactive Window

1. Create a new file and save it as `analysis.py` in your project directory
2. Add the following code:

```python
# %%
print("This is my first interactive cell")
x = 2 + 2
print(f"2 + 2 = {x}")
```

3. Click "Run Cell" above the `# %%` comment

This will open an Interactive Window where you can see the output, providing an interactive development experience integrated into VS Code.

### Jupyter Notebooks in VS Code

You can also create traditional Jupyter notebooks:

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette
2. Type "Jupyter: Create New Jupyter Notebook"
3. Press Enter

This creates a new `.ipynb` notebook file where you can add cells and run them interactively. VS Code provides the full notebook experience including:
- Rich output display (plots, tables, HTML)
- Variable explorer
- Kernel management
- Cell execution controls
- Markdown and code cells

## Selecting the Right Python Environment

After installing packages, it's crucial to ensure VS Code uses the correct Python environment. This is especially important if you have multiple Python installations.

### For Python Files (.py)

When working with Python files, VS Code needs to know which Python interpreter to use:

1. **Automatic Selection**: VS Code usually detects your Python installation automatically
2. **Manual Selection**: If needed, press `Ctrl+Shift+P` (or `Cmd+Shift+P`) and type "Python: Select Interpreter"
3. **Choose Your Environment**: Select the Python installation that has your packages installed:
   - If using uv: Look for the interpreter in your project's `.venv` folder
   - If using Anaconda: Choose the anaconda or miniconda interpreter
   - If using system Python: Choose the global Python installation

4. **Verify Selection**: Check the bottom-left status bar - it should show your selected Python version

### For Jupyter Notebooks (.ipynb)

Notebooks use "kernels" (similar to interpreters) to run code:

1. **Initial Kernel Selection**: When you create or open a notebook, VS Code may prompt you to select a kernel
2. **Manual Kernel Selection**: Click the kernel name in the top-right corner of the notebook to change it
3. **Choose the Right Kernel**: Select the same Python environment where you installed packages
4. **Verify Connection**: A green dot next to the kernel name means it's connected and ready

### Troubleshooting Environment Issues

If your imports don't work or packages aren't found:

1. **Check Active Environment**: Verify VS Code is using the environment where you installed packages
2. **Restart Kernel**: In notebooks, use "Restart Kernel" from the kernel menu
3. **Refresh Interpreters**: Use Command Palette → "Python: Refresh" to update the interpreter list
4. **Reinstall Packages**: If still having issues, reinstall packages in the correct environment

```{tip}
**Pro tip**: The status bar (bottom of VS Code) always shows your active Python interpreter. Make sure it matches the environment where you installed your packages!
```

Now you're ready to start learning Python for data analysis! The next chapter will introduce you to working with Jupyter notebooks in VS Code.
