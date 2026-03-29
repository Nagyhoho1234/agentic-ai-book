# Chapter 2: NumPy and Matplotlib

## Summary

This chapter introduces NumPy for numerical computing and Matplotlib for visualization. It covers the Anaconda IDE (Spyder), NumPy arrays and tensors, comprehensive 2D and 3D plotting, LaTeX integration, figure saving at publication quality, and Jupyter notebooks with Markdown. The chapter establishes the foundational tools used throughout the rest of the book.

## Key Concepts

### Anaconda and Spyder IDE
- **Anaconda** is recommended as the primary Python distribution for scientific computing
- **Spyder** IDE provides an Editor Window, Console Window, and Variable Explorer
- Spyder supports interactive plotting and debugging

### NumPy Fundamentals
- NumPy arrays are more efficient than Python lists for numerical computation
- **Tensors** are multi-dimensional arrays: scalar (rank 0), vector (rank 1), matrix (rank 2), 3D tensor (rank 3)
- Key array operations: `np.array()`, `np.arange()`, `np.linspace()`, `np.zeros()`, `np.ones()`
- Array slicing and indexing with `:` notation
- Vectorized operations operate element-wise on arrays
- Universal functions (ufuncs): `np.sin()`, `np.cos()`, `np.exp()`, `np.sqrt()`, etc.

### Matplotlib Plotting
- **2D plots**: `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.pie()`
- **Subplots**: `plt.subplot(rows, cols, index)` for multiple plots in one figure
- **3D plots**: using `mpl_toolkits.mplot3d` with `plot_surface()` and `plot_wireframe()`
- Customization: labels, titles, legends, colors, markers, line styles, font sizes
- LaTeX rendering in labels and titles using `r'$...$'` syntax
- **savefig**: save figures as PNG, PDF, EPS at specified DPI (dots per inch)
- Setting `plt.rcParams["font.size"]` for publication-quality figures

### Jupyter Notebooks
- `.ipynb` files combining code, text, and output in cells
- **Markdown** cells for formatted text with headers, bold, italic, lists, links, images
- Cells can be Code or Markdown type
- Notebooks can be shared and exported to HTML, PDF
- Google Colab provides free cloud-based Jupyter notebooks with GPU/TPU access

### GitHub
- All book programs available on GitHub
- Version control for scientific code

## Code Examples Described
- Creating and manipulating 1D, 2D, and 3D NumPy arrays
- Plotting trigonometric functions with customized axes
- 3D surface plots of mathematical functions
- Animations using matplotlib's FuncAnimation
- Interactive plots with slider widgets
- Saving publication-quality figures at 300 DPI

## Key Definitions
- **Tensor**: a multi-dimensional array; generalization of scalars, vectors, and matrices
- **Vectorization**: applying operations to entire arrays without explicit loops
- **DPI (dots per inch)**: resolution measure for saved figures
- **Markdown**: lightweight markup language for formatted text

## Practical Takeaways
- Always use NumPy arrays instead of Python lists for numerical computation -- they are faster and use less memory
- Use `plt.rcParams["font.size"]` to set consistent font sizes for all plot elements
- Save figures at 300 DPI minimum for publication quality
- LaTeX integration in matplotlib allows proper mathematical notation in figures
- Jupyter notebooks are ideal for reproducible research and sharing results

## Notable References
- Anaconda: https://www.anaconda.com
- NumPy documentation: https://numpy.org
- Matplotlib documentation: https://matplotlib.org
- McKinney, W. (2017). *Python for Data Analysis*, O'Reilly Media
