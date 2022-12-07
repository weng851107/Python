```Text
Author: Antony_Weng <weng851107@gmail.com>

This file is only used for the record of the learning process, only used by myself and the file has never been leaked out.
If there is related infringement or violation of related regulations, please contact me and the related files will be deleted immediately. Thank you!
```

# 目錄

- [Note](#0)
  - [如何在linux下執行python程式](#0.1)


<h1 id="0">Note</h1>

<h2 id="0.1">如何在linux下執行python程式</h2>

1. 直接使用 `python ***x.py` 執行。其中python可以寫成python的絕對路徑。使用 `which python` 進行查詢。

2. 在檔案的頭部（第一行）寫上 `#!/usr/bin/python2.7`，這個地方使用python的絕對路徑，就是上面用 `which python` 查詢來的結果。

然後在外面就可以使用./***.py執行了。
