CC=gcc
CFLAGS=-Wall -g -Itests/include -fPIC -std=c99

EX1_SRC=\
	ex1/vector.c \
	tests/vector_test.c

EX1_CONV_SRC=$(EX1_SRC:.c=_conv.c)
CONV=$(EX1_CONV_SRC)

EX1_OBJ=$(EX1_SRC:.c=.o)
OBJ=$(EX1_OBJ)

all: vector

vector: $(EX1_OBJ)
	$(CC) $(CFLAGS) -o $@ $?

$(OBJ): %.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

$(CONV): %_conv.c: %.c
	$(CC) $(CFLAGS) -Itests/fake -E $< > $@

.PHONY: clean

clean:
	rm -f $(OBJ) $(CONV) vector

autograder-clean:
	rm -rf ex1.expected grading/__pycache__
