#include <algorithm>
#include <cstdlib>
 
template<class T>
T randMfromN(T begin, T end, size_t num_random) {
    size_t left = std::distance(begin, end);
    while (num_random--) {
        T r = begin;
        std::advance(r, rand()%left);
        std::swap(*begin, *r);
        ++begin;
        --left;
    }
    return begin;
}
