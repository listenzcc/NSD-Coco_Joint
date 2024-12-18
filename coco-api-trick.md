# COCO API tricks

[toc]

## Solve the error of missing _mask.c

```shell
# Need cython to compile
pip install cython
```

## Error detail

```shell
# Make the cocoapi
$ cd PythonAPI 
$ make

# The output without cython: 
python setup.py build_ext --inplace
running build_ext
building 'pycocotools._mask' extension
clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -iwithsysroot/System/Library/Frameworks/System.framework/PrivateHeaders -iwithsysroot/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/Headers -arch arm64 -arch x86_64 -Werror=implicit-function-declaration -I/Users/remplacement/PycharmProjects/automaticImageCaptioning/venv/lib/python3.8/site-packages/numpy/core/include -I../common -I/Users/remplacement/PycharmProjects/automaticImageCaptioning/venv/include -I/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/include/python3.8 -c ../common/maskApi.c -o build/temp.macosx-10.14.6-arm64-cpython-38/../common/maskApi.o -Wno-cpp -Wno-unused-function -std=c99
clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -iwithsysroot/System/Library/Frameworks/System.framework/PrivateHeaders -iwithsysroot/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/Headers -arch arm64 -arch x86_64 -Werror=implicit-function-declaration -I/Users/remplacement/PycharmProjects/automaticImageCaptioning/venv/lib/python3.8/site-packages/numpy/core/include -I../common -I/Users/remplacement/PycharmProjects/automaticImageCaptioning/venv/include -I/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/include/python3.8 -c pycocotools/_mask.c -o build/temp.macosx-10.14.6-arm64-cpython-38/pycocotools/_mask.o -Wno-cpp -Wno-unused-function -std=c99
clang: error: no such file or directory: 'pycocotools/_mask.c'
clang: error: no input files
error: command '/usr/bin/clang' failed with exit code 1
make: *** [all] Error 1
```