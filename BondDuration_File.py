
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

def getBondDuration(y,face,couponRate,m,ppy=1):
  cf=face*couponRate
  pvcf=0
  pvcft=0
  for i in range(1,m+1):
   pvcf += cf*((1+y)**(-i))
   pvcft += i*cf*((1+y)**(-i))
   pvcfsum = pvcf+face*((1+y)**(-m))
   pvcftotal = pvcft+face*m*((1+y)**(-m))
   bondDuration = pvcftotal/pvcfsum
  return bondDuration

bondDuration=getBondDuration(y,face,couponRate,m,ppy=1)
print(bondDuration)