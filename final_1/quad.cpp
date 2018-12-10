#include <iostream>
#include <math.h>

int discriminant(int a, int b, int c){
  int y;
  y = ((b*b) - (4*a*c));
  return y;
}

int quadsolve(int a, int b, int c) {
  int x = discriminant(a,b,c);
  if (x >= 0)
  {
    int s;
    s = (0-b) + (sqrt(x));
    int r;
    r = s/(2 * a);
    return r;
  }
  else
  {
    int t;
    t = 0;
    return t;
  }
}

int main() {
  int x;
  x = discriminant(3,2,1);
  std::cout << x << "\n";
  int z;
  z = discriminant(-2,5,4);
  std::cout << z << "\n";

  int h;
  h = quadsolve(-2,5,4);
  std::cout << h << "\n";
  int g;
  g = quadsolve(3,2,1);
  std::cout << g << "\n";
  return 0;
}
