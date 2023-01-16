// Runtime: 91 ms, faster than 42.18% of C++ online submissions for Design Parking System.
// Memory Usage: 33.2 MB, less than 32.24% of C++ online submissions for Design Parking System.
class ParkingSystem {
 public:
  enum class CarType_ { kBig = 1, kMedium = 2, kSmall = 3 };
  map<CarType_, int> spots_left_ = {}; // tally of cars
  ParkingSystem(int big, int medium, int small)
      : spots_left_({pair(CarType_::kBig, big), pair(CarType_::kMedium, medium),
                     pair(CarType_::kSmall, small)}) {}

  bool addCar(int carType) {
    if (spots_left_[static_cast<CarType_>(carType)] == 0) {
      return false;
    } else {
      spots_left_[static_cast<CarType_>(carType)] -= 1;
      return true;
    }
  }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
