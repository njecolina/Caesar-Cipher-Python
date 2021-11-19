alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo + "\nVersion 0.0.1 by Sonja Hranjec - 2021. - github.com/njecolina")

shouldend = False
while not shouldend:
  direction = input("\nPlease type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Please type your message:\n").lower()
  shift = int(input("Please type the shift number:\n"))

  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("\nPlease type 'yes' if you want to try again, or just type 'no' for otherwise.\n")
  if restart == "no":
    shouldend = True
    print("Thank you for using this program and goodbye! xoxo")
