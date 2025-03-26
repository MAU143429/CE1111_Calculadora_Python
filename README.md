# 🧮 FunTras Calculator — CE-1111

## 🧠 Overview

This repository contains the solution for T1 from the course CE1111 – Análisis Numérico para Ingeniería at Instituto Tecnológico de Costa Rica. The project focuses on approximating a wide range of transcendental functions using custom-built numerical methods in Python.

It consists of two main components:

---

## 📐 Part 1: Transcendental Function Implementation

- All functions are implemented in Python using only basic operations:
  - Addition, subtraction, multiplication, and integer exponentiation.
  - No division or built-in transcendental functions are allowed.
- Each function uses iterative methods (e.g., Taylor series, Newton's method) with:
  - A tolerance of `1e-8`
  - A maximum of 2500 iterations
- Domain validation is performed for each function.
- A script (`test_funtras.py`) is included to demonstrate function composition and result accuracy.

---

## 🖥️ Part 2: Graphical FunTras Calculator

- A GUI calculator implemented using `tkinter`.
- Allows users to:
  - Input real values for `x` (and `y` if required)
  - Select a function to approximate
  - View results or receive error messages for invalid inputs
- Includes built-in **help** section and group member information.
- Supports functions like: `sin(x)`, `cos(x)`, `tan(x)`, `ln(x)`, `sinh(x)`, `sqrt(x)`, `x^y`, etc.
- A Windows executable (`.exe`) version was generated for easy testing.

---

## 🔬 Educational Objectives

- Practice numerical analysis techniques
- Gain experience with iterative methods
- Handle domain constraints programmatically
- Build a Python GUI from scratch

