import random

bag = list("ABCDEFGHIJ")

def main():
    print("Welcome to the Letter Bag Game!")
    print(f"The bag contains {len(bag)} hidden letters.")

    while bag:
        response = input("\nDo you want to pull a letter out of the bag? (yes/no): ") \
                    .lower().strip()

        if response == "yes":
            pulled_letter = random.choice(bag)
            bag.remove(pulled_letter)

            print(f"\nYou pulled out a letter: {pulled_letter}")
            print(f"Letters remaining in the bag: {len(bag)}")

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