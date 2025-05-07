def create_box_for():
    m,n = 5,5

    result = []
    for i in range(n):
        row = []
        for j in range(m):
            val = min(i+1, j+1, n-i, m-j)
            row.append(val)
        result.append(row)
    return result


#  ---------------------------------------------------------------
# ! 是檢查沒一個格子距離邊界有「多近」
# ! 所以邊界的就是0，（但是我們把全部都加上1）
import numpy as np

def create_box_numpy(m,n):
    x = np.arange(m).reshape(1, m)  # 當作X軸
    y = np.arange(n).reshape(n, 1)  # 當作Y軸，接著整個圖在右下方

    box = np.minimum(x+1, m-x)
    box = np.minimum(box, y+1)
    box = np.minimum(box, n-y)
    return box
    # return (box + 1).tolist() # 不能直接回傳，numpy出來的是numpy_array 不同於 list_of_lists




create_box_numpy()
# import timeit

# aa = timeit.timeit(create_box_for, number=10000)
# bb = timeit.timeit(create_box_numpy, number=10000)


# print(aa,bb,)


# def create_box(m, n):
#     horizontal = []
#     vertical =[]
#     m_middle = (m + 1) // 2

#     start =1
#     for i in range(1,m+1):
#         horizontal.append(start)
#         if i < m_middle:
#             start += 1
#         elif i==m_middle:
#             if m_middle> m/2:
#                 start-=1
#         else:
#             start -= 1
#     vertical.append(horizontal)
#     horizontal = []
#     print(vertical)

# zip??
