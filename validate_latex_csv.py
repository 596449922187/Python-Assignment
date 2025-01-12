import csv
import re

# File paths
input_file_path = "C:\Users\Pradn\Downloads"
output_file_path = "output_content.csv"

# Function to validate LaTeX expressions
def validate_latex(expression):
    # Check for balanced braces and brackets
    stack = []
    for char in expression:
        if char in "{[":
            stack.append(char)
        elif char in "}]":
            if not stack:
                return False
            top = stack.pop()
            if (char == "}" and top != "{") or (char == "]" and top != "["):
                return False

    if stack:  # Unbalanced braces/brackets
        return False

    # Ensure valid LaTeX delimiters (e.g., $...$, \(...\), \[...\])
    if expression.startswith("$") and expression.endswith("$"):
        return expression.count("$") % 2 == 0
    elif expression.startswith("\\(") and expression.endswith("\\)"):
        return True
    elif expression.startswith("\\[") and expression.endswith("\\]"):
        return True
    else:
        return False

# Function to process CSV and detect invalid LaTeX expressions
def process_csv(input_path, output_path):
    # Read input CSV
    with open(input_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    # Add a new column for invalid LaTeX expressions
    for row in rows:
        invalid_expressions = []
        for field in ['main_body', 'did_you_know', 'common_mistakes', 'tips', 'faq']:
            if field in row and row[field]:
                # Extract potential LaTeX expressions using regex
                matches = re.findall(r"(\$.*?\$|\\\(.*?\\\)|\\\[.*?\\\])", row[field])
                for match in matches:
                    if not validate_latex(match):
                        invalid_expressions.append(match)

        # Add invalid expressions to the new column
        row['latex_error_lines'] = "###".join(invalid_expressions) if invalid_expressions else ""

    # Write output CSV
    with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
        fieldnames = reader.fieldnames + ['latex_error_lines']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Execute processing
process_csv(input_file_path, output_file_path)
