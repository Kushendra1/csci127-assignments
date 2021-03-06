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
    s = (-b + sqrt(x)) / (2*a);
    return s;
  }
  else
  {
    return 0;
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
  int w;
  w = quadsolve(1,2,3);
  std::cout << w << "\n";
  return 0;
}
