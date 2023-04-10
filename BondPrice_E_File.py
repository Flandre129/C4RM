


yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
m = 5

def getBondPrice_E(face,couponRate,m,yc):
 cf=face*couponRate
 pvcf=0
 for i,y in enumerate(yc):
   pv=(1+y)**(-(i+1))
   pvcf+=cf*pv
   bondPrice=pvcf+face*((1+yc[-1])**(-m))
 return bondPrice

bondPrice=getBondPrice_E(face,couponRate,m,yc)
print(bondPrice)