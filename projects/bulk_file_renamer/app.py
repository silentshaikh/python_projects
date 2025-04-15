import os

def fileRenamer():
    
    filePath = "C:/Users/hp/Desktop/python_assignment/projects/bulk_file_renamer/images/"
    for fileName in os.listdir(filePath):
        myDest = f"imgWorld.jpg"
        mySource = filePath + fileName
        myDest = filePath + myDest
        os.rename(mySource,myDest)
        


fileRenamer()
