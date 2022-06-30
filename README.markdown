<h1 align="center"><i>✨ pylzf ✨ </i></h1>

<h3 align="center">The python binding for <a href="https://github.com/ProjectHentai/liblzf">liblzf</a> </h3>

[![pypi](https://img.shields.io/pypi/v/pylzf.svg)](https://pypi.org/project/pylzf/)
![python](https://img.shields.io/pypi/pyversions/pylzf)
![implementation](https://img.shields.io/pypi/implementation/pylzf)
![wheel](https://img.shields.io/pypi/wheel/pylzf)
![license](https://img.shields.io/github/license/synodriver/pylzf.svg)
![action](https://img.shields.io/github/workflow/status/synodriver/pylzf/build%20wheel)

### 安装
```bash
pip install pylzf
```


### 使用
```python
import pylzf

pylzf.compress(b"123", 100)
pylzf.decompress(b"xxx", 100)
data = bytearray(1000)
pylzf.compress_into(b"1212", data)
pylzf.decompress_into(b"xxxx", data)
```

### 公开函数
```python
def compress(data: bytes, outlen: int = ...) -> bytes: ...
def decompress(data: bytes, outlen: int) -> bytes: ...
def compress_into(data: bytes, out: bytearray) -> int: ...
def decompress_into(data: bytes, out: bytearray) -> int: ...
```

### 本机编译
```
python -m pip install setuptools wheel cython cffi
git clone https://github.com/synodriver/pylzf
cd pylzf
git submodule update --init --recursive
python setup.py bdist_wheel --use-cython --use-cffi
```

### 后端选择
默认由py实现决定，在cpython上自动选择cython后端，在pypy上自动选择cffi后端，使用```LZF_USE_CFFI```环境变量可以强制选择cffi