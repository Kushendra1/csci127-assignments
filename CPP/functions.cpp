#include <iostream>

/* def name (i,s):
in C++ it is  ___ name(int i, std::strings){}
in the space put in the return type
*/

int add2(int a, int b){
  int c;
  c = a+b;
  return c;
}

std::string times(std::string s, int t){
  std::string result = "";
  for (int i = 0; i<t; ++i) {
    result = result + s;
  }
  return result;
}

void printGreeting(std::string name){
  std::cout << "Hello" << name << "\n";
  return; // this just goes back to the caller, doesn't send back a value.
}

int add4(int a, int b, int c, int d){
  int x = add2(a,b);        // to reference another function you made, it
  int y = add2(c,d);        //MUST come after the pre established function.
  return add2(x,y);        // OR, you can simply type 'int add2(int a, int b);'
}                           // above the function you're writing.

int fact(int n){
  int product = 1;
  for (int i = n; i <1; i --){
    product = product * i;
  }
  return product;
}

int main()
{
  int a=10, b =20;
  int x = add2(a,b);
  std::cout << x << "\n";
  x = add2(100.5, 500);       //notes how this truncates the answer.
  std::cout << x << "\n";

  std::cout <<times("Hello_", 5) << "\n";

  printGreeting("stan");     //since it's void, there's no need for the std::cout

  std::cout <<add4(1,2,10,20) << "\n";
  return 0;
}
