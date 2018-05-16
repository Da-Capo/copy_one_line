# 安装方法：
下载anaconda： mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.1.0-Windows-x86_64.exe
打开Anaconda Prompt 
```
# 安装依赖
pip install clipboard
pip install keyboard
conda install git

# 下载脚本
git clone https://github.com/Da-Capo/copy_one_line
```

# 使用方法
### step1
打开Anaconda Prompt 
```
# 运行脚本(安装好以后每一次用就只要执行这一步就行了)
cd copy_one_line
git pull
python line_clipboard.py
```

### step2
```
this is the first line
this is the second line
this is the thrid line
```
选中以上内容  按ctrl+c

### step3
ctrl+v 就可以逐条粘贴了


# 快捷键说明(可以无视,郑总这你要是还不会用 我就真的没办法了)
以下快捷键可以打开文件line_clipboard.py设置
与系统快捷键冲突的键 会先执行系统的功能 再执行本脚本功能
```
ctrl+c # 先执行系统复制,再执行脚本的切分条目,再将第一条载入剪切板
ctrl+up #   载入上一条
ctrl+down # 载入下一条
ctrl+v # (系统)粘贴剪切板内容,(剪切板)载入下一条
```
