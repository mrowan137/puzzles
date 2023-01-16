// Runtime: 204 ms, faster than 12.10% of C++ online submissions for Wildcard Matching.
// Memory Usage: 23.8 MB, less than 34.44% of C++ online submissions for Wildcard Matching.
class Solution {
public:
    bool isMatch(string s, string p_orig) {        
        // make a copy, don't modify the original
        string p = p_orig;
        
        // preprocess delete repeated wildcard
        while (p.find("**") != string::npos) {
            p.replace(p.find("**"), 2, "*");
        }
        
        // see if s match to p
        // ? can replace the char
        // * can collapse the sequence
        int m = s.size(), n=p.size();
        
        // dp[j][i] means string up to i match pattern up to j
        // separate into cases. when does string match pattern?
        // 1) s[i] == p[j] and dp[j-1][i-1]
        // 2) p[j] == ?    and dp[j-1][i-1]
        // 3) p[j] = * and dp[j-1][i-k] for some k>=1
        vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
        dp[0][0] = 1; // the empty strange do match
        if (n > 0){dp[1][0] = 1 ? p[0] == '*' : 0;}
        
        for (int i=1; i<n+1; ++i) { //p
            for (int j=1; j<m+1; ++j) { //s
                if (s[j-1] == p[i-1]) {
                    dp[i][j] = dp[i-1][j-1];
                } else if (p[i-1] == '?') {
                    dp[i][j] = dp[i-1][j-1];
                } else if (p[i-1] == '*') {
                    // search for any match in substring of curr string to pattern, excluding wildcard
                    bool foundTheMatch = std::find(dp[i-1].begin(), 
                                                   dp[i-1].begin()+j+1, 1) != dp[i-1].begin()+j+1;
                    if (foundTheMatch) {dp[i][j] = 1;}
                    
                }
            }
        }
        
        return dp[n][m];
    }
};
