# 🔐 Password Strength Analyzer

A Python tool that analyzes password strength using entropy calculation, common-password detection, and multiple character-composition checks — then gives actionable feedback to improve weak passwords.

## 📌 Overview

Most password strength checkers only look at length and character variety. This tool goes further by cross-checking against a known breached-password list, detecting sequential and repeated-character patterns, and calculating Shannon entropy to give a more realistic measure of password strength.

## ✨ Features

- **Breach-list check** — flags passwords found in common/leaked password lists (auto-capped at "Very Weak")
- **Length check** — rewards passwords of 8+ characters
- **Character composition** — checks for uppercase, lowercase, digits, and special characters
- **Repeated character detection** — flags patterns like `aaa` or `111`
- **Sequential pattern detection** — flags both forward and reversed sequences (`123`, `321`, `abc`, `cba`, etc.)
- **Entropy calculation** — estimates password strength in bits based on character set size and length
- **Weighted scoring system** — combines all checks into a 0–100 score
- **Strength rating** — Very Weak / Weak / Medium / Strong / Very Strong
- **Actionable suggestions** — specific tips printed for every failed check

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `re` (pattern matching), `math` (entropy calculation)

## 🚀 How It Works

1. User enters a password via terminal input
2. Password is checked against a breach list of common passwords
3. Script evaluates length, character variety, repeated characters, and sequential patterns
4. Each check contributes weighted points to a 0–100 score
5. Shannon entropy is calculated based on the estimated character set size
6. A final strength rating and tailored suggestions are printed

## 📂 Project Structure
