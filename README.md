# Calculation Hub

A modular Python-based calculator application designed to serve as an all-in-one calculation platform while documenting my Python learning journey.

This project is being developed incrementally, following real-world software development practices. Rather than building everything in a single file, the application is organized into modules, making it easier to maintain, test, and extend.

---

## Project Goals

The primary goal of this project is to strengthen my Python fundamentals by implementing a variety of practical calculators and utilities while learning professional software development practices.

Through this project, I aim to gain hands-on experience with:

* Functions
* Modular Programming
* Object-Oriented Programming (OOP)
* File Handling
* JSON Processing
* API Integration
* Database Management
* Testing
* Error Handling
* Git & GitHub Workflow
* Software Architecture

---

## Current Features

### Basic Calculator

* Addition (supports multiple numbers)
* Subtraction (supports multiple numbers)
* Multiplication (supports multiple numbers)
* Division (supports multiple numbers)
* Modulus
* Power

### History Management

* Save calculations during runtime
* View calculation history
* Clear history

### Input Validation

* Numeric input validation
* Positive integer validation
* Prevention of common user input errors

### Automated Testing

* Unit tests for calculator operations
* Verification of expected outputs

---

## Planned Features

### Scientific Calculator

* Square Root
* Factorial
* Logarithms
* Trigonometric Functions
* Exponents

### GPA & CGPA Calculator

* Custom GPA Calculation
* University-Specific GPA Systems
* Semester-wise CGPA Calculation

### Area & Perimeter Calculator

* Circle
* Rectangle
* Square
* Triangle

### BMI Calculator

* BMI Calculation
* Health Category Classification

### Percentage Calculator

* Marks Percentage
* Percentage Increase
* Percentage Decrease

### Age Calculator

* Current Age
* Age in Days
* Age in Months

### Unit Converter

* Length Conversion
* Weight Conversion
* Temperature Conversion
* Time Conversion

### Currency Converter

* Live Exchange Rates
* Multiple Currency Support
* API Integration

### Database Integration

* SQLite Database
* Persistent Calculation History
* User Profiles

### GUI Version

* Tkinter-Based Desktop Application
* Improved User Experience

### Advanced Features

* Object-Oriented Refactoring
* JSON Configuration Files
* Logging System
* Export History
* Settings Management

---

## Project Structure

```text
CalculationHub/
│
├── main.py
│
├── calculators/
│   ├── __init__.py
│   └── basic.py
│
├── utils/
│   ├── __init__.py
│   ├── history.py
│   └── validator.py
│
├── tests/
│   └── test_basic.py
│
└── data/
    └── history.txt
```

As the project evolves, additional modules and folders will be added.

---

## Technologies Used

### Programming Language

* Python 3

### Development Concepts

* Modular Programming
* Functional Programming
* Software Testing
* Error Handling

### Future Technologies

* SQLite
* JSON
* Requests API
* Tkinter
* Pytest

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Move into Project Directory

```bash
cd CalculationHub
```

### Run the Application

```bash
python main.py
```

---

## Running Tests

Execute the following command from the project root directory:

```bash
pytest
```

Or:

```bash
python -m pytest
```

---

## Sample Usage

### Addition

```text
How many numbers do you want to enter? 5

Enter Number 1: 10
Enter Number 2: 20
Enter Number 3: 30
Enter Number 4: 40
Enter Number 5: 50

Result: 150
```

### Multiplication

```text
How many numbers do you want to enter? 4

Enter Number 1: 2
Enter Number 2: 3
Enter Number 3: 4
Enter Number 4: 5

Result: 120
```

---

## Learning Journey

This repository is not only a calculator project but also a documented learning journey.

The project will evolve through multiple phases:

### Phase 1

* Modular Basic Calculator
* Input Validation
* History System
* Unit Testing

### Phase 2

* Scientific Calculator
* GPA Calculator
* CGPA Calculator

### Phase 3

* Area, Percentage, BMI, and Age Calculators

### Phase 4

* File Handling
* JSON Storage

### Phase 5

* Currency Conversion API

### Phase 6

* SQLite Database Integration

### Phase 7

* Object-Oriented Refactoring

### Phase 8

* Tkinter Desktop Application

---

## Future Enhancements

* User Authentication
* Cloud Synchronization
* Calculation Export
* Dark Mode GUI
* Multi-language Support
* Plugin-Based Calculator Architecture

---

## Author

Malik Muhammad Sanaullah

Computer Science Student

This project is being developed as part of my Python learning journey and software development portfolio.
