import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int[] count = new int[words.length];
        int l = begin.length();
        
        Queue<String> num = new LinkedList<>(); 
        num.offer(begin);
        int transCount = 1;
        
        int answer = 0;
        while(!num.isEmpty()){
            for(int k=0;k<num.size();k++){
                String cur = num.poll();
                for(int i=0; i<words.length; i++){

                    if(count[i] == 0){
                        int diff = 0;
                        for(int j=0; j<l; j++){
                            if(cur.charAt(j) != words[i].charAt(j)){
                                diff += 1;
                            }
                        }
                        if(diff == 1){
                            if(words[i].equals(target)){
                                answer = transCount;
                                break;
                            }
                            num.offer(words[i]);
                            count[i] = transCount;
                        }
                    }   
                }
            }
            
            transCount += 1;
        }
        return answer;
    }
}