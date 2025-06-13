#https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        str_x = str(x)
        
        kiri = 0
        kanan = len(str_x) - 1 # len() sekarang bisa digunakan pada string

        while kiri < kanan:
            # Jika karakter di kiri tidak sama dengan di kanan, ini bukan palindrom.
            if str_x[kiri] != str_x[kanan]: # Gunakan != dan kurung siku
                return False
            
            # Geser penunjuk
            kiri += 1
            kanan -= 1
        
        # Jika loop selesai tanpa pernah menemukan perbedaan, artinya ini adalah palindrom.
        return True
