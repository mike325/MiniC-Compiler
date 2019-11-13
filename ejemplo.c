
float t;
int i, k;

void print() {
    float j;
}

int recursion( int acumulator ) {
    if (acumulator < 20) {
        return recursion(acumulator + 1);
    }
    return acumulator;
}

int main() {
    int x, acumulator;
    x = 0;
    while (x < 10) {
        x = x + 1;
    }
    recursion(x);
    return 0;
}
