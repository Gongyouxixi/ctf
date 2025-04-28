#include <stdbool.h>
#include <stdio.h>
#define MX (((z >> 5) ^ (y << 2)) + ((y >> 3) ^ (z << 4)) ^ (sum ^ y) + (k[(p & 3) ^ e] ^ z))
bool btea(unsigned int *v, int n, unsigned int *k)
{
    unsigned int z = v[n - 1], y = v[0], sum = 0, e, DELTA = 0x61C88647;
    unsigned int p, q;
    if (n > 1)
    { /* enCoding Part */
        q = 415 / n + 114;//轮次
        while (q-- > 0)
        {
            sum += DELTA;
            e = (sum >> 2) & 3;
            for (p = 0; p < (n - 1); p++)
            {
                y = v[p + 1];
                z = v[p] += MX;
            }

            y = v[0];
            z = v[n - 1] += MX;
        }
        return 0;
    }
    else if (n < -1)
    { /* Decoding Part */
        n = -n;
        q = 415 / n + 114;
        sum = -q * DELTA;
        while (sum != 0)
        {
            e = (sum >> 2) & 3;
            for (p = n - 1; p > 0; p--)
            {
                z = v[p - 1];
                y = v[p] -= MX;
            }

            z = v[n - 1];
            y = v[0] -= MX;
            sum += DELTA;
        }
        return 0;
    }
    return 1;
}

int main()
{
    unsigned int v[11] = {0x480AC20C, 0xCE9037F2, 0x8C212018, 0xE92A18D, 0xA4035274, 0x2473AAB1, 0xA9EFDB58, 0xA52CC5C8, 0xE432CB51, 0xD04E9223, 0x6FD07093}, key[4] = {0x79696755, 0x67346F6C, 0x69231231, 0x5F674231};
    int n = 11;       // n为要加密的数据个数
    btea(v, -n, key); // 取正为加密，取负为解密
    char *p = (char *)v;
    for (int i = 0; i < 44; i++)
    {
        printf("%c", *p);
        p++;
    }
    return 0;
}
