def getBondPrice(y,face,couponRate,m,ppy):
 coupon=face*couponRate/ppy
 pvcf=0
 for i in range(1,m*ppy):
  pvcf+=coupon*((1+y/ppy)**(-i))
  pvcfsum=coupon*((1+y/ppy)**(-m*ppy))+face*((1+y/ppy)**(-m*ppy))
  bondPrice=pvcf+pvcfsum
 return bondPrice
