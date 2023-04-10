def getBondPrice_Z(face,couponRate,times,yc):
  cf=face*couponRate
  pvcf=0
  for t,y in zip(times,yc):
    pv=(1+y)**(-t)
    pvcf+=cf*pv
    bondPrice=pvcf+face*(1+yc[-1])**(-times[-1])
  return bondPrice
