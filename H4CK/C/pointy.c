#include <stdio.h>
#include <string.h>

void main(int argc, char const *argv[]) {
  /* provide N byte buffer
  1 double word == 4 bytes, if more
  words are provided by user than bytes allocated
  there will be access violation segmentation fault
  */
 char buffer [50];
  if(argc < 2){
    printf("USAGE: %s <argument> \n", argv[0]);
    exit(0);
  }

  strcpy(buffer, argv[1]);
  printf("%s\n", &buffer);
  printf("%s\n", *buffer);
}
