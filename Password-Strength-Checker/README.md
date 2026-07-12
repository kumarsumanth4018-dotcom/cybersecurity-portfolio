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
Password-Strength-Checker/
├── password_checker.py
└── README.md

## ▶️ Usage

```bash
python password_checker.py
```

Example output:

```
Enter your password: Summer123!

Password Analysis
-----------------------
Score: 90 /100
Strength: Very Strong
Entropy: 72.34 bits

Excellent password!
```

## 🎯 Scoring Breakdown

| Check                        | Points |
|-------------------------------|--------|
| Length ≥ 8 characters          | 20     |
| Contains uppercase letter      | 15     |
| Contains lowercase letter      | 15     |
| Contains digit                 | 15     |
| Contains special character     | 15     |
| No repeated characters         | 10     |
| No sequential patterns         | 10     |

*Note: Passwords found in the breach list are automatically rated "Very Weak" regardless of score.*

## 🎯 Learning Outcomes

This project strengthened my understanding of:
- Regex-based pattern validation
- Entropy and information theory as applied to password security
- Practical credential security best practices
- Building rule-based scoring/decision systems in Python

## 🔮 Future Improvements

- Load a larger, external breach-password dataset (e.g. Have I Been Pwned API)
- Add a GUI or web interface
- Support batch password auditing from a file

## 📄 License

This project is open-source and available for educational use.
