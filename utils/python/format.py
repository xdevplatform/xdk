import ast
import os
import sys

def get_definitions_to_format(code):
    """
    Parse the code and return a list of (start_line, end_line) tuples for all
    function definitions (including methods within classes).
    
    Args:
        code (str): The source code as a string.
    
    Returns:
        list[tuple[int, int]]: Sorted list of (start, end) line numbers for definitions.
    """
    tree = ast.parse(code)
    defs = []
    for node in ast.walk(tree): # Use ast.walk to find all function definitions
        if isinstance(node, ast.FunctionDef):
            start = node.lineno
            # Ensure end_lineno is captured correctly, may need adjustment for decorators
            # Finding the true end might require iterating through node attributes or using get_source_segment
            # For now, rely on ast's end_lineno which is usually sufficient
            end = getattr(node, 'end_lineno', None)
            if end is not None:
                defs.append((start, end))
    
    # Sort definitions by starting line number
    defs.sort()
    return defs

def reduce_blank_lines(lines):
    """
    Reduce multiple consecutive blank lines to a single blank line, preserving leading whitespace.
    
    Args:
        lines (list[str]): List of lines from the file, with trailing whitespace already removed.
    
    Returns:
        list[str]: Processed lines with consecutive blanks reduced to one.
    """
    result = []
    for line in lines:
        is_blank = line.strip() == ''
        if not is_blank:
            result.append(line)
    return result

def remove_trailing_blanks(lines):
    """
    Remove trailing blank lines from a list of lines.
    
    Args:
        lines (list[str]): List of lines.
    
    Returns:
        list[str]: Lines with trailing blanks removed.
    """
    while lines and lines[-1].strip() == '':
        lines.pop()
    return lines

def format_file(file_path):
    """
    Format a single Python file by adjusting blank lines and removing trailing whitespace.
    
    Args:
        file_path (str): Path to the Python file to format.
    """
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Parse the code to find all function/method definitions
    code = ''.join(lines)
    try:
        defs = get_definitions_to_format(code) # Use the new function
    except SyntaxError:
        print(f"Syntax error in {file_path}, skipping")
        return
    
    new_lines = []
    
    if defs:
        # Process the segment before the first definition
        before_lines = lines[:defs[0][0] - 1]  # 0-based indexing
        before_lines = remove_trailing_blanks([line.rstrip() for line in before_lines])
        if before_lines:  # Only add blank lines if there's code before
            new_lines.extend(before_lines)
            new_lines.extend(['', ''])
        
        # Process each definition and the segments between them
        for i in range(len(defs)):
            start, end = defs[i]
            def_lines = lines[start - 1:end]  # Adjust for 0-based indexing
            def_lines = reduce_blank_lines([line.rstrip() for line in def_lines])
            new_lines.extend(def_lines)
            
            if i < len(defs) - 1:
                # Process the segment between this definition and the next
                next_start = defs[i + 1][0]
                between_lines = lines[end:next_start - 1]
                between_lines = remove_trailing_blanks([line.rstrip() for line in between_lines])
                if between_lines:
                    new_lines.extend(between_lines)
                new_lines.extend(['', ''])  # Two blank lines before next definition
        
        # Process the segment after the last definition
        after_lines = lines[defs[-1][1]:]
        after_lines = remove_trailing_blanks([line.rstrip() for line in after_lines])
        if after_lines:
            new_lines.extend(after_lines)
    else:
        # No top-level definitions; just clean up the lines
        new_lines = remove_trailing_blanks([line.rstrip() for line in lines])
    
    # Write the formatted lines back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in new_lines:
            f.write(line + '\n')

def format_directory(directory):
    """
    Format all Python files in the given directory and its subdirectories.
    
    Args:
        directory (str): Path to the directory to process.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Formatting {file_path}")
                format_file(file_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python format.py <file_or_directory>")
        sys.exit(1)
    path_arg = sys.argv[1]
    if os.path.isfile(path_arg):
        if path_arg.endswith('.py'):
            print(f"Formatting {path_arg}")
            format_file(path_arg)
        else:
            print(f"Skipping non-Python file: {path_arg}")
    elif os.path.isdir(path_arg):
        format_directory(path_arg)
    else:
        print(f"Error: '{path_arg}' is not a valid file or directory")
        sys.exit(1)
    print("Formatting complete")