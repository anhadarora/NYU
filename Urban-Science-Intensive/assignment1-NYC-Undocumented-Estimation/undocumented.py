import pandas as pd
import csv

content = pd.read_csv('Undocumented_Census_scale_all_State.csv')
content1 = pd.read_csv('Population_By_CTrack.csv')
zipcode = content['GEO.id2']
popu = content1['Naturalized U.S. citizen']
zipcode1 = content1['GEO.id2']
mpopulation = content['HD01_VD137']
spopulation = content['HD01_VD140']
gpopulation = content['HD01_VD141']
hpopulation = content['HD01_VD142']
cpopulation = content['HD01_VD48']
ppopulation = content['HD01_VD72']
ipopulation = content['HD01_VD58']
kpopulation = content['HD01_VD53']
epopulation = content['HD01_VD152']
vpopulation = content['HD01_VD75']
dpopulation = content['HD01_VD128']
npopulation = content['HD01_VD61']
copopulation = content['HD01_VD151']

moutput = []
soutput = []
goutput = []
houtput = []
coutput = []
poutput = []
ioutput = []
koutput = []
eoutput = []
voutput = []
doutput = []
noutput = []
cooutput = []



for x in range(0, len(zipcode1)):
    for y in range(0, len(mpopulation)):
        if zipcode1[x] == zipcode[y]:
            moutput.append(mpopulation[y])
            soutput.append(spopulation[y])
            goutput.append(gpopulation[y])
            houtput.append(hpopulation[y])
            coutput.append(cpopulation[y])
            poutput.append(ppopulation[y])
            ioutput.append(ipopulation[y])
            koutput.append(kpopulation[y])            
            eoutput.append(epopulation[y])            
            voutput.append(vpopulation[y])    
            doutput.append(dpopulation[y])
            noutput.append(npopulation[y])            
            cooutput.append(copopulation[y])
            
            
output = pd.DataFrame({'Mexico population': moutput, 'El Salvador population': soutput, 'Guatemala population' :goutput,'Honduras population' :houtput, 'China population' :coutput,'India population' :ioutput, 'Ecuador population' :eoutput,  'Dominican Republic population' :doutput,'Nepal population' :noutput,'Colombia population' :cooutput })

output.to_csv('Undocumented_Census_scale_All_second.csv', index = False) 


content = pd.read_csv('ACS_12_5YR_S1701_with_ann.csv')

content1 = pd.read_csv('Population_By_CTrack.csv')

lown = content['HC02_EST_VC01']
lowct = content['GEO.id2']

vn = content1['GEO.id2']

mmm = []
for x in range(0, len(vn)):
    for y in range(0, len(lowct)):
        if vn[x]==lowct[y]:
            mmm.append(lown[y])
output = pd.DataFrame({'Below poverty level': mmm})
output.to_csv('Below poverty level.csv', index = False)


content = pd.read_csv('ACS_12_5YR_B05006_with.csv')


zipcode = content['GEO.id2']

tpopulation = content['HD01_VD01']
mpopulation = content['HD01_VD137']
spopulation = content['HD01_VD140']
gpopulation = content['HD01_VD141']
hpopulation = content['HD01_VD142']
cpopulation = content['HD01_VD48']
ipopulation = content['HD01_VD58']
epopulation = content['HD01_VD152']
dpopulation = content['HD01_VD128']
npopulation = content['HD01_VD61']
copopulation = content['HD01_VD151']  
            
output = pd.DataFrame({'GEO.id2':zipcode,'Total population':tpopulation,'Mexico population':mpopulation, 'El Salvador population': spopulation, 'Guatemala population' :gpopulation,'Honduras population' :hpopulation, 'China population' :cpopulation,'India population' :ipopulation, 'Ecuador population' :epopulation,  'Dominican Republic population' :dpopulation,'Nepal population' :npopulation,'Colombia population' :copopulation })

output.to_csv('Undocumented_Census_scale_all_State.csv', index = False) 

