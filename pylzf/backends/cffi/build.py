import glob
import sys

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef(
    """
unsigned int 
lzf_compress (const void *const in_data,  unsigned int in_len,
              void             *out_data, unsigned int out_len);
              
unsigned int 
lzf_decompress (const void *const in_data,  unsigned int in_len,
                void             *out_data, unsigned int out_len);
int version();
    """
)

source = """
#include "lzf.h"
#include "lzfP.h"

int version()
{
    return LZF_VERSION;
}
"""

ffibuilder.set_source(
    "pylzf.backends.cffi._lzf",
    source,
    sources=["./liblzf/lzf_c.c", "./liblzf/lzf_d.c"],
    include_dirs=["./liblzf"],
)

if __name__ == "__main__":
    ffibuilder.compile()
