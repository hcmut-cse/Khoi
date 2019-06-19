import pdftotext
import json
import os
import re

# import pdb
# pdb.set_trace()

PDF_TYPE = "VN102347"
CURR_CONFIG = {}

'''with open(PDF_TYPE + '/' + PDF_TYPE + '.json', 'r', encoding='utf8') as json_file:'''
'''CONFIG = json.load(json_file)'''
CONFIG = {
        "SHIPPER / EXPORT": {
            "row": [2, 6],
            "column": [0, 106],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "SHIPPER / EXPORT",
                "bottom": "CONSIGNEE1",
                "left": -1,
                "right": "B/L NO"
            }
        },
        
        "CONSIGNEE1": {
            "row": [7, 13],
            "column": [1, 106],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "CONSIGNEE1",
                "bottom": "NOTIFY PARTY",
                "left": -1,
                "right": "FREIGHT PAYABLE AT"
            }
        },
        "NOTIFY PARTY": {
            "row": [14, 18],
            "column": [16, 106],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,
            
            "endObject": {
                "top": "NOTIFY PARTY",
                "bottom": "PRE-CARRIAGE BY",
                "left": -1,
                "right": "ALSO NOTIFY"
            }
        },
        "B/L NO": {
            "row": [2, 4],
            "column": [107, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "B/L NO",
                "bottom": "EXPORT REFERENCES",
                "left": "SHIPPER/EXPORT",
                "right": -1
            }
        },
        "EXPORT REFERENCES": {
            "row": [5, 6],
            "column": [107, null],
            "isFlex": 1,


            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "EXPORT REFERENCES",
                "bottom": "FREIGHT PAYABLE AT",
                "left": -1,
                "right": -1
            }
        },
        "FREIGHT PAYABLE AT": {
            "row": [7, 8],
            "column": [107, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "FREIGHT PAYABLE AT",
                "bottom": "TYE OF SERVICE",
                "left": "CONSIGNEE1",
                "right": -1
            }
        },
        "TYE OF SERVICE": {
            "row": [9, 11],
            "column": [107, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "TYE OF SERVICE",
                "bottom": "CONTAINER NO",
                "left": "CONSIGNEE1",
                "right": -1
            }
        },
        "CONTAINER NO": {
            "row": [11, 12],
            "column": [136, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "CONTAINER NO",
                "bottom": "ALSO NOTIFY",
                "left": "CONSIGNEE",
                "right": -1
            }
        },
        "ALSO NOTIFY": {
            "row": [15, 19],
            "column": [107, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "ALSO NOTIFY",
                "bottom": "NUMBER ORIGINAL BILL OF LADING ISSUED",
                "left": "NOTIFY PARTY",
                "right": -1
            }
        },
        "NUMBER ORIGINAL BILL OF LADING ISSUED": {
            "row": [20, 24],
            "column": [107, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "NUMBER ORIGINAL BILL OF LADING ISSUED",
                "bottom": "DESCRIPTION OF PACKGES AND GOODS",
                "left": "PORT OF LOADING",
                "right": -1
            }
        },
        "PRE-CARRIAGE BY": {
            "row": [18, 19],
            "column": [15, 51],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "PRE-CARRIAGE BY",
                "bottom": "OCEAN VESSEL / VOYAGE",
                "left": -1,
                "right": "PLACE OF RECEIPT"
            }
        },
        "OCEAN VESSEL / VOYAGE": {
            "row": [20, 21],
            "column": [2, 51],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "OCEAN VESSEL / VOYAGE",
                "bottom": "PORT OF DISCHARGE",
                "left": -1,
                "right": "PORT OF LOADING"
            }
        },
        "PORT OF DISCHARGE": {
            "row": [22, 24],
            "column": [6, 51],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "PORT OF DISCHARGE",
                "bottom": "MARKS AND NUMBERS",
                "left": -1,
                "right": "PLACE OF DELIVERY"
            }
        },
        "PLACE OF RECEIPT": {
            "row": [18, 19],
            "column": [69, 106],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "PLACE OF RECEIPT",
                "bottom": "PORT OF LOADING",
                "left": "PRE-CARRIAGE BY",
                "right": "ALSO NOTIFY"
            }
        },
        "PORT OF LOADING": {
            "row": [20, 21],
            "column": [52, 106],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "PORT OF LOADING",
                "bottom": "PLACE OF DELIVERY",
                "left": "OCEAN VESSEL / VOYAGE",
                "right": "NUMBER ORIGINAL BILL OF LADING ISSUED"
            }
        },
        "PLACE OF DELIVERY": {
            "row": [22, 24],
            "column": [62, 106],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "PLACE OF DELIVERY",
                "bottom": "NO.OF CONT",
                "left": "PORT OF DISCHARGE",
                "right": "NUMBER ORIGINAL BILL OF LADING ISSUED"
            }
        },
        "MARKS AND NUMBERS": {
            "row": [25, 41],
            "column": [2, 56],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "MARKS AND NUMBERS",
                "bottom": "SHIPPED ONBOARD THE VESSEL",
                "left": -1,
                "right": "NO.OF CONT"
            }
        },
        "NO.OF CONT": {
            "row": [25, 41],
            "column": [57,83],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "NO.OF CONT",
                "bottom": "SHIPPED ONBOARD THE VESSEL",
                "left": "MARKS AND NUMBERS",
                "right": "DESCRIPTION OF PACKGES AND GOODS"
            }
        },
        "DESCRIPTION OF PACKGES AND GOODS": {
            "row": [25, 41],
            "column": [84, 152],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "DESCRIPTION OF PACKGES AND GOODS",
                "bottom": "SHIPPED ONBOARD THE VESSEL",
                "left": "NO.OF CONT",
                "right": "GROSS WEIGHT1"
            }
        },
        "GROSS WEIGHT1": {
            "row": [25, 41],
            "column": [153, 176],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "GROSS WEIGHT1",
                "bottom": "SHIPPED ONBOARD THE VESSEL",
                "left": "DESCRIPTION OF PACKGES AND GOODS",
                "right": "MEASUREMENT"
            }
        },
        "MEASUREMENT": {
            "row": [25, 41],
            "column": [177, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "MEASUREMENT",
                "bottom": "SHIPPED ONBOARD THE VESSEL",
                "left": "GROSS WEIGHT1",
                "right": -1
            }
        },
        "SIGNED AT": {
            "row": [42, 43],
            "column": [13, 60],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "SHIPPED ONBOARD THE VESSEL",
                "bottom": "SIGNED AT",
                "left": -1,
                "right": "DATE"
            }
        },
        "DATE": {
            "row": [42, 43],
            "column": [66, 95],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "SHIPPED ONBOARD THE VESSEL",
                "bottom": "DATE",
                "left": -1,
                "right": -1
            }
        },
        
        "FREIGHT AND CHARES": {
            "row": [47, null],
            "column": [0, 33],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "FREIGHT AND CHARES",
                "bottom": -1,
                "left": -1,
                "right": "PREPAID"
            }
        },
        "PREPAID": {
            "row": [47, null],
            "column": [34, 65],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "PREPAID",
                "bottom": -1,
                "left": "FREIGHT AND CHARES",
                "right": "COLLECT"
            }
        },
        "COLLECT": {
            "row": [47, null],
            "column": [66, 95],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "PREPAID",
                "bottom": -1,
                "left": "FREIGHT AND CHARES",
                "right": -1
            }
        },
        "SHIPPED ONBOARD THE VESSEL": {
            "row": [42, 44],
            "column": [96, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 0,
            "hasSubfield": 0,

            "endObject": {
                "top": "SHIPPED ONBOARD THE VESSEL",
                "bottom": -1,
                "left": -1,
                "right": -1
            }
        },
        "A": {
            "row": [44, null],
            "column": [96, null],
            "isFlex": 1,

            "sameLineWithKeyword": 0,
            "singleLine": 1,
            "hasSubfield": 0,

            "endObject": {
                "top": "COLLECT",
                "bottom": -1,
                "left": "COLLECT",
                "right": -1
            }
        }
}
KEYWORD = ['SHIPPER / EXPORT', 'CONSIGNEE', 'NOTIFY PARTY', 'B/L NO', 'EXPORT REFERENCES', 'FREIGHT PAYABLE AT', 'TYE OF SERVICE', 'CONTAINER NO',
            'ALSO NOTIFY', 'NUMBER ORIGINAL BILL OF LADING ISSUED', 'PRE-CARRIAGE BY', 'OCEAN VESSEL / VOYAGE', 'PORT OF DISCHARGE', 'PLACE OF RECEIPT',
            'PORT OF LOADING', 'PLACE OF DELIVERY', 'MARKS AND NUMBERS', 'NO.OF CONT', 'DESCRIPTION OF PACKGES AND GOODS', 'GROSS WEIGHT',
            'MEASUREMENT', 'SIGNED AT', 'DATE', 'FREIGHT AND CHARES', 'PREPAID', 'COLLECT', 'SHIPPED ONBOARD THE VESSEL', 'A']

