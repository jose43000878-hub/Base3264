#!/usr/bin/env python3
"""
Security Tool: Base32/Base64 Encoder/Decoder
A CLI tool for encoding and decoding data using Base32 and Base64 algorithms.
"""

import base64
import sys


def encode_base32(data: str) -> str:
    """
    Encode a string using Base32 encoding.
    
    Args:
        data: The string to encode
        
    Returns:
        Base32 encoded string
    """
    # Convert string to bytes and encode using Base32
    encoded_bytes = base64.b32encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')


def decode_base32(data: str) -> str:
    """
    Decode a Base32 encoded string.
    
    Args:
        data: The Base32 encoded string to decode
        
    Returns:
        Decoded string
        
    Raises:
        ValueError: If the input is not valid Base32
    """
    # Strip whitespace to handle formatted input
    cleaned_data = data.strip().upper()
    
    # Add padding if necessary (Base32 requires padding to be multiple of 8)
    padding_needed = len(cleaned_data) % 8
    if padding_needed:
        cleaned_data += '=' * (8 - padding_needed)
    
    # Decode the Base32 string
    decoded_bytes = base64.b32decode(cleaned_data)
    return decoded_bytes.decode('utf-8')


def encode_base64(data: str) -> str:
    """
    Encode a string using Base64 encoding.
    
    Args:
        data: The string to encode
        
    Returns:
        Base64 encoded string
    """
    # Convert string to bytes and encode using Base64
    encoded_bytes = base64.b64encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')


def decode_base64(data: str) -> str:
    """
    Decode a Base64 encoded string.
    
    Args:
        data: The Base64 encoded string to decode
        
    Returns:
        Decoded string
        
    Raises:
        ValueError: If the input is not valid Base64
    """
    # Strip whitespace to handle formatted input
    cleaned_data = data.strip()
    
    # Add padding if necessary (Base64 requires padding to be multiple of 4)
    padding_needed = len(cleaned_data) % 4
    if padding_needed:
        cleaned_data += '=' * (4 - padding_needed)
    
    # Decode the Base64 string
    decoded_bytes = base64.b64decode(cleaned_data)
    return decoded_bytes.decode('utf-8')


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("     BASE32/BASE64 ENCODER/DECODER TOOL")
    print("="*50)
    print("  1. Encode Base32")
    print("  2. Decode Base32")
    print("  3. Encode Base64")
    print("  4. Decode Base64")
    print("  5. Exit")
    print("="*50)


def get_user_input(prompt: str) -> str:
    """
    Get input from the user with a formatted prompt.
    
    Args:
        prompt: The prompt message to display
        
    Returns:
        User's input string
    """
    print(f"\n{prompt}")
    return input(">>> ").strip()


def display_result(operation: str, result: str):
    """
    Display the operation result in a formatted way.
    
    Args:
        operation: The operation that was performed
        result: The result to display
    """
    print("\n" + "-"*50)
    print(f"  {operation} Result:")
    print("-"*50)
    print(f"  {result}")
    print("-"*50)


def handle_encode_base32():
    """Handle the Base32 encoding operation."""
    try:
        # Get input from user
        data = get_user_input("Enter text to encode with Base32:")
        
        if not data:
            print("\n[!] Error: Input cannot be empty.")
            return
        
        # Perform encoding
        result = encode_base32(data)
        display_result("Base32 Encode", result)
        
    except UnicodeEncodeError:
        print("\n[!] Error: Input contains characters that cannot be encoded.")
    except Exception as e:
        print(f"\n[!] Unexpected error during Base32 encoding: {e}")


def handle_decode_base32():
    """Handle the Base32 decoding operation."""
    try:
        # Get input from user
        data = get_user_input("Enter Base32 encoded text to decode:")
        
        if not data:
            print("\n[!] Error: Input cannot be empty.")
            return
        
        # Perform decoding
        result = decode_base32(data)
        display_result("Base32 Decode", result)
        
    except base64.binascii.Error as e:
        print(f"\n[!] Error: Invalid Base32 input - {e}")
        print("    Make sure the input is valid Base32 encoded text.")
    except UnicodeDecodeError:
        print("\n[!] Error: Decoded data contains non-UTF-8 characters.")
        print("    The input may not be valid Base32 encoded UTF-8 text.")
    except ValueError as e:
        print(f"\n[!] Error: {e}")
    except Exception as e:
        print(f"\n[!] Unexpected error during Base32 decoding: {e}")


def handle_encode_base64():
    """Handle the Base64 encoding operation."""
    try:
        # Get input from user
        data = get_user_input("Enter text to encode with Base64:")
        
        if not data:
            print("\n[!] Error: Input cannot be empty.")
            return
        
        # Perform encoding
        result = encode_base64(data)
        display_result("Base64 Encode", result)
        
    except UnicodeEncodeError:
        print("\n[!] Error: Input contains characters that cannot be encoded.")
    except Exception as e:
        print(f"\n[!] Unexpected error during Base64 encoding: {e}")


def handle_decode_base64():
    """Handle the Base64 decoding operation."""
    try:
        # Get input from user
        data = get_user_input("Enter Base64 encoded text to decode:")
        
        if not data:
            print("\n[!] Error: Input cannot be empty.")
            return
        
        # Perform decoding
        result = decode_base64(data)
        display_result("Base64 Decode", result)
        
    except base64.binascii.Error as e:
        print(f"\n[!] Error: Invalid Base64 input - {e}")
        print("    Make sure the input is valid Base64 encoded text.")
    except UnicodeDecodeError:
        print("\n[!] Error: Decoded data contains non-UTF-8 characters.")
        print("    The input may not be valid Base64 encoded UTF-8 text.")
    except Exception as e:
        print(f"\n[!] Unexpected error during Base64 decoding: {e}")


def main():
    """Main function to run the CLI tool."""
    print("\n[*] Security Tool: Base32/Base64 Encoder/Decoder")
    print("[*] Type your choice and press Enter to continue.")
    
    # Main loop - continues until user chooses to exit
    while True:
        try:
            # Display menu and get user choice
            display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            # Process user's menu selection
            if choice == '1':
                handle_encode_base32()
            elif choice == '2':
                handle_decode_base32()
            elif choice == '3':
                handle_encode_base64()
            elif choice == '4':
                handle_decode_base64()
            elif choice == '5':
                # Exit the program
                print("\n[*] Thank you for using the Encoder/Decoder Tool. Goodbye!")
                sys.exit(0)
            else:
                # Invalid menu option
                print("\n[!] Invalid choice. Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n[*] Interrupted by user. Exiting...")
            sys.exit(0)
        except EOFError:
            # Handle EOF (e.g., piped input exhausted)
            print("\n[*] End of input reached. Exiting...")
            sys.exit(0)


if __name__ == "__main__":
    main()
