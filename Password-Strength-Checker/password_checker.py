import re
import math

COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678", "12345",
    "qwerty", "abc123", "password1", "admin", "letmein",
    "welcome", "monkey", "iloveyou", "111111", "sunshine"
}

def analyze_password(password):
    score = 0
    suggestions = []
    length = len(password)

    # NEW: check common/breached passwords FIRST — this overrides everything else
    is_common = password.lower() in COMMON_PASSWORDS
    if is_common:
        suggestions.append("This password appears in known breach lists — choose a different one.")

    if length >= 8:
        score += 20
    else:
        suggestions.append("Password should be at least 8 characters long.")
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        suggestions.append("Add at least one uppercase letter.")
    if re.search(r"[a-z]", password):
        score += 15
    else:
        suggestions.append("Add lowercase letters.")
    if re.search(r"\d", password):
        score += 15
    else:
        suggestions.append("Include at least one number.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        suggestions.append("Include at least one special character.")
    if re.search(r"(.)\1{2,}", password):
        suggestions.append("Avoid repeated characters.")
    else:
        score += 10

    # UPDATED: now checks both forward and reversed sequences (e.g. "321", "cba")
    sequences = ["123", "234", "345", "456", "567", "678", "789", "abc", "bcd", "cde"]
    pw_lower = password.lower()
    if any(seq in pw_lower or seq[::-1] in pw_lower for seq in sequences):
        suggestions.append("Avoid sequential characters.")
    else:
        score += 10

    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32
    entropy = length * math.log2(charset) if charset else 0

    # NEW: a common password is capped at "Very Weak" no matter what the score says
    if is_common:
        strength = "Very Weak"
    elif score < 30:
        strength = "Very Weak"
    elif score < 50:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    elif score < 90:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print("\nPassword Analysis")
    print("-----------------------")
    print("Score:", score, "/100")
    print("Strength:", strength)
    print("Entropy:", round(entropy, 2), "bits")
    if suggestions:
        print("\nSuggestions:")
        for item in suggestions:
            print("-", item)
    else:
        print("\nExcellent password!")

password = input("Enter your password: ")
analyze_password(password)
