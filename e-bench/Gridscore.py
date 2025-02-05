import cmath
import math
FeederP_max=1
Ploss_max=1
IF_max=0.1
def gridscore (VraValue,ViaValue,VrbValue,VibValue,VrcValue,VicValue,Total_real_loss,rValue, FeederP_max, Ploss_max,IF_max):
    #Calculate IF
    Vab=abs(complex((VraValue-VrbValue),(ViaValue-VibValue)))
    Vbc = abs(complex((VrbValue - VrcValue), (VibValue - VicValue)))
    Vca = abs(complex((VrcValue - VraValue), (VicValue - ViaValue)))
    print(Vab,",",Vbc,",",Vca,",")
    alpha=((Vab**4+Vbc**4+Vca**4)/((Vab**2+Vbc**2+Vca**2)**2))
    Teg=(1-math.sqrt(3-6*alpha))/(1+math.sqrt(3+6*alpha))
    IF=math.sqrt(Teg)
    #IF=1
    if IF>IF_max:
        IF_max=IF
    #IF_max=IF*1.01
    T1=IF/IF_max

    #Calculate Voltage deviation
    vnom=280
    Del_vmax=15
    Del_va=abs(((complex(VraValue,ViaValue))-vnom)/vnom)
    Del_vb = abs(((complex(VrbValue, VibValue)) - vnom) / vnom)
    Del_vc = abs(((complex(VrcValue, VicValue)) - vnom) / vnom)
    T2=(Del_va+Del_vb+Del_vc)/(3*Del_vmax)

    #Calculate Feeder laod
    FeederP=rValue
    if rValue>FeederP_max:
        FeederP_max=rValue
    T3=FeederP/FeederP_max

    #Calculate Losses
    Ploss=Total_real_loss
    if Total_real_loss>Ploss_max:
        Ploss_max=Total_real_loss
    T4=Ploss/Ploss_max

    #GIS
    GIS=(T1+T2+T3+T4)/4

    return (GIS,Ploss_max,FeederP_max,IF_max)

FeederP_max = FeederP_max
Ploss_max = Ploss_max

gis_store=[]
t=[]

def GIS_store(grantedtime,GIS):
    t.append(grantedtime)
    gis_store.append(GIS)