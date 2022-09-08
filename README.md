**Installation**
open terminal
`git clone https://github.com/KoBruhh/docReader.git`
`pip install -r requirements.txt`


**Supported fileTypes:**

**.png .jpeg .jpg .pdf .py .rs .c .cpp .js .txt .sh**

**Main goal is simply searching words inside big files in a variety file types(Including image files)**


**There are two different programs in this repo:**

**-Python:**
Simply go inside of the python dir with `cd Python`

and then, if you type `ls` you are gonna see some example images to try with and also `main.py` which is code to execute

Type:
  `python main.py` to execute the program

  drag a folder to terminal or type it manually
  
  enter a word to search
  
  if program finds any word that you gave, It will print `<Your word> Found!`

**-Javascript**
I used Javascript/html/css to create a simple website to make things a bit fancier.
But there is a catch that I could not make python and javascript communicate so GUI verion only works with text files!
To run javascript code:
  
  go to directory's main folder and go inside to the `GUI (JS)` folder by `cd GUI\ \(JS\)/`
  
  type `pwd` and copy the result
  
  open any browser and paste it to search engine (on top)
  and add `index.html` to the end of it
  
  You should see something like this:![Screenshot_Document Reader — Mozilla Firefox_1](https://user-images.githubusercontent.com/101834410/189137405-b1ae45e3-e6bd-465c-85ac-7515f247ddfe.png)
  
  Here You have to drag your file into the dashed box OR click anywhere inside the dashed box and select a file you want (Has to be text file to work!)     type a word to search inside of the mini textbox (on the upper left side of right black box) 
  press enter to activate the search and You will get response via right black box

**Cons**
-It is pretty ugly (JS):
  I have almost no experience with html and js so the website sucks.

-Pretty Unefficient (PY):
  Python is so slow to use it in a search engine but using OCR like (ML related stuff) things are written for python.
  
**Things That I Could not Achieve:**

-I could not use multiple languages together. So I made different Js and Py versions.
