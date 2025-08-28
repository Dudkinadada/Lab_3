# Scientific Calculator

A simple scientific calculator with a graphical user interface, developed in Python using the Tkinter library.

## Features

### Basic Arithmetic Operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

### Scientific Functions:
- Square root (√)
- Trigonometric functions: sin, cos, tan (in degrees)
- Logarithmic functions: log (base 10), ln (natural log)
- Mathematical constant: π (pi)

## Requirements

- Python 3.x
- Tkinter (usually included with Python standard library)

## Installation

1. Clone or download this project
2. Ensure Python 3.x is installed on your system
3. No additional dependencies required (uses standard libraries)

## Usage

Run the calculator by executing the Python script:

```bash
python main.py
```

### Interface:
- The input field displays the current expression and results
- Number buttons (0-9) and decimal point for numeric input
- Operator buttons for basic arithmetic
- Function buttons for scientific operations
- 'C' button to clear the input
- '=' button to evaluate the expression

## Example Operations

- Basic: `2 + 3 * 4 = 14`
- Scientific: `sin(30) = 0.5`
- Constants: `pi = 3.141592653589793`
- Functions: `sqrt(16) = 4`

## Error Handling

The calculator includes basic error handling that displays informative messages for:
- Invalid mathematical operations
- Division by zero
- Syntax errors in expressions

## Project Structure

- `main.py` - Main application file
- README.md

## Educational Purpose

This project serves as a learning exercise for:
- GUI development with Tkinter
- Event-driven programming
- Mathematical operations in Python
- Exception handling
- Object-oriented design principles

## Limitations

- Basic error handling (may not catch all edge cases)
- Limited to functions implemented in the standard math module
- Input is evaluated using `eval()` - use with caution in production

