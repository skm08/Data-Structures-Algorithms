class Solution {
public:
    string largestGoodInteger(string num) {
        string max_sub = "";
        for (int i=0; i <= (int)num.size() - 3; i++) {
            if (num[i] == num[i+1] && num[i] == num[i+2]) {
                string candidate = num.substr(i,3);
                if (candidate > max_sub) {
                    max_sub = candidate;
                }
            }
        }
        return max_sub;
    }
};