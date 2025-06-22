class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> result;
        int n = s.length();
        int i = 0;
        while (i < n) {
            string group = s.substr(i, k);
            if (group.length() < k) {
                group += string(k - group.length(), fill);
            }
            result.push_back(group);
            i += k;
        }
        return result;
    }
};