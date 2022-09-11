import time 

def countdown(t):
  while t:
    mins, secs = divmod(t, 60) #商と余、秒数を分とそのあまりの秒数で取得
    timer = '{:02d}:{:02d}'.format(mins, secs)#最小の文字数（幅）を下回った場合0で左を埋める
    print(timer, end='\r') #行頭に戻る、つまり同じ行に上書きして表示することができる
    time.sleep(1)
    t -= 1
  print('Timer Completed!')
  
t = int(input('Enter the time in the seconds: '))
countdown(t)