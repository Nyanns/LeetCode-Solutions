#https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Langkah 1: Buat "Kamus" Angka Romawi
        nilai_romawi = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        #Langkah 2: Strategi Iterasi (Looping)
        total = 0
        for i in range(len(s) - 1):
            nilai_sekarang = nilai_romawi[s[i]]
            nilai_berikutnya = nilai_romawi[s[i+1]]
            if nilai_sekarang < nilai_berikutnya:
                total = total - nilai_sekarang
            else:
                total = total + nilai_sekarang
        
        #Langkah 3: Menangani Karakter Terakhir
        total += nilai_romawi[s[-1]]

        # Kembalikan hasil akhir
        return total
