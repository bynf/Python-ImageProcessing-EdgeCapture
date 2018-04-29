import numpy as np
from PIL import Image

def RGBtoGray(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]= data[i][j][0] * 0.299 + data[i][j][1] * 0.587 + data[i][j][2] * 0.114
    return data

def ConvFilter(data, filter):
    resault = np.zeros((len(data), len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            x = data[i][j-1][0] if j-1 >=0 else 0
            y = data[i][j][0]
            z = data[i][j+1][0] if j+1 < len(data[i]) else 0
            resault[i][j]= x * filter[0] + y * filter[1] + z * filter[2]
    return resault

def FilterAndShow(arr,filt):
    final_resault = ConvFilter(arr, filt)
    Image._show(Image.fromarray(final_resault))

def main():
    img = Image.open("Ataturk.jpg")
    #Image._show(img) # original image
    imgArray= np.array(img)
    #RGB to GrayScale
    tempArray=RGBtoGray(imgArray)
    Image._show(Image.fromarray(tempArray))
    FilterAndShow(tempArray,[0, -1, 1])
    FilterAndShow(tempArray,[1,-1,0])
    FilterAndShow(tempArray,[-0.5, 0, 0.5])
main()
