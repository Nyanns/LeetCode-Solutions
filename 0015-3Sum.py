#https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        clean = nums.sort()
        hasil = []

        # Langkah 3: Loop utama untuk mengunci satu angka
        for i, angka_kunci in enumerate(nums):

            # Petunjuk #1: Lompat jika angka kuncinya sama dengan sebelumnya
            if i > 0 and angka_kunci == nums[i-1]:
                continue

            # Petunjuk #2: Setup dua jari
            left = i + 1
            right = len(nums) - 1

            # Petunjuk #3: Loop dua jari
            while left < right:
                total = angka_kunci + nums[left] + nums[right]

                if total < 0:
                    # Geser penunjuk kiri ke kanan
                    left += 1
                elif total > 0:
                    # Geser penunjuk kanan ke kiri
                    right -= 1
                else: #total == 0
                    # Anda menemukan solusi! Tambahkan ke hasil.
                    hasil.append([angka_kunci, nums[left], nums[right]])

                    # Petunjuk #4: Geser penunjuk dan lompat duplikat.
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return hasil