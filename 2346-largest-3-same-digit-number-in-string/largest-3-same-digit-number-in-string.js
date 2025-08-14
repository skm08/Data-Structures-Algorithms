/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    let maxSub = "";
    for (let i = 0; i <= num.length - 3; i++) {
        if (num[i] === num[i+1] && num[i] === num[i+2]) {
            let candidate = num.substring(i,i+3);
            if (candidate > maxSub) {
                maxSub = candidate;
            }
        }
    }
    return maxSub;
};