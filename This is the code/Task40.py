# Ask "Are We There Yet?"
# Keep asking the same question until the user enters the word "yes".
# The condition that ends the loop is checked at the END of the loop, so the question is always asked at least once.
# When the loop ends, output "Zzzzzzzzzzzzz!"

while True:
    answer = input("Are We There Yet? ")
    if answer.lower() == "yes":
        break

print("Zzzzzzzzzzzzz!")