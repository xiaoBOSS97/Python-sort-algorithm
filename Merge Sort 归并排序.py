def merge(list_left, list_right):
    result = []
    # 传入的两个列表已经是升序有序表
    # 比较需要合并的两个列表的最后一个元素，将较大的元素添加到结果列表中，并删除原列表中该元素，
    # 较小的元素往前插入，直到其中一个列表为空
    while list_left and list_right:
        if list_left[-1] <= list_right[-1]:
            result.insert(0, list_right.pop())
        else:
            result.insert(0, list_left.pop())
    #若另一个列表不为空，其中元素都小于结果列表中元素，将该列表查到结果列表前面
    if list_left:
        result = list_left + result
    if list_right:
        result = list_right + result
    return result
def merge_sort(nums):
    #递归结束条件，输入列表为空或单元素
    if len(nums) <= 1:
        return nums
    #找到列表中间点
    mid = len(nums) // 2
    #合并两个经过分割的列表
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))

# 排序检验
if __name__ == '__main__':
    import numpy as np
    nums = np.random.randint(0, 100, 50)
    nums = nums.tolist()
    print(type(nums))
    print(nums)
    new_nums = merge_sort(nums)
    print(new_nums)
