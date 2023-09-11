class Solution {
    public String solution(String s) {
        String num[] = s.split(" ");
        
        int min = Integer.parseInt(num[0]);
        int max = Integer.parseInt(num[0]);
        
        for(int i=0;i<num.length;i++){
            int n = Integer.parseInt(num[i]);
            if(n > max){
                max = n;
            }
            if(n < min){
                min = n;
            }
                
        }
        
        
        String answer = Integer.toString(min) + " " + Integer.toString(max);
        return answer;
    }
}