# Prompt: Write a program that generates a random password for the user
import os
print("Your new password is: " + str(os.urandom(4)))

"""
Things I learned from this project:
- No need to build your own crazy complex random string generator when there's already
one built in. Just saves time.
- Casting data types to string via str()
- built-in 'os' library exists
"""