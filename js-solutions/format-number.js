
function solution(number) {
    var formatNumber = function (number) {
        if (number.length === 3 || number.length === 2)
            return number;
        else if (number.length === 4)
            return number.substring(0, 2) + '-' + number.substring(2);
        else
            return formatNumber(number.substring(0, 3)) + '-' + formatNumber(number.substring(3));
    }
    number = number.replace(/-/g, '');
    number = number.replace(/ /g, '');
    return formatNumber(number);


}
console.log(solution('112323'));
// 112-323 output
