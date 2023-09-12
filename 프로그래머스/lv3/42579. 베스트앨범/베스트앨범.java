import java.util.HashMap;
import java.util.Collections;
import java.util.ArrayList;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        
        HashMap<String, Integer> genrePlay = new HashMap<>();
        int n = genres.length;
        for(int i=0;i<n;i++){
            if(genrePlay.get(genres[i]) == null){
                genrePlay.put(genres[i], plays[i]);    
            }
            else{
                genrePlay.put(genres[i], genrePlay.get(genres[i]) + plays[i]);
            }
            
        }
        
        ArrayList<String> keySet = new ArrayList<>(genrePlay.keySet());
        keySet.sort((c1, c2) -> genrePlay.get(c2).compareTo(genrePlay.get(c1)));
        
        ArrayList<Integer> answerList = new ArrayList<>();
        
        for(String s : keySet){
            
            int count = 0;
            
            ArrayList<Integer> numberList = new ArrayList<>();
            for(int i=0;i<n;i++){
                if(genres[i].equals(s)){
                    numberList.add(plays[i]);
                }
            }
            numberList.sort((c1, c2) -> c2.compareTo(c1));
            
            
            for(int i: numberList){
                if(count == 2){
                    break;
                }
                
                for(int j=0;j<n;j++){
                    if(plays[j] == i){
                        answerList.add(j);
                        plays[j] = 10001;
                        break;
                    }
                }
                count++;
            }
        }
        
        int[] answer = new int[answerList.size()];
        for(int i=0;i<answerList.size();i++){
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}