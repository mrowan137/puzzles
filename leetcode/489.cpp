// Runtime: 24 ms, faster than 41.68% of C++ online submissions for Robot Room Cleaner.
// Memory Usage: 9.2 MB, less than 30.47% of C++ online submissions for Robot Room Cleaner.
/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the
 * cell.
 *     // Returns false if the cell in front is blocked and robot stays in the
 * current cell. bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

// DFS
class Solution {
 public:
  void backUp(Robot &robot, char &facing, pair<int, int> &pos,
              deque<char> &path) {
    // reverse direction
    char dir = *prev(path.end());
    path.pop_back();
    while (facing != dir) {
      if (facing == 'u') {
        facing = 'r';
      } else if (facing == 'r') {
        facing = 'd';
      } else if (facing == 'd') {
        facing = 'l';
      } else if (facing == 'l') {
        facing = 'u';
      }
      robot.turnRight();
    }
    robot.turnRight();
    robot.turnRight();
    robot.move();
    robot.turnLeft();
    robot.turnLeft();

    // updating state
    auto [x, y] = pos;
    pos = pair<int, int>(x + ((facing == 'r') ? -1 : (facing == 'l' ? 1 : 0)),
                         y + ((facing == 'u') ? 1 : (facing == 'd' ? -1 : 0)));
  }

  void search(Robot &robot, char &facing, pair<int, int> pos,
              set<pair<int, int>> &seen, deque<char> &path) {

    // don't explore it if we've seen it
    if (seen.find(pos) != seen.end()) {
      return;
    }

    // visit the node
    seen.insert(pos);
    robot.clean();

    // explore neighbor nodes
    for (auto dir : {'u', 'r', 'd', 'l'}) {
      while (facing != dir) {
        if (facing == 'u') {
          facing = 'r';
        } else if (facing == 'r') {
          facing = 'd';
        } else if (facing == 'd') {
          facing = 'l';
        } else if (facing == 'l') {
          facing = 'u';
        }
        robot.turnRight();
      }

      // move
      auto [x, y] = pos;
      pair<int, int> trial_pos =
          pair<int, int>(x + ((facing == 'r') ? 1 : (facing == 'l' ? -1 : 0)),
                         y + ((facing == 'u') ? -1 : (facing == 'd' ? 1 : 0)));
      if (seen.find(trial_pos) == seen.end()) {
        bool moved = robot.move();
        if (moved) {
          pos = trial_pos;
          path.push_back(facing);
          search(robot, facing, pos, seen, path);
          backUp(robot, facing, pos, path);
        }
      }
    }
    return;
  }

  void cleanRoom(Robot &robot) {
    // move to a square and clean it, explore each neighbor
    // keep track the 1) path, 2) block & cleaned
    // exit case: all surrounding squares is blocked or cleaned
    //            --> so you backup
    deque<char> path = {};
    set<pair<int, int>> seen = {};
    char facing = 'u';
    search(robot, facing, pair<int, int>({0, 0}), seen, path);
    return;
  }
};
