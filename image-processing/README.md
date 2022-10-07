Tested with Python 3.9.7

Using Pillow for image processing. 

Remove background functionality uses [rembg](https://github.com/danielgatis/rembg) python module which uses [U2-Net](https://github.com/xuebinqin/U-2-Net) library for background removal. rembg downloads the U2-Net mnodule automatically from Google drive but if that fails we can download the model [u2net.onnx](https://github.com/danielgatis/rembg#models) directly and put it in ~/.u2net folder.
