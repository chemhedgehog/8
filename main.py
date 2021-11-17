def kbig(nums,k):
    n=len(nums)
    order = []
    order.append(1)
    for i in range(n):
        order.append(1)
        for j in range(i):
            if nums[i]<nums[j]:
                order[i]+=1
            else:
                order[j]+=1
    for i in range(n):
        if order[i]==k:
            return nums[i]
