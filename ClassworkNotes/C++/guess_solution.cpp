#include <iostream>
#include <cstdlib>
#include <ctime>

int main()
{
  // establish computer's number
  srand(time(NULL));
  int answer = rand()%100;

  int guess;

  // repeat until answer is guessed
  // get a guess from user
  // return whether high/low/right
  std::cout << answer << "\n";
  std::cout << "Please enter a guess" ;
  std::cin >> guess;
  while (guess != answer)
  {
    if (guess > answer)
      std::cout <<"You guessed too high";
    else if (guess < answer)
      std::cout <<"You guessed too low";
  std::cout << "Please enter a guess" ;
  std::cin >> guess;
  }
  std::cout << "Congratulations, you guessed the number !!!" << "\n";
  return 0;
}
