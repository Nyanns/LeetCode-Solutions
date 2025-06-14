#https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Langkah 1: Siapkan stack (tumpukan) untuk menyimpan kurung buka.
        stack = []

        # Siapkan dictionary untuk memetakan kurung tutup ke kurung buka pasangannya.
        pasangan_kurung = {')': '(', ']': '[', '}': '{'}

        # Langkah 2: Iterasi melalui setiap karakter dalam string input.
        for karakter in s:

            # Jika karakter adalah KURUNG TUTUP (yaitu, ada sebagai kunci di dictionary)...
            if karakter in pasangan_kurung:
                
                # Ambil elemen teratas dari stack jika tidak kosong. 
                # Jika kosong, gunakan karakter dummy '#' agar perbandingan nanti gagal.
                elemen_teratas = stack.pop() if stack else '#' 

                # Bandingkan elemen dari stack dengan pasangan yang seharusnya.
                # Jika tidak cocok, string tidak valid.
                if pasangan_kurung[karakter] != elemen_teratas:
                    return False
            
            # Jika karakter adalah KURUNG BUKA...
            else:
                # Masukkan (append/push) kurung buka ini ke dalam stack.
                stack.append(karakter)

        # Langkah 3: Pengecekan Final.
        # String hanya valid jika stack kosong di akhir (semua kurung buka punya pasangan).
        return not stack