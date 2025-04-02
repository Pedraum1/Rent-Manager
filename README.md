# Rent Manager

Rent Manager is a Python-based application designed to help property administrators manage rental properties efficiently. It provides features to track overdue rents, view property records, and manage tenant information.

## Features

- **Overdue Rent Tracking**: Identify properties with overdue rents for today or a specific date.
- **Property Records**: View detailed records of all rental properties.
- **Tenant Management**: Manage tenant information associated with properties.
- **Excel Integration**: Read and process rental data from Excel files.

## Requirements

- Python 3.8 or higher
- Required Python libraries:
  - `pandas`
  - `openpyxl`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd RentManager
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your rental data in an Excel file named `Table.xlsx` inside the `Tables` directory.
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to navigate through the application.

## Project Structure

- **Classes**: Contains the core classes for the application, such as `App`, `Excel`, and property models.
- **Functions**: Utility functions for input handling, printing, and table processing.
- **Tables**: Directory for storing Excel files with rental data.
- **main.py**: Entry point for the application.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
