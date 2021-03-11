def by_type(ifctype, ifcfile):
    ifclist = []
    for line in ifcfile:
        if line.startswith("#") and ifctype.lower() == line.split("= ")[1].split("(")[0].lower():
            ifclist.append(line.replace("\n",""))
    return ifclist


def by_id(id, ifcfile):
    ifclist = []
    for line in ifcfile:
        if line.startswith("#") and id == int(line.split("= ")[0].strip("#")):
            ifclist.append(line.replace("\n",""))
    return ifclist


def ifcwrapper(ifcdata):
    ifclist = []
    ifcid = ifcdata.split("= ")[0].strip("#")
    ifctype = ifcdata.split("= ")[1].split("(",1)[0]
    ifcdata = ifcdata.split("(",1)[1].split(",")
    for i in ifcdata:
        ifclist.append(i.replace("'","").replace(");","").replace("$","none"))
    return ifcid, ifctype, ifclist
