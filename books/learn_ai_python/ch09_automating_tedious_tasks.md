# Chapter 9: Automating Tedious Tasks

## Summary

Chapter 9 demonstrates one of the most immediately practical applications of AI-assisted programming: automating repetitive, tedious tasks that you would otherwise do by hand. The chapter walks through three complete examples, showing the full workflow from identifying the task to having working code.

### Example 1: Cleaning Up an Email (Clipboard Manipulation)

The first example automates cleaning up email text by removing unwanted formatting. The key insight is using the `pyperclip` module to read from and write to the system clipboard. The workflow:
1. Ask Copilot Chat which Python module can interact with the clipboard
2. Learn about `pyperclip` and install it with `pip install pyperclip`
3. Write a function that reads text from the clipboard, cleans it, and writes the result back
4. The function takes no parameters (it gets its input from the clipboard)

### Example 2: Adding Cover Pages to PDF Files

The second example merges cover pages with report PDF files -- a task that would be extremely tedious to do manually for hundreds of files. This example introduces several important concepts:
- **Choosing the right Python module:** The authors use Copilot Chat to explore options (PyPDF2, ReportLab, FPDF, PDFMiner, PyMuPDF, pdfrw), evaluate their strengths and weaknesses, and select the best one.
- **Handling deprecated APIs:** When PyPDF2 3.0 removed `PdfFileReader` (replacing it with `PdfReader`), Copilot still generated code using the old API because it was trained on older code. The chapter shows three solutions: install an older version, fix the code manually, or switch to a different library (PyMuPDF/fitz).
- **Safety with file operations:** Test on small sample directories first, use `print()` instead of actual file writes to verify behavior, and always keep backups of original files.

### Example 3: Merging Phone Picture Libraries

The third example combines two directories of photos, handling duplicates and filename collisions. This example demonstrates top-down design applied to automation:
- **`make_copies`** (top-level): loops through directories, calls `make_copy` for each file
- **`make_copy`**: checks if a file is a duplicate, copies it if not (handling filename collisions)
- **`get_good_filename`**: generates a unique filename by adding underscores when a file with the same name already exists

Key modules used: `shutil` (for copying files), `filecmp` (for comparing file contents), `os` (for directory listing and path manipulation).

### The Module Selection Workflow (Figure 9.2)

The chapter formalizes a process for choosing Python modules:
1. Ask Copilot or ChatGPT for a list of modules that can help with your task
2. Ask for pros and cons of each
3. Pick one based on the comparison
4. If necessary, install the module
5. Start the function design cycle, including the module name in your initial prompt
6. If stuck, try a different module

## Key Techniques for AI-Assisted Coding

- **Use Copilot Chat to discover modules:** You do not need to know which Python module to use in advance. Ask Copilot, evaluate the options, then proceed.
- **The module selection workflow:** Systematically evaluate candidate modules before committing to one.
- **Handle API deprecation gracefully:** Copilot may generate code using deprecated APIs. Check error messages and either downgrade the library, update the code, or switch libraries.
- **Safety-first file operations:** Always test on sample data first, use `print()` to preview what would happen, and keep backups.
- **Top-down design for automation scripts:** Even automation tasks benefit from decomposition into smaller functions.

## Practical Takeaways for Scientists

- Any task you do repeatedly by hand is a candidate for automation: renaming files, converting formats, merging datasets, generating reports, reformatting data.
- Python has modules for almost everything: clipboard (`pyperclip`), PDFs (`PyPDF2`, `PyMuPDF`), Excel files (`openpyxl`), images (`Pillow`), email, web scraping, and more.
- Always test automation scripts on a small sample first. File operations can be destructive and difficult to undo.
- The `shutil`, `os`, and `filecmp` modules are built into Python and cover most file manipulation needs without installing anything.
- When Copilot generates code using a deprecated API, the error message usually tells you exactly what to use instead.

## Notable References

- `pyperclip` module for clipboard access
- PyPDF2 and PyMuPDF (`fitz`) for PDF manipulation
- `shutil`, `filecmp`, `os` modules for file operations
- `pip install` for installing third-party Python modules
- The module selection workflow (Figure 9.2)
