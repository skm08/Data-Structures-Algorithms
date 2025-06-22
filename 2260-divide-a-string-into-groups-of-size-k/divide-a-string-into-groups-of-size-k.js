/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
var divideString = function(s, k, fill) {
    let result = [];
    let i = 0;
    while(i < s.length) {
        let group = s.slice(i,i+k);
        if (group.length < k) {
            group += fill.repeat(k-group.length);
        }
        result.push(group);
        i += k;
    }
    return result;
};