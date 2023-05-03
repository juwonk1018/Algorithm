
class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        
        for(long i=-r2; i<=r2; i++){
            double c2 = Math.sqrt(((long)r2*(long)r2 - i*i));
            double c1 = Math.sqrt(((long)r1*(long)r1 - i*i));
            c2 = (int)c2 * 2 + 1;
            
            if(c1 > 0){
                if(c1 % 1 == 0){
                    c1 -= 1;
                }
                c1 = (int)c1 * 2 + 1;
            }
            else{
                c1 = 0;
            }
            answer += (c2 - c1);
        }
        
        return answer;
    }
}