#https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Langkah 1: Siapkan dummy node sebagai titik awal dan pointer 'current'.
        dummy = ListNode()
        current = dummy
        
        # Langkah 2: Loop utama selama kedua list masih memiliki node.
        while list1 and list2:
            if list1.val < list2.val:
                # Sambungkan 'current' ke node yang lebih kecil (dari list1).
                current.next = list1
                # Geser penunjuk list1 ke node berikutnya.
                list1 = list1.next
            else:
                # Sambungkan 'current' ke node yang lebih kecil atau sama (dari list2).
                current.next = list2
                # Geser penunjuk list2 ke node berikutnya.
                list2 = list2.next
            
            # PENTING: Geser penunjuk 'current' ke node yang baru saja ditambahkan.
            current = current.next
            
        # Langkah 3: Sambungkan sisa dari list yang belum habis.
        # Hanya salah satu dari dua kondisi ini yang bisa True.
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Langkah 4: Kembalikan kepala dari list yang sebenarnya (setelah dummy).
        return dummy.next