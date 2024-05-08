# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

def sort_array(num1,m,num2,n):
    outlist = []
    for i in range(m):
        outlist.append(num1[i])
    for j in range(n):
        outlist.append(num2[j])

    # outlist2 = outlist.sort()
    outlist.sort()
    print("inside fun ",outlist)

    return sorted(outlist)



nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
ans= sort_array(nums1,m,nums2,n)
print(ans)