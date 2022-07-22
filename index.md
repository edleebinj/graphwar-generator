## Welcome to graphwar-generator
this is a simple equation generator for graphwar, equations calculated using discrete cosine transformation
<img width="962" alt="graphwar" src="https://user-images.githubusercontent.com/81552194/180500611-5bd16ee5-2d9b-4c97-bc5f-ba6ec9460bc4.png">

## How this program works?
#### 1. gather data from clicking using win32api
```python
while True:
    a = win32api.GetKeyState(0x01)
    if int(win32api.GetAsyncKeyState(win32con.VK_RETURN)) != 0:
        break
    if a != state_left:  # state changed
        state_left = a
        if a < 0:
            rndtp = (round(win32gui.GetCursorPos()[0],20),round(win32gui.GetCursorPos()[1],20))#round up tuple
            rndtp2 = (round(transf(origin,top_right,rndtp)[0],3),round(transf(origin,top_right,rndtp)[1],3))
            listoftuples.append(rndtp2)
            print(win32gui.GetCursorPos())
    time.sleep(0.001)
```
#### 2. generate interpolation of data using scipy

```python
f_linear_interp = np.array([0])
f_linear_interp = interp1d(xdata,ydata)
```
![Figure_1](https://user-images.githubusercontent.com/81552194/180514007-91cd0a28-1059-49c1-9f58-3615603c43b2.png)
#### 3. generate samples and apply dct
```python
f_linear_interp=np.array([0])
f_linear_interp = interp1d(xdata,ydata)#linear interpolation function

sample_num=50

x_sample=np.linspace(np.amin(xdata),np.amax(xdata),num=sample_num,endpoint=True) 
y_linear_sample=f_linear_interp(x_sample)
    
dct_result=scipy.fftpack.dct(y_linear_sample)
```


#### 4. calculate equation using following formula


![03ebd9c1833db5ff969647c08e457e6610c64ea5](https://user-images.githubusercontent.com/81552194/180507491-6dcb9c33-72e5-4b7a-8b30-2eeff2cda6b2.svg)
```python
equation_str = f"{(dct_result[0]/sample_num)/2:.10f}"
i=1
while i < sample_num:
    equation_str+=f"+{dct_result[i]/sample_num:.10f}*cos({i}pi((x-{np.amin(xdata)})*({sample_num}-1)/({np.amax(xdata)}-{np.amin(xdata)})+0.5)/{sample_num})"
    i+=1
```



![螢幕擷取畫面 2022-07-23 024047 (2)](https://user-images.githubusercontent.com/81552194/180503787-d8ac63c7-6b2a-4dc9-a053-780e599c3429.png)

![22](https://user-images.githubusercontent.com/81552194/180507038-d35346b5-d2d7-4c74-a064-2dc517c9494a.jpg)

![22321](https://user-images.githubusercontent.com/81552194/180507042-281a7948-31ff-4503-be37-187f6298ebc0.jpg)

![123123](https://user-images.githubusercontent.com/81552194/180507046-cdcf814f-24c0-4a0a-9f20-30d1b134b1be.jpg)

You can go to [edleeebinj's github](https://github.com/edleebinj/) to have fun.






Whenever you are bored, GitHub Pages will rebuild the joy in your mind, from the ground up.

### Mashed potato

Mashed potato is a lightweight and easy-to-use food. It includes nothing.

## 1+1=2!?
go check out my newest graphwar fft equation generator at my [github page](https://github.com/edleebinj)
also check out [https://edleebinj.github.io/graphwar-generator/](https://edleebinj.github.io/graphwar-generator/)

[Despacito on 摩爾莊園](https://www.youtube.com/watch?v=zXVp4KZaXyk&ab_channel=Ouob)




