def validate_personnumber(pnr: str):
    """
    Validate given person number
    :param pnr: Person number, 10 or 12 digits. Required format: YYMMDD-XXXX or YYYYMMDD-XXXX
    """

    # Remove - from the string
    pnr_clean = pnr.replace('-', '')

    # If wrong input length - always return false
    if (len(pnr_clean) != 10) and (len(pnr_clean) != 12):
        return False

    # If year has four digits, remove the first two
    if len(pnr_clean) == 12:
        pnr_clean = pnr_clean[2:]

    pnr_sum = 0
    mul_two_flag = True  # Indicates if number should be multiplied with two

    for digit in pnr_clean:
        d = int(digit)  # Convert to string digit to integer

        # Every other digit should be multiplied with two
        if mul_two_flag:
            d *= 2

        mul_two_flag = not mul_two_flag  # Invert mul check for next iteration

        # If number is 10 or larger, split into two digits and add separately
        # E.g. if d is 15: Replace with d = 1 + 5 ( = 15 - 9 = 6 )
        if d >= 10:
            d -= 9

        pnr_sum += d

    # Is the sum evenly divisible with 10?
    return pnr_sum % 10 == 0


if __name__ == '__main__':
    print('###  Swedish person number validator  ###')
    print('Enter number (YYMMDD-XXXX or YYYYMMDD-XXXX)')
    number = input('> ')

    try:
        print("Valid?", validate_personnumber(number))
    except ValueError as e:
        print("Invalid text entry")
        print(e)
