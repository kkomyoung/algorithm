// 프로그래머스 > 2016년
// https://programmers.co.kr/learn/courses/30/lessons/12901

function solution(a, b) {
  var answer = '';
  var weekArray = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
  var month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  var remainder;
  var sum = 0;

  for(var i = 0; i < a; i++) {
    sum += month[i];
  }

  sum += b;
  remainder = sum % 7;

  answer = weekArray[remainder];
  
  return answer;
}

console.log(solution(3, 17));




