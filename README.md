# Python-ImageProcessing-EdgeCapture
<br>
<h2>Original Image</h2> 
We want to get the edges of the following image. We will use three methods for this.<br><br>
<image src="https://github.com/bynf/Python-ImageProcessing-EdgeCapture/blob/master/OriginalImage.jpg?raw=true"></image>

<h3>GrayScale</h3>
<image src="https://github.com/bynf/Python-ImageProcessing-EdgeCapture/blob/master/Images/Gray.png?raw=true"/>

<h3>Forward-end differences</h3>
<h4>Filter : [0, -1, 1]</h4>
<image src="https://github.com/bynf/Python-ImageProcessing-EdgeCapture/blob/master/Images/Filter1.png?raw=true"/>

<h3>Backward differences</h3>
<h4>Filter : [1,-1,0]</h4>
<image src="https://github.com/bynf/Python-ImageProcessing-EdgeCapture/blob/master/Images/Filter2.png?raw=true"/>

<h3>Central differences</h3>
<h4>Filter :[-0.5, 0, 0.5]</h4>
<image src="https://github.com/bynf/Python-ImageProcessing-EdgeCapture/blob/master/Images/Filter3.png?raw=true"/>
