// Runtime: 865 ms, faster than 25.69% of C++ online submissions for Find All Possible Recipes from Given Supplies.
// Memory Usage: 159 MB, less than 39.06% of C++ online submissions for Find All Possible Recipes from Given Supplies.
class Solution {
 public:
  vector<string> findAllRecipes(vector<string> &recipes,
                                vector<vector<string>> &ingredients,
                                vector<string> &supplies) {
    // goal: find all recipes we can construct with given supplies
    // (dependencies) strategy: topological sort/Khan algorithm

    // construct DAG and in-degrees
    map<string, vector<string>> ingredient_to_recipe = {};
    map<string, int> in_degree = {};
    for (int i = 0; i < recipes.size(); ++i) {
      for (auto ing : ingredients[i]) {
        ingredient_to_recipe[ing].push_back(recipes[i]);
      }
      in_degree[recipes[i]] = ingredients[i].size();
    }

    // construct topoligical sort
    deque<string> available(supplies.begin(), supplies.end());
    vector<string> res = {};

    while (!available.empty()) {
      string ing = available[0];
      available.pop_front();
      for (auto rcp : ingredient_to_recipe[ing]) {
        in_degree[rcp] -= 1;
        if (in_degree[rcp] == 0) {
          available.push_back(rcp);
          res.push_back(rcp);
        }
      }
    }

    return res;
  }
};
