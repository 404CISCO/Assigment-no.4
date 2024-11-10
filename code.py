def merge_insertion_sort(arr, threshold=20):
def merge(left, right):
result = []
i=j=0
while i < len(left) and j < len(right):if left[i] < right[j]:
result.append(left[i])
i += 1
else:
result.append(right[j])
j += 1
result.extend(left[i:])
result.extend(right[j:])
return result
if len(arr) <= 1:
return arr
elif len(arr) < threshold:
for i in range(1, len(arr)):
key = arr[i]
j=i-1
while j >= 0 and arr[j] > key:
arr[j + 1] = arr[j]
j -= 1
arr[j + 1] = key
return arr
else:
mid = len(arr) // 2
left = merge_insertion_sort(arr[:mid], threshold)
right = merge_insertion_sort(arr[mid:], threshold)
return merge(left, right)
