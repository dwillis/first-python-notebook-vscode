# Dual Format Guide

This tutorial is available in two complementary formats designed to accommodate different learning preferences and use cases.

## Format Options

### 📖 Traditional Tutorial Chapters

**Best for**: Reading, reference, quick lookup, conceptual understanding

**Location**: `docs/src/*.md` files
- Comprehensive markdown documentation
- Embedded code examples with syntax highlighting  
- Detailed explanations and theory
- Easy to search and cross-reference
- Mobile-friendly reading experience

**How to use**: 
- Read online at the documentation site
- Browse the markdown files directly in VS Code
- Use for quick reference during development

### 📓 Interactive Jupyter Notebooks

**Best for**: Hands-on learning, experimentation, running code

**Location**: `docs/src/notebooks/*.ipynb` files
- Self-contained executable notebooks
- Run code directly and see immediate results
- Experiment with modifications and variations
- Full integration with VS Code's notebook features
- Variable explorer and debugging support

**How to use**:
- Open `.ipynb` files directly in VS Code
- Run cells sequentially or individually
- Modify code and explore different approaches
- Use for active learning and experimentation

## Content Synchronization

Both formats cover identical content and learning objectives:

| Chapter | Markdown File | Notebook File | Topic |
|---------|---------------|---------------|-------|
| Pandas Introduction | `pandas.md` | `pandas.ipynb` | pandas library basics |
| Working with Data | `dataframe.md` | `dataframe.ipynb` | DataFrames and CSV loading |
| Column Operations | `columns.md` | `columns.ipynb` | Adding and manipulating columns |
| Filtering Data | `filters.md` | `filters.ipynb` | Boolean indexing and queries |
| Grouping & Aggregation | `groupby.md` | `groupby.ipynb` | GroupBy operations |
| Joining Data | `merge.md` | `merge.ipynb` | Merging DataFrames |
| Calculations | `compute.md` | `compute.ipynb` | Mathematical operations |
| Sorting | `sorting.md` | `sorting.ipynb` | Ordering data |
| Concatenation | `concat.md` | `concat.ipynb` | Combining DataFrames |
| Visualization | `charts.md` | `charts.ipynb` | Creating charts with Altair |
| Export | `export.md` | `export.ipynb` | Saving results |

## Choosing Your Path

### New to Python/pandas?
**Recommended**: Start with the **interactive notebooks** for hands-on learning, then use **markdown chapters** for reference.

### Experienced developer?
**Recommended**: Skim the **markdown chapters** for concepts, then dive into **notebooks** for code examples.

### Teaching/presenting?
**Recommended**: Use **notebooks** for live coding demonstrations, **markdown** for slides and handouts.

### Need quick reference?
**Recommended**: Use **markdown chapters** for fast lookup and searching.

## Technical Notes

- **Notebooks** require VS Code with Python and Jupyter extensions
- **Notebooks** are self-contained with imports and data loading in each file
- **Markdown** chapters assume a continuous session (imports from previous chapters)
- Both formats use the same datasets and produce identical results
- Cross-references link between formats for easy navigation

## Contribution Guidelines

When updating content:

1. **Content changes**: Update both markdown and notebook versions
2. **Code examples**: Test in both formats to ensure compatibility  
3. **New chapters**: Create both `.md` and `.ipynb` versions
4. **Documentation**: Update navigation and cross-references

The dual format approach ensures the tutorial serves both casual readers and hands-on learners effectively.
