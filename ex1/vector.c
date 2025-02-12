/* Include the system headers we need */
#include <stdlib.h>
#include <stdio.h>

/* Include our header */
#include "vector.h"

/* Define what our struct is */
struct vector_t {
  size_t size;
  int *data;
};

/* Utility function to handle allocation failures. In this
   case we print a message and exit. */
static void allocation_failed() {
    fprintf(stderr, "Out of memory.\n");
    exit(1);
}

/* Create a new vector */
vector_t *vector_new() {
  vector_t *retval;

  /*
    Allocate memory for the whole structure
    Check if you got a valid pointer
    If not, report it with allocation_failed()
    If yes, initialize the size
  */

  /*
    Then, allocate memory for the internal data
    Check if you got a valid pointer
    If not, report it with allocation_failed()
    If yes, initialize the content of data
  */

  return retval;
}

/* Free up the memory allocated for the passed vector */
void vector_delete(vector_t *v) {
  
  /*
    Remember to free ALL the memory that you allocated
  */

}

/* Return the value in the vector */
int vector_get(vector_t *v, size_t loc) {

  /*
    Return the content of the location
    What do you return if that location doesn't exist yet?
  */

  return -1;
}

/* Set a value in the vector. If the extra memory allocation fails, call allocation_failed(). */
void vector_set(vector_t *v, size_t loc, int value) {
  
  /*
    What do you do if the location doesn't exist yet?
    Allocate memory for the bigger data
    Remember to check if you got a valid pointer, 
    clean the newly created positions, and update the size
  */

}
