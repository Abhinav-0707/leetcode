class Solution(object):
    def divide(self, dividend, divisor):
        # Handle overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Determine the sign of the answer
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Repeatedly subtract the largest possible multiple
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        # Keep result within 32-bit signed integer range
        return max(-2147483648, min(2147483647, quotient))