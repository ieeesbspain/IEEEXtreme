#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING 300000

static int parseint(void)
{
    int c, n;

    n = getchar_unlocked() - '0';
    while ((c = getchar_unlocked()) >= '0')
        n = 10*n + c-'0';

    return n;
}

int main(int argc, char **argv)
{
    register char *original = (char *)malloc(MAX_STRING * 2 * sizeof(char));
    register char *password = original + MAX_STRING;
    int operations = 0;
    int i = 0;

    char mybuf[MAX_STRING];
    setvbuf(stdin, mybuf, _IOFBF, MAX_STRING);

    /* Read input */
    fgets(original, MAX_STRING, stdin);
    strcpy(password, original);
    operations = parseint();

    /* Make each operation */
    for (i = 0; i < operations; ++i) {
        int type = parseint();
        int start = parseint() - 1;
        int end = parseint() - 1;

        /* Read special parameters and make the operation */
        if (type == 1) {
            int cmpStart = parseint() - 1;
            int length = end - start + 1;
            if (memcmp(password + start, password + cmpStart, length) == 0) {
                fprintf(stdout, "Y\n");
            } else {
                fprintf(stdout, "N\n");
            }
        } else if (type == 2) {
            int cpyStart = parseint() - 1;
            int length = end - start + 1;
            memcpy(password + start, original + cpyStart, length);
        } else if (type == 3) {
            int i = 0;
            for (i = start; i <= end; ++i) {
                password[i] = (password[i] == 'z') ? 'a' : password[i] + '\x1';
            }
        }
    }

    free(original);

    return 0;
}
