import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int n = tangerine.length;
        
        HashMap<Integer, Integer> num = new HashMap<Integer, Integer>();
        
        for(int i=0;i<n;i++){
            if(num.get(tangerine[i]) == null){
                num.put(tangerine[i], 1);    
            }
            else{
                num.put(tangerine[i], num.get(tangerine[i]) + 1);
            }
        }
        
        ArrayList<Integer> numberOfSize = new ArrayList<>();
        
        for(int i : num.keySet()){
            numberOfSize.add(num.get(i));
        }
        
        int pick = 0;
        int answer = 0;
        
        Collections.sort(numberOfSize, Collections.reverseOrder());
        while(pick < k){
            pick += numberOfSize.remove(0);
            answer += 1;
            if(pick >= k){
                break;
            }
            
        }
        return answer;
    }
}