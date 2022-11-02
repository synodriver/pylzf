"""
Copyright (c) 2008-2021 synodriver <synodriver@gmail.com>
"""
from pylzf.backends.cffi._lzf import ffi, lib


def compress(data: bytes, outlen: int = None) -> bytes:
    c_data = ffi.from_buffer(data)
    if outlen is None:
        outlen = ((len(data) * 33) >> 5) + 1
    out = ffi.new(f"char[{outlen}]")
    ret = lib.lzf_compress(
        ffi.cast("void *", c_data), len(data), ffi.cast("void *", out), outlen
    )
    if ret == 0:
        raise ValueError
    return ffi.unpack(out, ret)


def decompress(data: bytes, outlen: int) -> bytes:
    c_data = ffi.from_buffer(data)
    out = ffi.new(f"char[{outlen}]")
    ret = lib.lzf_decompress(
        ffi.cast("void *", c_data), len(data), ffi.cast("void *", out), outlen
    )
    if ret == 0:
        raise ValueError
    return ffi.unpack(out, ret)


def compress_into(data: bytes, out: bytearray) -> int:
    in_data = ffi.from_buffer(data)
    out_data = ffi.from_buffer(out)
    ret = lib.lzf_compress(
        ffi.cast("void *", in_data), len(data), ffi.cast("void *", out_data), len(out)
    )
    if ret == 0:
        raise ValueError
    return ret


def decompress_into(data: bytes, out: bytearray) -> int:
    in_data = ffi.from_buffer(data)
    out_data = ffi.from_buffer(out)
    ret = lib.lzf_decompress(
        ffi.cast("void *", in_data), len(data), ffi.cast("void *", out_data), len(out)
    )
    if ret == 0:
        raise ValueError
    return ret


LZF_VERSION = lib.version()
