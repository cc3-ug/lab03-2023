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

  // Allocate memory for the struct

  // Check if we got a valid pointer, if not, report it

  // Initialize size

  // Allocate memory for the struct

  // Check if we got a valid pointer for data, if not, clean and report

  // Initialize the content of data

  return retval;
}

/* Free up the memory allocated for the passed vector */
void vector_delete(vector_t *v) {
  
  // Remember, you need to free up ALL the memory that is allocated

}

/* Return the value in the vector */
int vector_get(vector_t *v, size_t loc) {
  
  // Return the content of the location
  // What do we return if that location doesn't exist yet?

  return -1;
}

/* Set a value in the vector. If the extra memory allocation fails, call allocation_failed(). */
void vector_set(vector_t *v, size_t loc, int value) {
  
  // What do we do if the location doesn't exist yet?

  // Change the size of the structure

  // Allocate memory for the bigger data

  // Check if we got a valid pointer for the bigger data, if not, clean and report

  // What do we write in the newly created positions?

  // Finally, put the value in loc

}
