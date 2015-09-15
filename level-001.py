import string

def unencrypt(str):
  f = 'abcedfghijklmnopqrstuvwxyz'
  t = 'cdefghijklmnopqrstuvwxyzab'
  table = string.maketrans(f, t)
  return string.translate(str, table)
  
enc_text = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'

print unencrypt(enc_text)

print unencrypt('map')


# the output:
# i hope you didnt translate it by hand. thats what computers are for.doing it in by hand is inefficient and that’s why this text is so long.using string.maketrans() is recommended. now apply on the url.
# ocr

# use 'ocr' to replace 'map' in the url and you get into the next level.
