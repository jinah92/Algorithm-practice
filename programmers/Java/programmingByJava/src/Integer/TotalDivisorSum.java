package Integer;

public class TotalDivisorSum {

	public static void main(String[] args) {
		int result = solution(5);
		System.out.println(result);
	}
	
	private static int solution(int n) {
		int answer = 0;
		for(int i=1; i<=n; i++) {
			if(n%i==0) {
				answer += i;
			}
		}
		return answer;
	}

}
