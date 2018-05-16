import clipboard
import keyboard

cache_lines = []
i = 0

def load_line():
  global cache_lines
  try:
    print('载入第'+str(i)+'条:',cache_lines[i])
    clipboard.copy(cache_lines[i])
  except:
    print('载入异常')

def get_clipboard():
  global cache_lines
  global i
  i = 0
  cache_lines = clipboard.paste().split('\n')
  print('复制内容：',cache_lines)
  load_line()

def next_line():
  global i
  i = i+1
  load_line()
  
def before_line():
  global i
  i = i-1
  load_line()



keyboard.add_hotkey('ctrl+c',lambda:get_clipboard())
keyboard.add_hotkey('ctrl+up',lambda:before_line())
keyboard.add_hotkey('ctrl+down',lambda:next_line())
keyboard.add_hotkey('ctrl+v',lambda:next_line())

keyboard.wait()
