package Integer;

public class OddOrEven {

	public static void main(String[] args) {
		String result = solution(2);
		System.out.println(result);
	}


	public static String solution(int num) {
        String answer = (num%2==0)?"Even":"Odd";
        return answer;
    }

}
