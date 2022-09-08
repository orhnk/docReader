import easyocr
import cv2 as cv
import keyboard as kb
import pdfplumber as pb

global searchData

content = []


print("""Attributes:
- type 'path' to enter new file path
- type 'quit' to quit
- press q to close popup image menu
- while searching an image press space to search for any word""")
while True:
    path = input("please enter a path: ")
    if path == "quit":
        quit()
    if path[-1:] == "'" or path[-1:] == ' ':
        if path[0] == "'" or path[0] == ' ':
            path = path[1:]
        path = path[:-1]
        path.replace("'", "")
        print(path)
    if path[-4:] == ".txt" or path[-4:] == ".cpp" or path[-3:] == ".rs" or path[-3:] == ".py" or path[-3:] == ".js" or path[-2:] == ".c" or path[-3:] == ".sh":
        try:
            with open(path) as f:
                raw = f.read()
                data = raw.replace("?", " ")
                data = data.replace("\"", " ")
                data = data.replace("\\", " ")
                data = data.replace("'", " ")
                data = data.replace(")", " ")
                data = data.replace("(", " ")
                data = data.replace("{", " ")
                data = data.replace("}", " ")
                data = data.replace("/", " ")
                data = data.replace(".", " ")
                data = data.replace("<", " ")
                data = data.replace(">", " ")
                data = data.replace("*", " ")
                data = data.replace("+", " ")
                data = data.replace(",", " ")
                data = data.replace(";", " ")
                data = data.replace("~", " ")
                data = data.replace(":", " ")
                data = data.replace("=", " ")
                data = data.replace("#", " ")
                data = data.replace("\"", " ")
                data = data.replace("\r\n", " ")
                done = data.replace("\n", " ")
                ds = done.split()
                while True:
                    response = input("Search: ")
                    for i in ds:
                        if response == i:
                            print(f"{i} Found!")
                            break
                    if response.lower() == "quit":
                            quit()
                    if response.lower() == "path":
                            break

        except Exception as e:
            print(e)

    elif path[-4:] == ".pdf":
        try:
            with pb.open(path) as f:
                for i in f.pages:
                    i = i.extract_text()
        except Exception as e:
            print(e)
            print("cannot open the file!")
        #Speacial Char filter:
        data = i.replace("?", " ")
        data = data.replace("\"", " ")
        data = data.replace("\\", " ")
        data = data.replace("'", " ")
        data = data.replace(")", " ")
        data = data.replace("(", " ")
        data = data.replace("{", " ")
        data = data.replace("}", " ")
        data = data.replace("/", " ")
        data = data.replace(".", " ")
        data = data.replace("<", " ")
        data = data.replace(">", " ")
        data = data.replace("*", " ")
        data = data.replace("+", " ")
        data = data.replace(",", " ")
        data = data.replace(";", " ")
        data = data.replace("~", " ")
        data = data.replace(":", " ")
        data = data.replace("=", " ")
        data = data.replace("#", " ")
        i = data.replace("\"", " ")
        ds = i.split()
        content.append(ds)

        while True:
            search = input("Search: ")
            for word in ds:
                if search.lower() == word.lower():
                    print("Found", search)
                    break
            if search.lower() == "quit":
                quit()
            if search.lower() == "path":
                break


    elif path[-4:] == ".png" or path[-5:] == ".jpeg" or path[-4:] == ".jpg" or path[-5:] == ".webp":
        reigionThickness = 2
        reigionColor = (23,151,46)

        try:
            img = cv.imread(path, 1)
        except Exception as e:
            print(e)
            print("Could not read the file")
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        noise = cv.medianBlur(gray,3)
        thresh = cv.threshold(noise, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
        reader = easyocr.Reader(['en'])
        result = reader.readtext(img,paragraph="True")

        print(f"Found {len(result)} topics")

        try:
            for i in result:
                cv.rectangle(img, tuple(i[0][0]), tuple(i[0][len(i[0])-2]), reigionColor, reigionThickness)

        except Exception as e:
            print(e)
            print("Could not recognize a pattern that represents a letter.")


        try:
            for i in result:
                i.remove(i[0])

        except Exception as e:
            print(e)
            print("Could not recognize a pattern that represents a letter")

        for i in result:
            searchData = i[0].split()
        print(searchData)

        while True:
            if kb.is_pressed('SPACE'):
                resp = input("Search: ")
                if resp[0] == ' ':
                    resp = resp[1:]
                if resp.lower() == "quit":
                    quit()
                if resp.lower() == "path":
                    cv.destroyAllWindows()
                    break
                for keyword in searchData:
                    if keyword.lower() == resp.lower():
                        print("Found!", keyword)
                        break

            cv.imshow("Image", img)

            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break
    else:
        print("This type of file is not supported")
