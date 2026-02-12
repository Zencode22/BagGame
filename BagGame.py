import random

# ----------------------------------------------------------------------
# Initialise the bag with ten distinct letters.
# The actual letters are kept private – they never appear in output.
# ----------------------------------------------------------------------
bag = list("ABCDEFGHIJ")   # You can replace these with any ten characters.

def main():
    print("Welcome to the Letter Bag Game!")
    print(f"The bag contains {len(bag)} hidden letters.")   # No reveal of contents

    while bag:
        # Prompt the player
        response = input("\nDo you want to pull a letter out of the bag? (yes/no): ") \
                    .lower().strip()

        if response == "yes":
            # Randomly draw a letter and remove it from the bag
            pulled_letter = random.choice(bag)
            bag.remove(pulled_letter)

            print(f"\nYou pulled out a letter: {pulled_letter}")
            print(f"Letters remaining in the bag: {len(bag)}")
            # No display of which letters are left

            if not bag:
                print("\nThe bag is now empty. Thanks for playing!")
                break

        elif response == "no":
            print("\nThank you for playing! Goodbye.")
            break

        else:
            print("\nInvalid input – please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()