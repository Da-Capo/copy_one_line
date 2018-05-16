# 环境依赖：
下载anaconda： mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.1.0-Windows-x86_64.exe

# 安装方法：

打开Anaconda Prompt 

运行
```
# 安装依赖
pip install clipboard
pip install keyboard
conda install git

# 下载脚本
git clone https://github.com/Da-Capo/copy_one_line

# 运行脚本
cd copy_one_line
python line_clipboard.py
```

# 使用示例
### step1
```
this is the first line
this is the second line
this is the thrid line
```
选中以上内容  按ctrl+c

### step2
ctrl+v 就可以逐条粘贴了


# 快捷键说明(可以无视)
以下快捷键可以打开文件line_clipboard.py设置
与系统快捷键冲突的键 会先执行系统的功能 再执行本脚本功能
```
ctrl+c # 先执行系统复制,再执行脚本的切分条目,再将第一条载入剪切板
ctrl+up #   载入上一条
ctrl+down # 载入下一条
ctrl+v # (系统)粘贴剪切板内容,(剪切板)载入下一条
```
