import mysql.connector
conn = mysql.connector.connect(user='root', password='8267836785', host='127.0.0.1', database='sys')


import os
import xml.etree.ElementTree as ET


from xml.dom import minidom


path = "/Users/tansudoruk/Desktop/treebank_merged_corrections_feb_2008/treebank_files"
listFileName=os.listdir(path)

cur = conn.cursor(buffered=True)


for filename in listFileName:
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)
        xmldoc = minidom.parse(fullname)
        itemlist = xmldoc.getElementsByTagName("S")
        for s in itemlist:
            W=s.getElementsByTagName('W')
            for w in W:
                try:



                    try:
                        ORG_IG1=w.attributes['ORG_IG1'].value

                    except:
                        ORG_IG1="NULL"



                    try:
                        ORG_IG2=w.attributes['ORG_IG2'].value

                    except:
                        ORG_IG2="NULL"

                    try:
                        ORG_IG3=w.attributes['ORG_IG3'].value

                    except:
                        ORG_IG3="NULL"

                    try:
                        ORG_IG4=w.attributes['ORG_IG4'].value

                    except:
                        ORG_IG4="NULL"

                    try:
                        ORG_IG5=w.attributes['ORG_IG5'].value

                    except:
                        ORG_IG5="NULL"

                    try:
                        ORG_IG6=w.attributes['ORG_IG6'].value

                    except:
                        ORG_IG6="NULL"

                    try:
                        ORG_IG7=w.attributes['ORG_IG7'].value

                    except:
                        ORG_IG7="NULL"

                    try:
                        ORG_IG8=w.attributes['ORG_IG8'].value


                    except:
                        ORG_IG8="NULL"

                    try:
                        ORG_IG9=w.attributes['ORG_IG9'].value


                    except:
                        ORG_IG9="NULL"


                    try:
                        ORG_IG10=w.attributes['ORG_IG10'].value

                    except:
                        ORG_IG10="NULL"




                    cur.execute('''INSERT into nlp_database (FILE_NAME, No, IX, LEM, MORPH, IG, REL,
                    ORG_IG1,ORG_IG2,ORG_IG3,ORG_IG4,ORG_IG5,ORG_IG6,ORG_IG7,ORG_IG8,
                    ORG_IG9,ORG_IG10, WORD) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                    (filename,s.attributes['No'].value, w.attributes['IX'].value,w.attributes['LEM'].value,w.attributes['MORPH'].value,
                    w.attributes['IG'].value,w.attributes['REL'].value,ORG_IG1,ORG_IG2,ORG_IG3,
                     ORG_IG4,ORG_IG5,ORG_IG6,ORG_IG7,ORG_IG8,ORG_IG9,ORG_IG10,w.childNodes[0].data))






                    conn.commit()
                except:
                    conn.rollback()

conn.close()

