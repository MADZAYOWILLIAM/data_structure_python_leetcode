class GCDString:
    """
    GCDString class for finding the greatest common divisor (GCD) of two strings.
    A GCD string is defined as a string that divides both input strings evenly,
    meaning both strings can be formed by concatenating the GCD string multiple times.
    """

    def gcd(a, b):
        """
        Calculate the greatest common divisor of two integers using Euclidean algorithm.
        Args:
            a (int): First integer.
            b (int): Second integer.
        Returns:
            int: The greatest common divisor of a and b.
        """
        while b:
            a, b = b, a % b
        return a

    def gcd_of_strings(self, str1: str, str2: str):
        """
        Find the greatest common divisor string of two input strings.
        A GCD string must divide both input strings evenly. If no such string exists,
        an empty string is returned.
        Args:
            str1 (str): First input string.
            str2 (str): Second input string.
        Returns:
            str: The GCD string if it exists, otherwise an empty string.
        Example:
            >>> gcd = GCDString()
            >>> gcd.gcd_of_strings("ABCABC", "ABC")
            'ABC'
            >>> gcd.gcd_of_strings("ABABAB", "ABAB")
            'AB'
        """

        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = GCDString.gcd(len(str1), len(str2))
        return str1[:gcd_length]


# Example usage:gcd_string_finder = GCDString()
GCDString().gcd_of_strings("ABABAB", "ABAB")
# Output: "AB"
