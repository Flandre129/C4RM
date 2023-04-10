def getBondPrice_E(face,couponRate,yc):
 cf=face*couponRate
 pvcf=0
 for i,y in enumerate(yc):
   pv=(1+y)**(-(i+1))
   pvcf+=cf*pv
   bondPrice=face*pv+pvcf
 return bondPrice
