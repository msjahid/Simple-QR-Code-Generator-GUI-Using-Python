# Simple QR Code Generator GUI APP 

It's a simple application for generating web Link to QR codes. 

## Getting Started

To start, clone the present repository into your local machine. If you're unaware of how to achieve this, you can familiarise yourself with the mechanisms of GitHub repositories in the provided link.

```
git clone git@github.com:msjahid/Simple-QR-Code-Generator-GUI-Using-Python.git
```
### Prerequisites
Ensure that you have [Python3](https://www.python.org/download/releases/3.0/), and [tkinter](https://docs.python.org/3/library/tkinter.html) installed and properly set up. 

#### Installing Python Package

We need Install some python pip packages. 

```bash
qrcode==6.1
Pillow==7.2.0
```

#### Pip install Instructions

Start by opening a terminal, and navigate to the project's folder.

```python
pip install -r requirements.txt 
|or| 
pip3 install -r requirements.txt
```
### Run App

```
python qrcode.py
```
![Screenshot_20200716_002838](https://user-images.githubusercontent.com/12425488/87582060-ad9c1600-c6fb-11ea-81de-844d3946ce24.png)

Now add your desire link in Link field. Suppose, We are gonna add 'https://www.kaggle.com/c/titanic' this link. 

## Is it Working? 

Now we are gonna test qcode.png file. Go to https://online-barcode-reader.inliteresearch.com/ and then upload qcode.png file.

![Screencast-2020-07-16-01-11-13-o](https://user-images.githubusercontent.com/12425488/87586247-14243280-c702-11ea-8f44-580eb40bbdf6.gif)

Hurrah! It's working :D 

## License

This project is originally licensed under the MIT License - see the [LICENSE.md](https://github.com/msjahid/Simple-QR-Code-Generator-GUI-Using-Python/blob/master/LICENSE) file for details. 

**Notice**: This forked version and all future contributions by [Daemon](https://github.com/daethyra) are licensed under the Affero General Public License (AGPL). See the [LICENSE-AGPL](https://github.com/daethyra/Simple-QR-Code-Generator-GUI-Using-Python/blob/master/LICENSE-AGPL) file for details.

## Authors

* **Jahid Hasan** - [msjahid](https://github.com/msjahid)
* Forked/Modified by - **Daemon** - [daethyra](https://github.com/daethyra)

For any inquiries, feel free to open up an issue.
