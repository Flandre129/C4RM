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
