function solution(sequence, k) {
    var answer = [0, sequence.length];
    
    let total = sequence[0];
    let start = 0, end = 0;
    
    while(end < sequence.length && start < sequence.length){
        if(total < k && end < sequence.length){
            end += 1;
            total += sequence[end];
        }
        else if(total == k){
            if(answer[1] - answer[0] > end - start){
                answer = [start, end]
            }
            total -= sequence[start];  
            start += 1;
        }
        else if(total > k && start < sequence.length){
            total -= sequence[start];  
            start += 1;   
        }
    }
    return answer;
}