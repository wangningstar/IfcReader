# import ifcreader as ir
# from ifcschema import getattributename as ifcattributename
# import time
import pickle
#
# s = time.time()
#
# ifcfile = open("Project1.ifc")
# lines = ifcfile.readlines()
# ifcschema = "IFC4.exp"
# inputifctype = "ifcwall"
#
# irbytype = ir.by_type(inputifctype, lines)
# for i in irbytype:
#     print(i)
#
# irbyid = ir.by_id(1, lines)
# for i in irbyid:
#     print(i)
#
# ifctype, parsedata = ir.ifcwrapper(irbytype[0])
# print(ifctype)
# for i in parsedata:
#     print(i)
#
# x = ifcattributename(inputifctype, ifcschema)
# # print(len(x))
# print(x)
#
# e= time.time()
# print((e-s)*1000, "ms")
#
# from ifcschema import expraw
# from ifcschema import getattributename
# x,y,z = expraw("IFC4.exp")
# print(len(x))
# print(len(y))
# print(len(z))
# a_dic = {}
# for i in x:
#     # print("type:",i)
#     t = getattributename(i, "IFC4.exp")
#     # print("att:",t)
#     a_dic[i.upper()] = t
# #
# #
# file = open('ifc4.pickle', 'wb')
# pickle.dump(a_dic, file)
# file.close()


with open('ifc4.pickle', 'rb') as file:
    a_dict1 =pickle.load(file)
print(len(a_dict1))
print(len(a_dict1.keys()))
print(len(a_dict1.values()))
print(len(set(a_dict1)))
# for i in x:
#     print(i,a_dict1[i])
print(a_dict1["IfcWindow".upper()])
