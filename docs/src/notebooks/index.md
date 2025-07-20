# Jupyter Notebooks

This section contains the complete tutorial as interactive Jupyter notebooks that you can run directly in VS Code. Each notebook builds on the previous one, so it's recommended to work through them in order.

## Getting Started

Make sure you've completed the [VS Code Setup](../vscode_setup.md) before starting with these notebooks. You'll need:

- VS Code with Python and Jupyter extensions installed
- A Python environment with pandas, matplotlib, seaborn, and altair installed
- Basic familiarity with VS Code's notebook interface

## How to Use These Notebooks

1. **Download or clone** this repository to your local machine
2. **Open VS Code** and navigate to the project folder
3. **Open any notebook** by clicking on the `.ipynb` files in the `docs/src/notebooks/` directory
4. **Run cells sequentially** by clicking the play button or pressing `Shift+Enter`
5. **Experiment** by modifying the code and running your changes

Each notebook is self-contained and includes all necessary imports and data loading, so you can start with any chapter that interests you.

## Tutorial Notebooks

```{toctree}
:maxdepth: 1

pandas.ipynb
dataframe.ipynb
columns.ipynb
filters.ipynb  
groupby.ipynb
merge.ipynb
compute.ipynb
sorting.ipynb
concat.ipynb
charts.ipynb
export.ipynb
```

## Notebook Descriptions

Each notebook is self-contained and includes all necessary imports and data loading. However, they build conceptually on each other:

- **pandas.ipynb**: Introduction to pandas and Series objects
- **dataframe.ipynb**: Working with DataFrames and loading CSV data  
- **columns.ipynb**: Adding, renaming, and manipulating DataFrame columns
- **filters.ipynb**: Filtering data with boolean indexing and queries
- **groupby.ipynb**: Grouping and aggregating data for analysis
- **merge.ipynb**: Joining datasets using merge operations
- **compute.ipynb**: Mathematical operations and calculations
- **sorting.ipynb**: Sorting data by different criteria
- **concat.ipynb**: Concatenating DataFrames vertically and horizontally
- **charts.ipynb**: Creating visualizations with matplotlib, seaborn, and altair
- **export.ipynb**: Saving your analysis results to various file formats

## Alternative: Markdown Chapters

If you prefer reading the tutorial as traditional documentation, you can also access the same content as markdown chapters in the main tutorial. The notebooks provide an interactive experience, while the markdown chapters are better for reference and quick lookup.
- **sorting.ipynb**: Sorting DataFrames 
- **filters.ipynb**: Filtering and selecting data
- **columns.ipynb**: Working with columns and data types
- **merge.ipynb**: Joining datasets together
- **compute.ipynb**: Calculating new columns and statistics
- **concat.ipynb**: Combining DataFrames
- **export.ipynb**: Saving your work
- **charts.ipynb**: Creating visualizations with Altair

## Tips for Success

- **Run cells in order**: While each notebook loads its own data, the concepts build on each other
- **Experiment**: Try modifying the code to see what happens
- **Use VS Code features**: Take advantage of IntelliSense, debugging, and the variable explorer
- **Save frequently**: Use `Ctrl+S` (or `Cmd+S`) to save your notebooks as you work

Start with [pandas.ipynb](pandas.ipynb) to begin your data analysis journey!
