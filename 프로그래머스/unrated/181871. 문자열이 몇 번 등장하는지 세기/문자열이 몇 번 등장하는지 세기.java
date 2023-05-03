class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        for(int i=0;i <= myString.length() - pat.length();i++){
            if(pat.charAt(0) == myString.charAt(i)){
                for(int j=0; j<pat.length();j++){
                    if(myString.charAt(i+j) != pat.charAt(j)){
                        break;
                    }
                    if(j == pat.length() - 1){
                        answer += 1;
                    }
                }
            }
        }
        
        
        return answer;
    }
}