# Python-Assignment
# Approach
# 1.Parsing the CSV File

The script reads the input CSV file row by row using Python’s built-in csv module.
It processes five specific fields for LaTeX expressions:

main_body
did_you_know
common_mistakes
tips
faq

# 2.Detecting LaTeX Expressions

LaTeX expressions are identified using regular expressions:

$...$ for inline expressions.
\(...\) for inline expressions.
\[...\] for display expressions.

# 3. Validating LaTeX Syntax

The script ensures the following:

Balanced braces {} and brackets [].
Valid delimiters for inline ($...$, \(...\)) and display (\[...\]) expressions.
Proper matching of opening and closing characters.

# 4. Logging Invalid Expressions

Invalid LaTeX expressions are listed in the latex_error_lines column, separated by ###.

If no invalid expressions are found, the column is left empty.

# 5. Writing the Output File

The processed data is written to a new CSV file, output_content.csv, maintaining all original columns and adding the latex_error_lines column.

## Assumptions and Limitations

# Assumptions

The input file has the expected headers.

All LaTeX expressions are properly delimited using $...$, \(...\), or \[...\].

Empty fields are allowed and do not raise errors.

# Limitations

The script does not validate the semantic correctness of LaTeX expressions (e.g., whether \frac is used with valid arguments).

Only syntax errors (e.g., unmatched braces or improper delimiters) are detected.

The script uses basic regular expressions and does not rely on external LaTeX parsers or validators.

# Instructions to Run the Script
## Prerequisites
Python 3.x installed on your system.
Basic knowledge of the command line.

# Steps

# 1.Save the Script

Save the provided Python code to a file named validate_latex_csv.py.

# 2.Prepare the Input File

Place the input file (content.csv) in the same directory as the script.

# 3.Run the Script

Open a terminal or command prompt.

Navigate to the script’s directory.

Execute the script using the command:

python validate_latex_csv.py

# 4.Check the Output File

After execution, a new file named output_content.csv will be generated in the same directory.

Open this file to review the latex_error_lines column for invalid LaTeX expressions.
