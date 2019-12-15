# 내 풀이방법

def solution(participant, completion):
	n = len(completion)
	participant.sort()
	completion.sort()
	
	for i in range(0, n):
		if participant[i] != completion[i]:
			answer = participant[i]
			return answer

	answer = participant[-1]
	return answer