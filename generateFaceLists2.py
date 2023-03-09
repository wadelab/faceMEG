import csv as csv
import glob as glob



# %% Data are in S1/E1, E2 etc
# Our job is to generate 4 csv files with headers 'Filename','InvertedFlag'
nExpts=4
fileNameBase='ExptSeq'
wordList=["happy","fear","anger","neutral"]

header=['FileName','InvertedFlag','EmotionType']
finalData=[]

for thisExpt in range(nExpts):
    thisFileList=glob.glob(f'./S1/E{thisExpt+1}/*.jpg')
    print(thisFileList)
    nIms=len(thisFileList)

    
    # Duplicate the list - we need inverted versions as well (later we will shuffle)
    thisFileList.extend(thisFileList)
    emotionType=([0]*nIms*2)

    for thisIdx,thisFile in enumerate(thisFileList):
        for thisEmotionindex,thisEmotion in enumerate(wordList):
            positionOfWord=thisFile.find(thisEmotion)
            if (positionOfWord!= -1):
                emotionType[thisIdx]=thisEmotionindex+1
                    
                    

    invertedFlagList=([0]*nIms)
    invertedFlagList.extend([1]*nIms)
    for thisIdx,thisListEntry in enumerate(thisFileList):
        finalData.extend([[thisListEntry,invertedFlagList[thisIdx],emotionType[thisIdx]]])
        

        
    
    filename = 'Students_Data.csv'
    outFile=f'ExperimentListx_{thisExpt}.csv'
 
    with open(outFile, 'w', newline="") as file:
        csvwriter = csv.writer(file) # 2. create a csvwriter object
        csvwriter.writerow(header) # 4. write the header
        csvwriter.writerows(finalData) # 5. write the rest of the data