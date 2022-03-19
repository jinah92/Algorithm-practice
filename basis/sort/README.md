## 정렬(sorting)

- 어떤 데이터들이 주어졌을 때, 이를 정해진 순서대로 정렬하는 방법

<br />

## 버블 정렬(bubble sort)

- **두 인접한 데이터를 비교**해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크거나 작은경우 서로 자리를 변경하며 정렬
- 하나의 턴마다 **마지막 위치에 있는 자리에는 가장 큰(작은) 값이 정렬**되어 진다
- 한 턴에서 swap된 경우가 없다면, 정렬 종료

```python
def bubble_sort(data):
	for index in ranage(len(data)-1):
		swap = False
		for index2 in range(len(data)-index-1):
			if data[index2] > data[index2+1]:
				data[index2], data[index2+1] = data[index2+1], data[index2] # swap
				swap = True
		# 한 턴에 스왑되지 않은 경우, 종료
		if swap == False:
			break
		return data
```

- 시간 복잡도
  $$O(n^2)$$

<br />

## 삽입 정렬(insertion sort)

- **두 번째 인덱스**부터 정렬을 시작
- 기준 인덱스(A) 앞에 있는 데이터(B)부터 비교하여, 해당 인덱스의 값(A)이 더 작으면 B값을 뒤 인덱스로 복사
- A값이 더 큰 데이터를 찾을때까지 반복하여 비교하고, A 값이 더 큰 비교한 인덱스 바로 뒤로 A를 이동

```python
def insertion_sort(data):
	for index in range(len(data)-1):
		for index2 in range(index+1, 0, -1):
			if data[index2] < data[index2-1]:
				data[index2], data[index2-1] = data[index2-1], data[index2]
			else:
				break # 스왑이 안되면 현재 턴에서 비교 종료
	return data
```

- 시간 복잡도
  $$O(n^2)$$

<br />

## 선택 정렬(selection sort)

1. 주어진 데이터 중, 최솟값을 찾음
2. 찾은 최솟값을 데이터 맨 앞에 위치한 값과 swap
3. 맨 앞의 데이터를 뺀 나머지 데이터를 동일한 방법으로 반복

```python
def selection_sort(data):
	for stand in range(len(data)-1):
		lowest = stand
		for index in range(stand+1, len(data)):
			if data[lowest] > data[index]: # 현재 비교 위치와 최솟갑의 크기 비교
				lowest = index
		data[lowest], data[stand] = data[stand], data[lowest]
	return data
```

- 시간 복잡도
  $$O(n^2)$$
