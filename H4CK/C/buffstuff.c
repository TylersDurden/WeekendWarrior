#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[]) {
  /* provide N byte buffer
  1 double word == 4 bytes, if more
  words are provided by user than bytes allocated
  there will be access violation segmentation fault
  */
  int correct = 0;
  char buff[15];
  

  if(argc < 2){
    printf("USAGE: %s <argument> \n", argv[0]);
    return 0;
  }
  /* Fail to check length of input when copying
  into buffer with strcpy*/
  strcpy(buff, argv[1]);
  if (strcmp(buff, "badpassword")){
    printf("\t~ Incorrect Password ~\n");
  }else{
  	correct = 1;
  }

  /* Use the 'over-flowable' correct flag as execution flow control */
  if (correct){
    printf("~ Access Granted ~\n");
  }
}
