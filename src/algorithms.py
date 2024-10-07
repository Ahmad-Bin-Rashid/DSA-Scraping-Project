import math

# Bubble Sort
def bubble_sort(data, col):
   
   n = len(data)
   for i in range(n):
      for j in range(0, n - i - 1):
            if data[j][col] > data[j + 1][col]:
               data[j], data[j + 1] = data[j + 1], data[j]
   
   return data
     
# Selection Sort
def selection_sort(data, col):
   
   n = len(data)
   for i in range(n):
      min_index = i
      for j in range(i+1, n):
         if data[j][col] < data[min_index][col]:
               min_index = j
      data[i], data[min_index] = data[min_index], data[i]
   
   return data


# Insertion Sort
def insertion_sort(data, col):
   
   n = len(data)
   for i in range(1, n):
      key_item = data[i]
      j = i - 1
      while j >= 0 and data[j][col] > key_item[col]:
         data[j + 1] = data[j]
         j -= 1
      data[j + 1] = key_item
   
   return data


# Merge Sort
def merge_sort(data, col):
   
   data = merge_sort_recursive(data, col)
   
   return data

def merge_sort_recursive(data, col):
   if len(data) > 1:
      mid = len(data) // 2
      left_half = data[:mid]
      right_half = data[mid:]

      left_half = merge_sort_recursive(left_half, col)
      right_half = merge_sort_recursive(right_half, col)

      return merge(left_half, right_half, col)
   return data

def merge(left, right, col):
   result = []
   i = j = 0
   while i < len(left) and j < len(right):
      if left[i][col] < right[j][col]:
         result.append(left[i])
         i += 1
      else:
         result.append(right[j])
         j += 1
   result.extend(left[i:])
   result.extend(right[j:])
   return result


# Quick Sort
def quick_sort(data, col):
   
   quick_sort_recursive(data, 0, len(data) - 1, col)
   
   return data

def quick_sort_recursive(data, low, high, col):
   if low < high:
      pi = partition(data, low, high, col)
      quick_sort_recursive(data, low, pi - 1, col)
      quick_sort_recursive(data, pi + 1, high, col)

def partition(data, low, high, col):
   pivot = data[high][col]
   i = low - 1
   for j in range(low, high):
      if data[j][col] <= pivot:
         i += 1
         data[i], data[j] = data[j], data[i]
   data[i + 1], data[high] = data[high], data[i + 1]
   return i + 1


# Shell Sort
def shell_sort(data, col):
   
   n = len(data)
   gap = n // 2
   
   while gap > 0:
      for i in range(gap, n):
         temp = data[i]
         j = i
         while j >= gap and data[j - gap][col] > temp[col]:
               data[j] = data[j - gap]
               j -= gap
         data[j] = temp
      gap //= 2
   
   return data


# Gnome Sort
def gnome_sort(data, col):
   
   index = 0
   n = len(data)
   
   while index < n:
      if index == 0 or data[index][col] >= data[index - 1][col]:
         index += 1
      else:
         data[index], data[index - 1] = data[index - 1], data[index]
         index -= 1
   
   
   return data

# Counting Sort
def counting_sort(data, col):
   arr = [row[col] for row in data]
   
   if all(isinstance(i, int) for i in arr):
      max_val = max(arr)
      count = [0] * (max_val + 1)
      
      for num in arr:
         count[num] += 1

      sorted_arr = []
      for i in range(len(count)):
         sorted_arr.extend([i] * count[i])

      sorted_data = []
      index = 0
      for val in sorted_arr:
         for row in data:
               if row[col] == val:
                  sorted_data.append(row)
                  break

      return sorted_data

      # sort for strings (based on ASCII values)
   elif all(isinstance(i, str) for i in arr):
      max_val = ord(max([i[0] for i in arr]))
      count = [0] * (max_val + 1)
      
      for char in arr:
         count[ord(char[0])] += 1

      sorted_arr = []
      for i in range(len(count)):
         sorted_arr.extend([chr(i)] * count[i])

      sorted_data = []
      for val in sorted_arr:
         for row in data:
               if row[col][0] == val:
                  sorted_data.append(row)
                  break

      return sorted_data


# Radix Sort
def radix_sort(data, col):
   if all(isinstance(row[col], int) for row in data):
      max_val = max(row[col] for row in data)
      place = 1
      while max_val // place > 0:
         counting_sort_int_for_radix(data, col, place)
         place *= 10

   elif all(isinstance(row[col], str) for row in data):
      counting_sort_str_for_radix(data, col)
   
   return data


def counting_sort_int_for_radix(data, col, place):
   n = len(data)
   output = [None] * n
   count = [0] * 10  

   arr = [row[col] for row in data]

   for i in arr:
      index = (i // place) % 10
      count[index] += 1

   for i in range(1, 10):
      count[i] += count[i - 1]

   for i in range(n - 1, -1, -1):
      index = (arr[i] // place) % 10
      output[count[index] - 1] = data[i]
      count[index] -= 1

   for i in range(n):
      data[i] = output[i]
      

# sort for strings based on ASCII values
def counting_sort_str_for_radix(data, col):
   n = len(data)
   output = [None] * n
   count = [0] * 256 
   arr = [row[col] for row in data]

   for char in arr:
      count[ord(char[0])] += 1

   for i in range(1, 256):
      count[i] += count[i - 1]

   for i in range(n - 1, -1, -1):
      char = arr[i]
      output[count[ord(char[0])] - 1] = data[i]
      count[ord(char[0])] -= 1

   for i in range(n):
      data[i] = output[i]



# Bucket Sort function
def bucket_sort(data, col):
   if not data:
      return data

   arr = [row[col] for row in data]

   is_int = all(isinstance(i, int) for i in arr)
   is_str = all(isinstance(i, str) for i in arr)

   if is_int:
      max_value = max(arr)
      num_buckets = round(math.sqrt(len(arr)))
      buckets = [[] for _ in range(num_buckets)]
      
      for i, val in enumerate(arr):
         index = min(math.ceil(val * num_buckets / max_value), num_buckets) - 1
         buckets[index].append(data[i]) 
   elif is_str:
      max_value = ord(max([i[0] for i in arr]))
      num_buckets = round(math.sqrt(len(arr)))
      buckets = [[] for _ in range(num_buckets)]
      
      for i, val in enumerate(arr):
         index = min(math.ceil(ord(val[0]) * num_buckets / max_value), num_buckets) - 1
         buckets[index].append(data[i]) 

   sorted_data = []
   for bucket in buckets:
      sorted_bucket = insertion_sort_for_bucket(bucket, col)
      sorted_data.extend(sorted_bucket)

   return sorted_data


def insertion_sort_for_bucket(bucket, col):
   for i in range(1, len(bucket)):
      key_item = bucket[i]
      j = i - 1
      while j >= 0 and bucket[j][col] > key_item[col]:
         bucket[j + 1] = bucket[j]
         j -= 1
      bucket[j + 1] = key_item
   return bucket
