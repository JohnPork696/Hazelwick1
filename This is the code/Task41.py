# Ask "Are We There Yet?"
# Keep asking the same question until the user enters the word "yes".
# This is a post-condition loop, so the condition is checked at the END of the loop.
# When the loop ends, output "Zzzzzzzzzzzzz!"

while True:
    answer = input("Are We There Yet? ")
    if answer.lower() == "yes":
        break

print("Zzzzzzzzzzzzz!")