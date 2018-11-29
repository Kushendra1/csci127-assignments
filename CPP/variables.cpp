#include <iostream>

int main()
{
  //long int x; and short int, basically long and short ints
  //unsigned x; for when engatives don't exist
  int i;
  int some_variable = 10, another_variable;
  double d;    //gives you 2x significant digits. Takes more memory
  float f;     //gives you 8 sig figs. So double gives you 16

  char c;

  c = 'z';     //double quotes are for strings, single quotes are for characters

  i = 20;
  i = i + some_variable;
  d = i;

  i = i/4.2;
  std::cout <<"i = " << i << "\n";

  d = d/4.2;
  std::cout << "d = " << d << "\n";

  std::cout << c << "\n";

  std::cout << true << "\n";
  std::cout << false << "\n";
  std::cout << (i>100) << "\n";
  std::cout << (i<100) << "\n";

  std::cout << "Please enter a number:";
  std::cin >> i;
  std::cout << "You entered: " << i << "\n";

  return 0;
}
