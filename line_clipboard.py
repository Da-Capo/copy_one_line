import clipboard
import keyboard

cache_lines = []
i = 0

def get_clipboard():
  global cache_lines
  cache_lines = clipboard.paste().split('\n')
  print('复制内容：',cache_lines)

def next_line():
  global i
  i = i+1
  print('第'+str(i)+'条')
  
def before_line():
  global i
  i = i-1
  print('第'+str(i)+'条')

def write_line():
  global cache_lines
  global i
  try:
    print('粘贴',str(i),cache_lines[i])
    keyboard.write(cache_lines[i])
  except:
    print('粘贴异常')


keyboard.add_hotkey('ctrl+alt+c',lambda:get_clipboard())
keyboard.add_hotkey('ctrl+alt+z',lambda:next_line())
keyboard.add_hotkey('ctrl+alt+x',lambda:before_line())
keyboard.add_hotkey('ctrl+shift+a',lambda:write_line())

keyboard.wait()
