import re


def expraw(file_name):
    expfile = open(file_name)
    lines = str(expfile.read())
    alleneity = []
    templist = lines.split("END_ENTITY;")
    firstentity = "ENTITY " + templist[0].split("ENTITY")[1].strip()
    alleneity.append(firstentity)
    templist.pop()
    templist.pop(0)
    for i in templist:
        alleneity.append(i.strip())
    # print(len(alleneity))
    # print(alleneity[-1])
    ifctypelist = []
    ifcattributelist = []
    ifcsuptypelist = []

    for i in alleneity:
        entity = re.findall(r"ENTITY\s[a-zA-Z0-9]*",i)
        ifctype = str(entity).replace("ENTITY ", "").replace("['","").replace("']","")
        # print("ifctype:", ifctype)
        ifctypelist.append(ifctype)

        suptype = str(re.findall(r"SUBTYPE\sOF\s\([a-zA-Z]*\);",i)).replace("SUBTYPE OF (","").replace(");'","").replace("'","").replace("]","").replace("[","")
        if suptype == "":
            suptype = None
        # print(suptype)
        ifcsuptypelist.append(suptype)

        l = i.split("WHERE")[0].split("INVERSE")[0].split("UNIQUE")[0].split("DERIVE")[0].split(";")
        l.pop(0)
        l.pop()
        attribute_list = []
        for j in l:
            attribute_list.append(j.split(":")[0].strip())
        # print("attribute:",attribute_list)
        ifcattributelist.append(attribute_list)

    return ifctypelist, ifcsuptypelist, ifcattributelist


def getattributenameraw(ifctype,ifcschema):
    ifctypelist, ifcsuptypelist, ifcattributelist = expraw(ifcschema)
    for index, types in enumerate(ifctypelist):
        if ifctype.lower() == types.lower():
            # print(types)
            return ifcsuptypelist[index], ifcattributelist[index]


def getattributename(ifctype,ifcschema):
    attibutelist = []
    ifcsuptype, ifcattribute = getattributenameraw(ifctype, ifcschema)
    while True:
        attibutelist.append(ifcattribute)
        if ifcsuptype == None:
            break
        ifcsuptype, ifcattribute = getattributenameraw(ifcsuptype, ifcschema)
    attibutelist.reverse()
    attibutelist = [x for x in attibutelist if x != []]
    attibutelistfinal = []
    for i in attibutelist:
        for j in i:
            attibutelistfinal.append(j)
    return attibutelistfinal

