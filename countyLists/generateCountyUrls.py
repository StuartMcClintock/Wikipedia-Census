# import urllib
import os

ENDPOINT_BASE = 'https://api.wikimedia.org/core/v1/wikipedia/en/page/'
RAW_DIR = './raw'
PROCESSED_DIR = './processed/'

def getRegionType(stateName):
    if stateName == 'Louisiana':
        return 'Parish'
    if stateName == 'Alaska':
        return ''
    return 'County'

def main():
    for filename in os.listdir(RAW_DIR):
        stateName = filename.split('.')[0]
        print(stateName)
        filePath = os.path.join(RAW_DIR, filename)
        pages = []
        if os.path.isfile(filePath):
            try:
                with open(filePath, "r", encoding="utf-8") as inFile:
                    for line in inFile:
                        pages.append(line.strip().replace(' ', '_').replace("'", '%27')+'_'+getRegionType(stateName)+',_'+stateName)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
        with open(PROCESSED_DIR+stateName+'.txt', 'w') as outFile:
            for page in pages:
                outFile.write(ENDPOINT_BASE+page+'\n')
        print('complete\n')


if __name__ == '__main__':
    main()
