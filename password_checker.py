import string
import pyautogui

# check if password is in the common passwords list
def check_common_password(password):
    with open('10k-most-common-passwords.txt', 'r') as file:
        common_passwords = file.read().splitlines()
    if password in common_passwords:
        return False
    return True

# calculate password score based on length and character variety
def password_score(password):
    score = 0;

    if len(password) > 8:
        score += 1
    if len(password) > 12:
        score += 1
    if len(password) > 16:
        score += 1
    if len(password) > 20:
        score += 1
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digits = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)
    
    character_types = [uppercase, lowercase, digits, special]

    for bool in character_types:
        if bool:
            score += 1
    
    return score, character_types

# provide feedback based on password score
def is_password_strong(password):
    if not check_common_password(password):
        return 'Password is too common. Score: 0/7'
    
    feedback = ''
    score, weaknesses = password_score(password)
    strength = 0

    if score >= 6:
        strength = 'Very Strong'
    elif score == 5:
        strength = 'Strong'
    elif score == 4:
        strength = 'Moderate'
    elif score == 3:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    feedback = f"Your password is {strength} (Score: {score}/7)\n"

    if score <= 3:
        feedback += "Suggestions to improve your password:\n"
        if not weaknesses[0]:
            feedback += "- Add uppercase letters\n"
        if not weaknesses[1]:
            feedback += "- Add lowercase letters\n"
        if not weaknesses[2]:
            feedback += "- Add digits\n"
        if not weaknesses[3]:
            feedback += "- Add special characters\n"
        if len(password) <= 8:
            feedback += "- Increase the length of your password\n"

    return feedback

# Main execution
paswrd = pyautogui.password(text='Enter your password to check strength:', title='Password Strength Checker', default='', mask='*')
print(is_password_strong(paswrd))