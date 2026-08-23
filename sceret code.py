while True:
    print("\n--- Secret Code Menu ---")
    choice = input("Type 'code' to encrypt, 'decode' to decrypt, or 'quit' to exit: ")

    if choice == "quit":
        print("Exiting program. Goodbye!")
        break

    elif choice == "code" or choice == "encrypt":
        word = input("Enter a word to encrypt: ")
        
        if len(word) >= 3:
            
            secret_code = "abc" + word[1:] + word[0] + "xyz"
            print(f"Encrypted message: {secret_code}")
        else:
           
            secret_code = word[::-1]
            print(f"Encrypted message: {secret_code}")

    elif choice == "decode":
        word = input("Enter your secret code to decrypt: ")
        
        if len(word) >= 3:
           
            stripped = word[3:-3]
            
            original_word = stripped[-1] + stripped[:-1]
            print(f"Decrypted message: {original_word}")
        else:
           
            original_word = word[::-1]
            print(f"Decrypted message: {original_word}")

    else:
        print("Invalid choice! Try again.")