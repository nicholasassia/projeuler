public class euler34 {
    private static int fact(int n){
        if (n <= 1){
        return 1;
        }
        return n * fact(n-1);
    }
    public static void main(String[] args){
        int result = 0;
        for (int n = 19; n < 100000; n++){
            int sum = 0;
            String tmp = String.valueOf(n);
            for (char num : tmp.toCharArray()){
                sum += fact(Character.getNumericValue(num));
                if (sum == n){
                    result += n;
                    System.out.println("digit factorial is "+n);
                }
            }
        }
    System.out.println(result);
    }
}