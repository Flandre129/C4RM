


yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = 0.04

def getBondPrice_Z(face,couponRate,times,yc):
  cf=face*couponRate
  pvcf=0
  for t,y in zip(times,yc):
    pv=(1+y)**(-t)
    pvcf+=cf*pv
    bondPrice=pvcf+face*(1+yc[-1])**(-times[-1])
  return bondPrice

bondPrice=getBondPrice_Z(face,couponRate,times,yc)
print(bondPrice)
