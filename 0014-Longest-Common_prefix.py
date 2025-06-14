#https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Catatan: Menambahkan pengaman untuk list kosong
        if not strs:
            return ""

        kata_acuan = strs[0]

        # Iterasi melalui setiap indeks dan karakter dari kata acuan.
        for i, karakter in enumerate(kata_acuan):
            # Iterasi melalui sisa kata di dalam list (termasuk kata acuan itu sendiri, tidak masalah)
            for kata_lain in strs: # Loop ini bisa dimulai dari awal
                if i >= len(kata_lain) or kata_lain[i] != karakter:
                    # PERBAIKAN: Gunakan [:i] untuk mengambil awalan (prefix).
                    return kata_acuan[:i]
        
        # Jika loop selesai, berarti seluruh kata acuan adalah prefixnya.
        return kata_acuan
