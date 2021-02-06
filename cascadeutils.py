import os

def generate_negative_description_file():
    #open the output file for writing . will overwrite all existing data in store
    with open("neg.txt", 'w') as f:
        #loop over all the filenames
        for filename in os.listdir("PotholeData/PlainRoad"):
            f.write('PotholeData/PlainRoad/' + filename + '\n')

generate_negative_description_file()
#E:/Vedant/Projectdocs/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=posMedium.txt --images=PotholeData/PotholeRoad/Medium/
#E:/Vedant/Projectdocs/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 20 -h 20 -num 2000 -vec pos.vec
#E:/Vedant/Projectdocs/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 20 -h 20 -numPos 1000 -numNeg 500 -numStages 10