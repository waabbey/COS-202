# Mathematical Calculator (MC)

A simple yet functional graphical calculator built with Python's Tkinter library. This application provides a user-friendly interface for performing basic mathematical operations.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Advanced Operations**:
  - Exponentiation (^)
  - Integer division (\)
  - Modulo (%)
  - Decimal point support
- **User-Friendly GUI**: Clean interface with buttons for all operations
- **Error Handling**: Gracefully handles calculation errors
- **Clear Function**: Reset the calculator to start fresh
- **Exit Button**: Close the application with the OFF button

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/waabbey/COS-202.git
   cd COS-202
   ```

2. Ensure Python and Tkinter are installed on your system.

3. Run the calculator:
   ```bash
   python calculator.py
   ```

## Usage

### Interface Overview

The calculator window displays:
- **Entry Box**: Shows the current expression and results at the top
- **Number Buttons**: 0-9 for entering numbers
- **Operation Buttons**: Standard arithmetic operators (+, -, *, /)
- **Special Buttons**:
  - **^**: Exponentiation (power) operation
  - **%**: Modulo (remainder) operation
  - **\\**: Integer division operation
  - **.**: Decimal point for floating-point numbers
  - **=**: Calculate the result
  - **C**: Clear the display and reset
  - **OFF**: Close the application (red button)

### How to Use

1. **Enter an Expression**: Click number and operator buttons in sequence
   - Example: Click 5 → + → 3 → = will display 8

2. **Use Special Operations**:
   - **Power**: 2 → ^ → 3 → = calculates 2³ (result: 8)
   - **Integer Division**: 7 → \ → 2 → = calculates 7 // 2 (result: 3)
   - **Modulo**: 7 → % → 2 → = calculates 7 % 2 (result: 1)

3. **Clear**: Press the **C** button to reset the calculator
4. **Exit**: Press the **OFF** button to close the application

## Code Structure

### Global Variables
- `expression`: Stores the current mathematical expression as a string

### Key Functions

#### `press(value)`
- Handles button presses for numbers and operators
- Converts display symbols (^ and \) to Python equivalents (** and //)
- Updates the entry box with the current expression

#### `equal()`
- Evaluates the current expression using Python's `eval()`
- Displays the result or an error message if calculation fails
- Stores the result in `expression` for further calculations

#### `clear()`
- Resets the global expression variable
- Clears the entry box display

#### `off()`
- Destroys the root window and closes the application

### GUI Components
- **Root Window**: 380×500 px, light blue background, non-resizable
- **Entry Box**: Arial font (20pt), right-aligned, with padding
- **Button Layout**: 6 rows organized in a grid pattern with expandable frames

## Display Conversion

The calculator uses symbol conversion for user-friendly display:
- **^** (displayed) ↔ `**` (Python exponentiation)
- **\\** (displayed) ↔ `//` (Python integer division)

This allows users to see intuitive mathematical symbols while using Python's operators internally.

## Error Handling

If an invalid expression is entered:
- The calculator displays **"Error"** in the entry box
- The expression is reset to empty
- The calculator is ready for a new calculation

## Example Calculations

| Expression | Result | Steps |
|-----------|--------|-------|
| 5 + 3 | 8 | 5 → + → 3 → = |
| 10 / 2 | 5.0 | 10 → / → 2 → = |
| 2 ^ 3 | 8 | 2 → ^ → 3 → = |
| 7 \ 2 | 3 | 7 → \ → 2 → = |
| 10 % 3 | 1 | 10 → % → 3 → = |
| 3.5 + 2.1 | 5.6 | 3 → . → 5 → + → 2 → . → 1 → = |

## Limitations

- **Single Expression Only**: Cannot store previous calculations
- **No Parentheses Support**: Complex expressions with order of operations must be calculated in sequence
- **Limited to Python's eval()**: Subject to Python's mathematical evaluation rules
- **No Keyboard Support**: Must use mouse to click buttons

## Future Enhancements

Potential improvements for future versions:
- Add keyboard input support
- Implement parentheses for complex expressions
- Add operation history/memory functions
- Create undo/backspace functionality
- Add more advanced mathematical functions (sin, cos, log, etc.)
- Support for negative numbers handling

## License

This project is part of the COS-202 coursework.

## Author

Created by: waabbey

## Support

For issues, suggestions, or questions, please open an issue in the repository.
