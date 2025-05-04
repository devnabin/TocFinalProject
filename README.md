# PDA-Based HTML/XML Validator

This is a Python project that validates whether a markup file like HTML or XML document is well-formed or structured using the logic of a Pushdown Automaton (PDA). It simulates stack operations to track opening and closing tags.This system provides detailed feedback about mismatches, missing tags, and invalid content, if any.

## Course Context

This project is design and developed for the Theory of Computation (CSC720) class as the final semester project. It demonstrates the application of context-free grammar recognition and PDA logic in real-world syntax validation system.


## Features

- PDA simulation using a stack
- Validates proper tag nesting
- Validates proper tag matching
- Detects malformed tags and invalid symbols
- Handles self-closing HTML tags like `<img />` or `<br />` etc.
- Accepts raw HTML/XML
- Accepts file input for validation
- Detailed error diagnostics
- Case-sensitive tag comparison
---

## How It Works

1. User can give inputs either:
   - By a raw HTML/XML string
   - By a filename using `validate <filename>`
2. The code extracts tags using regular expressions.
3. Tags are classified as:
   - Opening (`<div>`)
   - Closing (`</div>`)
   - Self-closing (`<img />`)
4. A stack is used to simulate PDA behavior:
   - Opening tags are pushed
   - Matching closing tags are popped
5. If all tags match and the stack is empty, then maching prove structure is valid. else it display error as a message.

---

## Usage

### Run the program

```bash
python validator.py
```

### Available commands

- `validate <filename>` => It Validate HTML/XML in a file  
- `read <filename>`  => It display file contents  
- Paste raw HTML/XML  => Validate input instantly  
- `exit`  => Exit the program

---

## Sample Test Cases

| Input                          | Result        |
|-------------------------------|---------------|
| `<div><p>Hello</p></div>`     | Valid       |
| `<div><p></div></p>`          | Invalid     |
| `<img src="x.jpg" />`         | Valid       |
| `?`                           | Invalid       |
| `<div .`                      | Invalid       |
| `<div><span>`                 | Unclosed tag -> Invalid|
| `</img>`                      | Not allowed  -> Invalid |

---

## File Structure

```
validator.py       # Main Python script
index.html
note.xml
README.md        
/Report/Presentation.ppt
/Report/Report.pdf
```

---

## Requirements

- Python 3.x
- No external dependencies (uses only `re` and `os`)
- No any third party libraries
---

## License

This project is for educational use under the CSC720 course. Reuse is permitted for learning and teaching purposes with attribution.
---

## Project Lik
https://github.com/devnabin/TocFinalProject

## Author

- **Nabin Bhandari**  
  Graduate Student, MS Computer Science <br>
  Dakota State University <br>
  nabin.bhandari@trojans.dsu.edu <br>
  Student ID: 101213073 


  
