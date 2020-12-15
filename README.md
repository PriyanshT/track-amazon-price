# Track the price of Amazon Product!
## Let's create a python application for windows to track the book `A Song of Ice and Fire`

To get started, we need to have pip installed for windows.<br>

Open Command Prompt and type the following:<br>
`pip install requests bs4`
<br>

Here, I am going to keep the track of price for <a href="https://www.amazon.in/Song-Ice-Fire-Thrones-Complete/dp/0007477155/ref=sr_1_1?crid=3ILLV1VL7EKH8&keywords=a+song+of+ice+and+fire&qid=1568283272&s=gateway&sprefix=a+song%2Caps%2C278&sr=8-1" target="_blank">this</a> item<br>

The code will check everyday for the product price.<br>
It will send the mail if one of the following thing about price is satisfied:<br>
- Price remain unchanged
- Price Increase
- Price Decrease <br>

<img src="https://github.com/PriyanshT/track-amazon-price/blob/master/mail.jpg">

If the project is to be kept working in the background, executable file is to be generated.<br>
To do that:<br>
`pip install pyinstaller`<br>
then,
`pyinstaller --onefile filename.py`, in my example: `pyinstaller --onefile track1.py`<br>
Do the above step in the folder in which the .exe file is to be created.<br>
After completion, one can find the executable file in `disc` folder.