fileName = list(filter(lambda pdf: pdf[-3:] == 'pdf' ,os.listdir(PDF_TYPE)))
# fileName = ["SI_HANV08177300.pdf"]

if __name__ == '__main__':
    for file in fileName:
        # Reset Current CONFIG
        print('====================',file,'====================')
        CURR_CONFIG = {}

        # Load PDF
        with open(PDF_TYPE + '/' + file, "rb") as f:
            pdf = pdftotext.PDF(f)

        page=pdf[0].split('\n')

        for page in pdf:
            lineList=page.split('\n')

        length=len(lineList)

        kwpos_temp={}
        for key in KEYWORD:
            found=[]
            for r in range(length):
                if (lineList[r].find(key)!=-1):
                    found.append([r,lineList[r].find(key)])
            kwpos_temp[key]=found

        
        kwpos={}
        
        for key in KEYWORD:
            l=len(kwpos_temp[key])
            pos=key.rfind('  ')
            if (pos!=-1): newKey=key[:pos] 
            else: newKey=key
            if (l!=1):
                for i in range(l): kwpos[newKey+str(i+1)]=kwpos_temp[key][i]
            else:
                kwpos[newKey]=kwpos_temp[key][0]
    	
        for key in CONFIG:
            haskey = False
            for kw in kwpos:
                if (key == kw):
                  haskey = True
            if not haskey:
                row = CONFIG[key]['row'][1]
                col = CONFIG[key]['column'][0]
                found = [row, col]
                kwpos[key] = found

        for key in CONFIG:
            if (CONFIG[key]['isFlex']): 
                top=CONFIG[key]['endObject']['top']
                bot=CONFIG[key]['endObject']['bottom']
                toprow=-1
                botrow=-1
                minDistance=100000
                for kw in kwpos:
                    # print('In the loop key and kw',key,kw)
                    if (top==kw and abs(kwpos[kw][0]-kwpos[key][0])<minDistance): 
                        minDistance=abs(kwpos[kw][0]-kwpos[key][0])
                        toprow=kwpos[kw][0]
                minDistance=100000
                for kw in kwpos:
                    if (bot==kw and abs(kwpos[kw][0]-kwpos[key][0])<minDistance): 
                        minDistance=abs(kwpos[kw][0]-kwpos[key][0])
                        botrow=kwpos[kw][0]
                # print(key)
                if (top!=-1): CONFIG[key]['row'][0]=max(CONFIG[key]['row'][0],toprow+1)
                if (bot!=-1): CONFIG[key]['row'][1]=max(CONFIG[key]['row'][1],botrow)


        for key in CONFIG:
            if (CONFIG[key]['isFlex']): 
                left=CONFIG[key]['endObject']['left']
                right=CONFIG[key]['endObject']['right']
                leftColumn=-1
                rightColumn=-1
                if (left!=-1):
                    for kw in kwpos:
                        # print('In the loop key and kw',key,kw)
                        if (left==kw and (kwpos[kw][0]-kwpos[key][0]==0)): 
                            leftColumn=kwpos[kw][0]
                            break
                if (right!=-1):
                    for kw in kwpos:
                        if (right==kw and (kwpos[kw][0]-kwpos[key][0]==0)): 
                            rightColumn=kwpos[kw][0]
                            break
                # print(key)
                if (left!=-1): CONFIG[key]['column'][0]=min(CONFIG[key]['column'][0],leftColumn)
                if (right!=-1): CONFIG[key]['column'][1]=max(CONFIG[key]['row'][1],rightColumn)
        data={}
        for key in CONFIG:
            row=CONFIG[key]['row']
            column=CONFIG[key]['column']
            lines=lineList[row[0]:row[1]]
            data[key]='\n'.join([x[column[0]:column[1]] for x in lines])

        for key in CONFIG:
            if ('subfields' in CONFIG):
                pos=0
                for subfield in CONFIG[key]['subfields']:
                    if CONFIG[key]['subfields'][subfield]!=10: 
                        result=re.search(CONFIG[key]['subfields'][subfield],data[key]).span()
                        data[key+'_'+subfield]=data[key][result[0]:result[1]+1]
                        pos=result[1]
                    else:
                        data[key+subfield]=data[key][pos:]
                del data[key]

        for key in data:
            data_pros=data[key]
            data_pros=data_pros.strip()
            data_pros=re.sub('\n+','\n',data_pros)
            data_pros=re.sub('\n\s+','\n',data_pros)
            print('%s:\n%s' % (key,data_pros))