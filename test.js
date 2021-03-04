// 프로그래머스 > 같은 숫자는 싫어
// https://programmers.co.kr/learn/courses/30/lessons/12906

function solution(arr) {

    var answer = [];

    for(var i = 0; i < arr.length; i++) {

        if( answer[answer.length - 1] != arr[i] ) {
            answer.push(arr[i]);
        }

    }
    
    return answer;
}


var arr = [3,3,1,1,7,7,7];
console.log(solution(arr));