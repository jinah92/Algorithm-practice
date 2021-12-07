# 완주하지 못한 선수
# 레벨 1
# 해쉬

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

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

solution(participant, completion)