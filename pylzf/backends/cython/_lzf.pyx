# cython: language_level=3
# cython: cdivision=True
from cpython.bytes cimport PyBytes_AS_STRING, PyBytes_FromStringAndSize
from libc.stdint cimport uint8_t

from pylzf.backends.cython.lzf cimport (LZF_VERSION_C, lzf_compress,
                                        lzf_decompress)


cpdef inline bytes compress(const uint8_t[::1] data, Py_ssize_t output_size = 0):
    cdef Py_ssize_t input_size = data.shape[0]
    if output_size == 0:
        output_size = ((input_size * 33) >> 5 ) + 1
    cdef bytes out = PyBytes_FromStringAndSize(NULL, output_size)
    if <void*>out == NULL:
        raise MemoryError
    cdef unsigned int ret
    cdef void* out_ptr = <void*> PyBytes_AS_STRING(out)
    with nogil:
        ret = lzf_compress(<void*>&data[0],<unsigned int> input_size, out_ptr, <unsigned int> output_size)
    if ret == 0:
        raise ValueError
    return out[:ret]

cpdef inline bytes decompress(const uint8_t[::1] data, unsigned int outlen):
    cdef Py_ssize_t input_size = data.shape[0]
    cdef bytes out = PyBytes_FromStringAndSize(NULL, outlen)
    if <void*>out == NULL:
        raise MemoryError
    cdef unsigned int ret
    cdef void* out_ptr = <void*> PyBytes_AS_STRING(out)
    with nogil:
        ret = lzf_decompress(<void*>&data[0],<unsigned int> input_size, out_ptr, outlen)
    if ret == 0:
        raise ValueError
    return out[:ret]

cpdef inline unsigned int compress_into(const uint8_t[::1] data, uint8_t[::1] out) except? 0:
    cdef unsigned int ret
    with nogil:
        ret = lzf_compress(<void *> &data[0], <unsigned int> data.shape[0],
                                            <void *> &out[0], <unsigned int> out.shape[0])
    if ret == 0:
        raise ValueError
    return ret

cpdef inline unsigned int decompress_into(const uint8_t[::1] data, uint8_t[::1] out) except? 0:
    cdef unsigned int ret
    with nogil:
        ret = lzf_decompress(<void *> &data[0], <unsigned int> data.shape[0],
                                            <void *> &out[0], <unsigned int> out.shape[0])
    if ret == 0:
        raise ValueError
    return ret

LZF_VERSION = LZF_VERSION_C
