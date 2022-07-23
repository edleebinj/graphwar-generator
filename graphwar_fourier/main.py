import win32api,win32con,win32gui
import time
from lagrange import lagr,transf#,fourier_series #used for lagrange interpolation
from scipy.interpolate import interp1d
import pyperclip
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fftpack import fftfreq

'''
graphwar cheat using discrete cosine transform

'''
if __name__ == '__main__':
    listoftuples=[]
    print("click the bottom left corner of the cartesian plane")

    state_left = win32api.GetKeyState(0x01)
    while True:
        a = win32api.GetKeyState(0x01)

        if a != state_left:  # state changed
            state_left = a

            if a < 0:
                origin=win32gui.GetCursorPos()#get origin coords
                print(win32gui.GetCursorPos())
                break
            else:
                pass
        time.sleep(0.001)

    print("click the top right corner of cartesian plane")

    state_left = win32api.GetKeyState(0x01)
    while True:
        a = win32api.GetKeyState(0x01)

        if a != state_left:  # state changed
            state_left = a
            if a < 0:
                top_right=win32gui.GetCursorPos()#get top right coords
                print(win32gui.GetCursorPos())
                break
            else:
                pass
        time.sleep(0.001)

    print("click the point you want the graph to go through, and press enter when you finished")

    state_left = win32api.GetKeyState(0x01)
    while True:
        a = win32api.GetKeyState(0x01)
        if int(win32api.GetAsyncKeyState(win32con.VK_RETURN)) != 0:
            break
        if a != state_left:  # state changed
            state_left = a
            if a < 0:
                rndtp=(round(win32gui.GetCursorPos()[0],20),round(win32gui.GetCursorPos()[1],20))#round up tuple
                rndtp2=(round(transf(origin,top_right,rndtp)[0],3),round(transf(origin,top_right,rndtp)[1],3))
                listoftuples.append(rndtp2)
                print(win32gui.GetCursorPos())
            else:
                pass
        time.sleep(0.001)

    #print(lagr(listoftuples).replace("--","+"))#replace -- into +
    #pyperclip.copy(lagr(listoftuples).replace("--","+"))#copy to clipboard
######################################

    listoftuples.sort(key=lambda tup: tup[0])#sort listoftuples

    dt=np.dtype('float,float')
    xdata = np.array(listoftuples,dtype=dt)['f0']#split listoftuples into two nparray
    ydata = np.array(listoftuples,dtype=dt)['f1']
    print((xdata,ydata))

    #x_interp_point=np.linspace(np.amin(xdata),np.amax(xdata),num=100,endpoint=True) #interpolation point for x
    f_linear_interp=np.array([0])
    f_linear_interp = interp1d(xdata,ydata)#linear interpolation function
    #f_cubic_interp = interp1d(xdata,ydata,kind='cubic')#cubic interpolation function #cubic works really badly

    sample_num=50

    x_sample=np.linspace(np.amin(xdata),np.amax(xdata),num=sample_num,endpoint=True)#sample for dft 
    y_linear_sample=f_linear_interp(x_sample)#change cubic or linear hear
    #y_cubic_sample=f_cubic_interp(x_sample)
    
    #dft_coefficient=fft(y_linear_sample)
    dct_result=scipy.fftpack.dct(y_linear_sample)

    
    plt.scatter(xdata,ydata,label="data",color='red')#original data
    plt.plot(x_sample,y_linear_sample,label="linear sampling",color='green',ls=':')#linear interpolation
    #plt.plot(x_sample,y_cubic_sample,label="cubic sampling",color='blue')
    plt.legend(loc='upper left')
    plt.show()
    #print(dct_result)
    cutoff=1e-10
    dct_result[abs(dct_result)<cutoff]=0.0
    equation_str = f"{(dct_result[0]/sample_num)/2:.10f}"
    i=1
    while i < sample_num:
        equation_str+=f"+{dct_result[i]/sample_num:.10f}*cos({i}pi((x-{np.amin(xdata)})*({sample_num}-1)/({np.amax(xdata)}-{np.amin(xdata)})+0.5)/{sample_num})"
        i+=1
    #print(equation_str)
    pyperclip.copy(equation_str.replace("--","+"))#replace -- with +
