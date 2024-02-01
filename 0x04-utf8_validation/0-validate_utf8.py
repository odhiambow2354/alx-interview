#!/usr/bin/python3
"""UTF-8 Validation"""


def get_leading_set_bits(num):
    """Returns the number of leading set bits (1)"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    bits_count = 0
    
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[i])
            # 1-byte (format: 0xxxxxxx)
            if bits_count == 0:
                continue
            # A character in UTF-8 can be 1 to 4 bytes long
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            # Checks if current byte has format 10xxxxxx
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
        
    return bits_count == 0

# Test cases
if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
