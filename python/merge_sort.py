def merge(left, right):
	result = []
	left_idx, right_idx = 0, 0
	while left_idx < len(left) and right_idx < len(right):
		if left(left_idx) < right(right_idx):
			result.append(left(left_idx))
			left_idx += 1

		else:
			result.append(right(right_idx))
			right_idx += 1

	result.extend(left[left_idx:])
	result.extend(right[right_idx:])
	return result

def merge_sort(in_list):
	if len(in_list) <= 1:
		return in_list

	mid_idx = len(in_list) // 2
	left_half = in_list[:mid_idx]
	right_half = in_list[mid_idx:]

	merge_sort(left)
	merge_sort(right)

	return merge(left, right)
