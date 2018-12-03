#include <iostream>
#include <stdlib.h>
using namespace std;

// int main()
// {
//   int i;
//   std::cout<<"Please enter a number between 0 and 99:";
//   std::cin>>i;
//
//   int g;
//   g = 1;
//   list<int> my_list(100);
//
//   while (g<=100)
//   {
//     int h;
//     h=rand() % my_list;
//     std::cout<<"You entered:"<<h<<"\n";
//     if (h > i)
//     {
//       std::cin>> 1;
//       h = h-1
//       std::cout << "You entered:" <<h<<"\n";
//     }
//     if (h < i)
//     {
//       std::cin>> -1;
//       h = h+1
//       std::cout << "You entered:" <<h<< "\n";
//     }
//     else
//     {
//       std::cin >> 0;
//       std::cout << "You entered" <<i<< "\n";
//     }
// }

int main() {
  int input;
  int less = 0;
  int more = 99;
  int eval;
  int guess;

  guess = (less+more)/2;

  std::cout << "Please enter a number between 0and 99: ";
  std::cin >> input;
  std::cout << "Guess: " << guess << std::endl;
  std::cout << "Higher? = 1 Lower? = -1 Correct? = 0: ";
  std::cin >> eval;

  while (eval != 0)
  {
    if (eval == 1)
    {
      more = guess;
    }
    else
    {
      less = guess;
    }
    guess = (less+more) / 2;
    std::cout << "New guess=" << guess << std::endl;
    std::cout << "Higher? = 1 Lower? = -1 Correct = 0: ";
    std::cin >> eval;
  }
  std::cout << "CONGRATS!" << guess << std::endl;
  return 0;
}
