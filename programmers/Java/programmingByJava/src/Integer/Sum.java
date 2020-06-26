package Integer;

public class Sum {

	public static void main(String[] args) {
		long result = solution(3, 5);
		System.out.println(result);
		
	}
	
	private static long solution(int a, int b) {
		long answer = 0; 
		int start = (a<=b)?a:b;
		int end = (a<=b)?b:a;
		for(int i=start; i<=end; i++) {
			answer += i;
		}
		return answer;
	}

}
