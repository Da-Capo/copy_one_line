# 环境依赖：
下载anaconda： mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.1.0-Windows-x86_64.exe

安装完成后打开Anaconda Prompt 运行 pip install clipboard 和 pip install keyboard

# 使用方法：

打开Anaconda Prompt 

运行
```
git clone https://github.com/Da-Capo/copy_one_line
cd copy_one_line
python line_clipboard.py
```

ctrl+c复制内容到剪切板

再按快捷键操作，程序会按行切分每一条存到内存，选择条目粘贴即可。


# 快捷键设置
以下快捷键可以打开文件line_clipboard.py设置
```
ctrl+alt+c # 获取剪切板并切分
ctrl+alt+x # 下一条
ctrl+alt+z # 上一条
ctrl+shift+a # 粘贴当前条目
```
