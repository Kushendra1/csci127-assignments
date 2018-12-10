#include <iostream>

int sumofsquares(int a, int b) {
  int s;
  while(a < b){
    s = 0;
    for(a;a < (b + 1) ; a = (a + 1)){
      int r = a*a;
      s = s + r;
    }
  }
  return s;
}

int main(){
  std::cout << sumofsquares(5,10) << "\n";
  std::cout << sumofsquares(4,8) << "\n";
  std::cout << " ^^ This is the sumofsquares of the Giants record :(" << "\n";
  std::cout << sumofsquares(9,13) << "\n";

  return 0;
}
