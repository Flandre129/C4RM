

y = 0.03
face = 2000000
couponRate = 0.04
m = 10


def getBondPrice(y,face,couponRate,m,ppy):
 coupon=face*couponRate/ppy
 pvcf=0
 for i in range(1,m*ppy):
  pvcf+=coupon*((1+y/ppy)**(-i))
  pvcfsum=coupon*((1+y/ppy)**(-m*ppy))+face*((1+y/ppy)**(-m*ppy))
  bondPrice=pvcf+pvcfsum
 return bondPrice

bondPrice1=getBondPrice(y,face,couponRate,m,ppy=1)
print(bondPrice1)
bondPrice2=getBondPrice(y,face,couponRate,m,ppy=2)
print(bondPrice2)