![Version App](https://img.shields.io/pypi/v/1?color=blue&label=LNJ%20Downloader%20YT&style=for-the-badge)

<h1 >LNJ Downloader YT</h1>
<div >
    <img  src='./images/app.png' width=400 >
</div>
<div  >
    <h2>Downloader MP4 & MP3 from LNJ</h2>
    <p>The application allows you to add in multiple Youtube links and download both video and audio, mp4 and mp3 respectively.</p>
    
</div>

---

## Technologies

<img src="./images/Python.png" alt="Python logo" width=100>

### **Python** 

- tkinter,
- pytube, 
- moviepy, 
- threading,
- webbrowser,
- sys,
- os

## [Dependencies](./requeriments.txt)

```bash
pip freeze > requeriments.txt
```
## [Executable](./output/LNJ_Downloader_YT.exe)

You can download the exe in the output folder, script packaged with pyinstaller.

```bash
pip install pyinstaller
# simple configuration
pyinstaller --onefile LNJ_Downloader_YT.py

# works with pyinstaller, but has a graphical interface
pip install auto-py-to-exe
auto-py-to-exe
```
> https://github.com/brentvollebregt/auto-py-to-exe

Relative paths for the images, so pyinstaller can pack them.
_MEIPASS lets us know whether we are in development or not

```python
def resolver_ruta(ruta_relativa):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath("."), ruta_relativa)
```
Solution for the executable with pyinstaller,
since moviepy required an output and needed the console.
This would be like an application log

```python
output = open("output.txt", "wt")
sys.stdout = output
sys.stderr = output
```

You can also clone this repository and run the script:

```bash
phyton .\LNJ_Downloader_YT.py
```

---

<small>
    Important Notice: When using our application, please remember that downloading YouTube content may infringe upon copyright laws and the rights of content creators. We strongly advise responsible and legal usage of downloaded content, ensuring compliance with YouTube's terms of use. Users are solely responsible for their actions, and our application and team cannot be held liable for any misuse or illegal use of downloaded content. Please utilize our application ethically, respecting copyright laws and usage policies.
</small>

<small><a href="https://lanuevajerusalenamorysalvacion.com">https://lanuevajerusalenamorysalvacion.com</a></small>