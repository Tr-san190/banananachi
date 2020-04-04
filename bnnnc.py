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

def bnnncParser(f):
  bnnncCode = f.read()
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

def bnnncConverter(f):
  bfCode = f.read()
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

if __name__ == '__main__':
  if len(sys.argv) >= 2:
    srcFilePath = sys.argv[1];
  else:
    srcFilePath = "test.bf"

  srcFileExt = path.splitext(path.basename(srcFilePath))
  if len(srcFileExt) == 2:
    srcFileExt = srcFileExt[1]
  else:
    srcFileExt = ""
#  print(path.splitext(path.basename(srcFilePath))[0])
#  print(path.splitext(path.basename(srcFilePath))[1])
  f = open(srcFilePath, "r")

  if srcFileExt == ".bnnnc":
    bf = bnnncParser(f)
    print(bf)
  elif srcFileExt == ".bf":
    bnnnc = bnnncConverter(f)
    print(bnnnc)
