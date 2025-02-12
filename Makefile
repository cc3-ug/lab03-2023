CC=gcc
CFLAGS=-Wall -g -Itests/include -fPIC -std=c99

EX1_SRC=\
	ex1/vector.c \
	tests/vector_test.c

EX2_SRC=\
	ex2/bubble.c \
	tests/bubble_test.c

EX1_CONV_SRC=$(EX1_SRC:.c=_conv.c)
EX2_CONV_SRC=$(EX2_SRC:.c=_conv.c)
CONV=$(EX1_CONV_SRC) $(EX2_CONV_SRC)

EX1_OBJ=$(EX1_SRC:.c=.o)
EX2_OBJ=$(EX2_SRC:.c=.o)
OBJ=$(EX1_OBJ) $(EX2_OBJ)

all: vector

vector: $(EX1_OBJ)
	$(CC) $(CFLAGS) -o $@ $?

bubble: $(EX2_OBJ)
	$(CC) $(CFLAGS) -o $@ $?

$(OBJ): %.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

$(CONV): %_conv.c: %.c
	$(CC) $(CFLAGS) -Itests/fake -E $< > $@

.PHONY: clean

clean:
	rm -f $(OBJ) $(CONV) vector bubble
	rm -rf grading/__pycache__/