content = pd.read_csv('Undocumented_Census_scale_all_State.csv')

content1 = pd.read_csv('Population_By_CTrack.csv')

zipcode = content['GEO.id2']
zipcode1 = content1['GEO.id2']
mpopulation = content['Mexico undocumented']
spopulation = content['El Salvador undocumented']
gpopulation = content['Guatemala undocumented']
hpopulation = content['Honduras undocumented']
cpopulation = content['China undocumented']
ipopulation = content['India undocumented']
tpopulation = content['Total undocumented']
epopulation = content['Ecuador undocumented']
opopulation = content['Other undocumented']
dpopulation = content['Dominican Republic undocumented']
npopulation = content['Nepal undocumented']
copopulation = content['Colombia undocumented']

moutput = []
soutput = []
goutput = []
houtput = []
coutput = []
toutput = []
ioutput = []
ooutput = []
eoutput = []
doutput = []
noutput = []
cooutput = []



for x in range(0, len(zipcode1)):
    for y in range(0, len(mpopulation)):
        if zipcode1[x] == zipcode[y]:
            moutput.append(mpopulation[y])
            soutput.append(spopulation[y])
            goutput.append(gpopulation[y])
            houtput.append(hpopulation[y])
            coutput.append(cpopulation[y])
            toutput.append(tpopulation[y])
            ioutput.append(ipopulation[y])
            ooutput.append(opopulation[y])            
            eoutput.append(epopulation[y])              
            doutput.append(dpopulation[y])
            noutput.append(npopulation[y])            
            cooutput.append(copopulation[y])
            
            
output = pd.DataFrame({'Others':ooutput,'Total population':toutput,'Mexico population': moutput, 'El Salvador population': soutput, 'Guatemala population' :goutput,'Honduras population' :houtput, 'China population' :coutput,'India population' :ioutput, 'Ecuador population' :eoutput,  'Dominican Republic population' :doutput,'Nepal population' :noutput,'Colombia population' :cooutput })

output.to_csv('Undocumented_Census_scale_All_NewYorkCity.csv', index = False) 


content = pd.read_csv('enigma.csv')

content1 = pd.read_csv('Revised_By_Zipcode.csv')

ez = content['zip_code']
for x in range(0, len(ez)):
    ez[x]= ez[x][0:5]
ebt = content['building_type_service_class']
ec = content['consumption_kwh']

z = content1['GEO.id2']
t = content1['Total population']
f = content1['Foreign-born population']
u = content1['Total undocumented']
lg = [0 for i in range(0, 175)]
sm = [0 for i in range(0, 175)]
print len(z)
for x in range(0, len(z)):
    for y in range(0, len(ez)):
        if int(z[x])== int(ez[y]) and ebt[y] == 'Large Residential':
            lg[x] += ec[y]
   #          lg.append(0)
        if int(z[x])== int(ez[y]) and ebt[y] == 'Small Residential':
            sm[x] += ec[y]
    #    else:
     #       sm.append(0)

all = np.array(lg)+np.array(sm)
print all
tvsa =np.corrcoef(t,all)
tvslg =np.corrcoef(t,lg)
tvssm =np.corrcoef(t,sm)
uvsa =np.corrcoef(u,all)
uvslg =np.corrcoef(u,lg)
uvssm =np.corrcoef(u,sm)


output = pd.DataFrame({'Zipcode': z, 'Total population':t, 'Foreign-born population':f,'Total undocumented':u, 'Large Residential':lg,'Small Residential':sm, 'All Residental':total,
                       'Total VS All':tvsa[0][1],
                       'Total VS large':tvslg[0][1],'Total VS Small':tvssm[0][1], 'Undocumented VS All':uvsa[0][1], 'Undocumented VS Large':uvslg[0][1], 'Undocumented VS Small':uvssm[0][1]  
                       })
output.to_csv('Electricity_correlation.csv', index = False)

