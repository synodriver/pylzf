# cython: language_level=3
# cython: cdivision=True
cdef extern from "lzf.h" nogil:
    unsigned int lzf_compress(void *in_data,  unsigned int in_len, void *out_data, unsigned int out_len)
    unsigned int lzf_decompress(void *in_data,  unsigned int in_len, void  *out_data, unsigned int out_len)
    int LZF_VERSION_C "LZF_VERSION"