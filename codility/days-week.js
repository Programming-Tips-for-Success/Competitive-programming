// problem statement
// Days of the week are represented as three-letter strings ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun").

// Write a function solution that, given a string S representing the day of the week and an integer K (between 0 and 500, inclusive), returns the day of the week that is K days later.

// For example, given S = "Wed" and K = 2, the function should return "Fri".

// Given S = "Sat" and K = 23, the function should return "Mon".

function solution(s, k) {
    var weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]; 
    var index = weekDays.findIndex(function (weekDay) { return weekDay == s; }); 
    return weekDays[(index + k) % 7];
}