content = pd.read_csv('Multi Agency Permits - DOB & DOHMH.csv')

content1 = pd.read_csv('Corporate Registrations - Primary Filings.csv')

lown = content['zip_code']
lowct = np.array(content1['dos_process_address'])
zipcode = []
zipcode2 = []
for x in range(len(lowct)):
    if str(lowct[x])[-5:-4]=='-':
        zipcode.append(str(lowct[x])[-10:-5])
    else:
        zipcode.append(str(lowct[x])[-5:])
        
for x in range(len(lown)):
    if lown[x]>0 :
        zipcode2.append(int(lown[x]))

zipcode2 = map(str, zipcode2)
uzip = set(zipcode)
uzip2 = set(zipcode2)
uzip  =  sorted(list(set(uzip).union(set(uzip2))))
uzip2 = list(uzip2)
number  = [0 for i in range(0,len(uzip))]

for x in range (0, len(uzip)):
    for y in range (0, len(zipcode)):
        if uzip[x]==zipcode[y]:
            number[x]+=1
for x in range (0, len(uzip)):
    for y in range (0, len(zipcode2)):
        if uzip[x]==zipcode2[y]:
            number[x]+=1


output = pd.DataFrame({'Zipcode': uzip, 'Jobs permits':number})
output.to_csv('Jobs.csv', index = False)


content = pd.read_csv('blocks.csv')

content1 = pd.read_csv('Population_By_CTrack.csv')



boro = content['BoroCode'].astype(int)
lastcode = content['CT2010'].astype(int)
lastcode = map(int, lastcode)
lastcode = map(str, lastcode)
boro[boro==5]= 36085
boro[boro==4]= 36081
boro[boro==3]= 36047
boro[boro==2]= 36005
boro[boro==1]= 36061
boro = map(int, boro)
boro = map(str, boro)

for x in range(0, len(lastcode)):
    if len(lastcode[x])== 3:
        mm = '000'+lastcode[x]
        boro[x]= boro[x]+mm
    if len(lastcode[x])== 4:
        mm = '00'+lastcode[x]
        boro[x]= boro[x]+mm
    if len(lastcode[x])== 5:
        mm = '0'+lastcode[x]
        boro[x]= boro[x]+mm
    if len(lastcode[x])== 6:
        boro[x]= boro[x]+lastcode[x]

    
output = pd.DataFrame({'census': boro})
output.to_csv('census.csv', index = False)


content = pd.read_csv('blocks.csv')

content1 = pd.read_csv('Third_Estimation_Population_By_CTrack.csv')



boro = content['Census'].astype(int)
total = content['Shape_Area']
lastcode = content1['GEO.id2'].astype(int)
po = content1['Total population']
lastcode = map(int, lastcode)
lastcode = map(str, lastcode)
boro = map(int, boro)
boro = map(str, boro)

totalpo = [0 for i in range(0, len(boro))]
totalarea = []
mm = '36005000100'
kk = 0
n = 0

hh = []
for x in range(0, len(boro)):
    if boro[x]==mm:
        kk = kk+ total[x]
        n = n+1
    else:
        print kk
        xxx = [kk for i in range(0, n)]
        hh += xxx
        kk = total[x]
        n = 1
        if x<(len(boro)-1):
            mm = boro[x]

print len(totalpo)
print len(hh)
output = pd.DataFrame({'Area':hh})
output.to_csv('New.csv', index = False)



content = pd.read_csv('blocks.csv')

content1 = pd.read_csv('Third_Estimation_Population_By_CTrack.csv')


ppo = content['Census Population']
boro = content['Census'].astype(int)
con = content1['GEO.id2'].astype(int)
po = content1['population']
mm = []
for x in range (0, len(ppo)):
    for  y in range(0, len(con)):
        if boro[x]==con[y]:
            mm.append(po[y])
            continue
        continue
output = pd.DataFrame({'population': mm})
output.to_csv('undocumented.csv', index = False)
