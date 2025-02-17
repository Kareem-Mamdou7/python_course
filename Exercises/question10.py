import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Ensure at least one character from each required set
password = (
    random.choice(lower)
    + random.choice(upper)
    + random.choice(digits)
    + random.choice(special)
)

# Fill the rest with random characters from all sets
all_chars = lower + upper + digits + special
password += "".join(random.choices(all_chars, k=6))  # At least 10 characters total

# Shuffle the password to avoid predictable patterns
password = "".join(random.sample(password, len(password)))

# Print the final password
print(password)
