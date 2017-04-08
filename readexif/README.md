## exif    

Exchangeable image file format([Exif](https://en.wikipedia.org/wiki/Exif))是存储在图片文件中的一些辅助信息，一些常见属性和值举例

Tag |	Value
----|-------
Manufacturer |	CASIO
Model |	QV-4000
Orientation (rotation)	| top-left [8 possible values[20]]
Software	|Ver1.01
Date and time	|2003:08:11 16:45:32
YCbCr positioning |	centered
Compression	|JPEG compression
X resolution	|72.00
Y resolution	|72.00
Resolution unit	|Inch
Exposure time	|1/659 s
F-number	|f/4.0
Exposure program	|Normal program
Exif version	|Exif version 2.1
Date and time (original)	|2003:08:11 16:45:32
Date and time (digitized)	|2003:08:11 16:45:32
Components configuration	|Y Cb Cr –
Compressed bits per pixel	|4.01
Exposure bias	|0.0

## 影响    
有些软件旋转图片时，并未实际旋转，而是设置了exif中的 Orientation 选项。而浏览器、不同图片查看器、图片处理库(Opencv、skimage、PIL)等对exif的支持各不相同。有时会遇到坑。

## 已知坑    

### opencv    
截至到 2017.4.8

opencv 2.* 是直接忽略exif的

opencv 3.* 开始支持exif，其中:
* cvLoadImage是早期c语言接口，为向后兼容，仍不处理exif
* imread默认处理exif
* imdecode不处理exif

## 读写exif的库     

### python    
[exifread](https://pypi.python.org/pypi/ExifRead)

### c++
* [TinyEXIF](https://github.com/cdcseacave/TinyEXIF)
* [easyexif](https://github.com/mayanklahiri/easyexif)




