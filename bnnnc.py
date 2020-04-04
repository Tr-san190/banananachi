#!/usr/bin/python
# -*- Coding: utf-8 -*-

import sys
from os import path

# バナナナチ ........  >  ...  p++;
# バナチ ...........  <  ...  p--;
# バナナチ  ........  +  ...  (*p)++;
# バナナナナナチ .....  -  ...  (*p)--;
# バナナのナナチは ...  .  ...  putchar(*p);
# ナナチのバナナは ...  ,  ...  *p = getchar();
# バナナのバナナは ...  [  ...  while(*p){
# ナナチのナナチは ...  ]  ...  }

def bnnnc2bfConverter(bnnncCode):
  bfCode = bnnncCode.replace("\n", "")
  bfCode = bfCode.replace("バナナナチ",     ">")
  bfCode = bfCode.replace("バナチ",        "<")
  bfCode = bfCode.replace("バナナチ",      "+")
  bfCode = bfCode.replace("バナナナナナチ",  "-")
  bfCode = bfCode.replace("バナナのナナチは", ".")
  bfCode = bfCode.replace("ナナチのバナナは", ",")
  bfCode = bfCode.replace("バナナのバナナは", "[")
  bfCode = bfCode.replace("ナナチのナナチは", "]")
  return bfCode

def bf2bnnncConverter(bfCode):
  bnnncCode = bfCode.replace("\n", "")
  bnnncCode = bnnncCode.replace(">", "バナナナチ")
  bnnncCode = bnnncCode.replace("<", "バナチ")
  bnnncCode = bnnncCode.replace("+", "バナナチ")
  bnnncCode = bnnncCode.replace("-", "バナナナナナチ")
  bnnncCode = bnnncCode.replace(".", "バナナのナナチは")
  bnnncCode = bnnncCode.replace(",", "ナナチのバナナは")
  bnnncCode = bnnncCode.replace("[", "バナナのバナナは")
  bnnncCode = bnnncCode.replace("]", "ナナチのナナチは")
  return bnnncCode

def testBnnnc():
  print("Test for bnnnc\n")
  print("----------------------------")
  print("Case 1")
  print("----------------------------\n")

  srcFilePath = "test.bnnnc"
  f = open(srcFilePath, "r")
  src = f.read()
  f.close()

  src = src.replace("\n", "")

  bf = bnnnc2bfConverter(src)
  bnnnc = bf2bnnncConverter(bf)

  print("Input :")
  print(src)
  print("")
  print("Output :")
  print(bnnnc)
  print("")
  print("Comparison :")
  print(bnnnc == src)
  print("")

  print("----------------------------")
  print("Case 2")
  print("----------------------------\n")

  srcFilePath = "test.bf"
  f = open(srcFilePath, "r")
  src = f.read()
  f.close()

  src = src.replace("\n", "")

  bnnnc = bf2bnnncConverter(src)
  bf = bnnnc2bfConverter(bnnnc)

  print("Input :")
  print(src)
  print("")
  print("Output :")
  print(bf)
  print("")
  print("Comparison :")
  print(bf == src)
  print("")

if __name__ == '__main__':
  if len(sys.argv) >= 2:
    srcFilePath = sys.argv[1];

    srcFileExt = path.splitext(path.basename(srcFilePath))
    if len(srcFileExt) == 2:
      srcFileExt = srcFileExt[1]
    else:
      srcFileExt = ""

    f = open(srcFilePath, "r")
    src = f.read()
    f.close()

    if srcFileExt == ".bnnnc":
      bf = bnnnc2bfConverter(src)
      print(bf)
    elif srcFileExt == ".bf":
      bnnnc = bf2bnnncConverter(src)
      print(bnnnc)
    else:
      print("Invalid src file.")

  else:
    testBnnnc()
