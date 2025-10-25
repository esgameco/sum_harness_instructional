#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>
#include <stdlib.h>

#include "sums.h"

void setup(int64_t N, int64_t A[])
{
    printf(" inside sum_indirect problem_setup, N=%lld \n", N);

    for (int i = 0; i < N; i++) 
    {
        A[i] = (int64_t)lrand48() % N;
    }
}

int64_t sum(int64_t N, int64_t A[])
{
    printf(" inside sum_indirect perform_sum, N=%lld \n", N);

    int64_t total = 0;
    int64_t index = A[0];
    int64_t temp;

    for (int64_t i = 0; i < N; i++) 
    {
        temp = A[index];
        index = temp;
        total += temp;
    }

    return total;
}

