function solution(my_string) {
    const arr = my_string.split(' ')
    //첫번째 숫자로 result 초기화
    let result = Number(arr[0]);
    for(let i =1; i<arr.length; i+=2){
        
        const operator = arr[i] //홀수가 연산자
        const operand = Number(arr[i+1]) //짝수가 연산숫자
        
        switch (operator){
            case '+' :
                result += operand;
                break;
            case '-' : 
                result -= operand;
                break;
        }
    }
    return result;
}