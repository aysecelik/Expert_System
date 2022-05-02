from random import choice
from experta import *
from sqlalchemy import null
from torch import int64

class Heart_Failure(Fact):
    """Info about the traffic light."""
    pass

global sonuc
class Check_Heart_Failure(KnowledgeEngine):
    global sonuc
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) ,
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) ,
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age <= 56.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 153.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 191.0) & P(lambda RestingBP: RestingBP > 109.0) ))
    def rule_1(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) ,
                        Sex=P(lambda Sex: Sex > 0.5) ,  
                        Age=P(lambda Age: Age > 52.5) & P(lambda Age: Age <= 71.5), 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 130.5)  ))
    def rule_2(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age <= 52.5) ))
    def rule_3(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.1) ))
    def rule_4(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5), 
                        Sex=P(lambda Sex: Sex > 0.5)  , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 112.0) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) ))
    def rule_5(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) ,
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) ,
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 149.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 42.5) , 
                        Age=P(lambda Age: Age <= 65.5) ))
    def rule_6(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) & P(lambda MaxHR: MaxHR <= 125.5), 
                        Sex=P(lambda Sex: Sex > 0.5)  , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 130.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG <= 1.5) ))
    def rule_7(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age > 56.5) & P(lambda Age: Age <= 72.0) & P(lambda Age: Age > 59.5) ,
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 316.0) 
                         ))
    def rule_8(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS > 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 103.0) ))
    def rule_9(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 152.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 231.0) ))
    def rule_10(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 97.5) & P(lambda MaxHR: MaxHR <= 147.5), 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 145.0) 
                         ))
    def rule_11(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 151.0) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) ))
    def rule_12(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR."
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS > 0.5) ))    
    def rule_13(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age > 56.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 122.0) ))   
    def rule_14(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope > 0.5)  , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5)  , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5), 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 1.9) ))    
    def rule_15(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age <= 56.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 153.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 191.0) & P(lambda RestingBP: RestingBP <= 109.0) & P(lambda RestingBP: RestingBP <= 107.0) ))   
    def rule_16(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 176.5)  & P(lambda MaxHR: MaxHR <= 183.0) & P(lambda MaxHR: MaxHR > 154.5) ,
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 255.0) 
                        ))    
    def rule_17(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 126.0)  & P(lambda MaxHR: MaxHR > 135.5) & P(lambda MaxHR: MaxHR <= 159.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 146.0) , 
                        Sex=P(lambda Sex: Sex > 0.5) 
                        ))    
    def rule_18(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) & P(lambda MaxHR: MaxHR > 152.0), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 205.0)  ))    
    def rule_19(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 172.0) & P(lambda MaxHR: MaxHR <= 183.0) & P(lambda MaxHR: MaxHR > 154.5) ,
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 255.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 115.0) & P(lambda RestingBP: RestingBP <= 131.0)  ))    
    def rule_20(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope > 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) & P(lambda MaxHR: MaxHR <= 147.5) ,
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5)  , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 1.9) & P(lambda Oldpeak: Oldpeak > 0.05) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 261.0) & P(lambda Cholesterol: Cholesterol <= 244.0)
                        ))    
    def rule_21(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) & P(lambda MaxHR: MaxHR <= 179.5) ,
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 205.0) , 
                        RestingECG=P(lambda RestingECG: RestingECG > 0.5)  , 
                        RestingBP=P(lambda RestingBP: RestingBP > 129.0) ))    
    def rule_22(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 154.5), 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5)  ))    
    def rule_23(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5)  , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 112.0) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) & P(lambda Oldpeak: Oldpeak <= 0.2) ))    
    def rule_24(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 126.0) ))    
    def rule_25(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0)  & P(lambda MaxHR: MaxHR <= 175.5) & P(lambda MaxHR: MaxHR > 158.5) & P(lambda MaxHR: MaxHR > 152.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 231.0) & P(lambda Cholesterol: Cholesterol > 239.0) , 
                        ))    
    def rule_26(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2)  & P(lambda Oldpeak: Oldpeak <= 0.15), 
                        Age=P(lambda Age: Age > 56.5)  & P(lambda Age: Age <= 72.0) & P(lambda Age: Age <= 59.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 316.0) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG > 0.5) 
                        ))   
    def rule_27(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) ,                      
                        Age=P(lambda Age: Age > 52.5)& P(lambda Age: Age <= 74.5)   , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75)  & P(lambda Oldpeak: Oldpeak > 1.25) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 308.0)                        
                        ))    
    def rule_28(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 205.0) & P(lambda Cholesterol: Cholesterol > 255.0) , 
                        RestingECG=P(lambda RestingECG: RestingECG <= 0.5) ,                         
                        Sex=P(lambda Sex: Sex > 0.5) ))    
    def rule_29(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0)  & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) ,   
                        Age=P(lambda Age: Age > 52.5)  & P(lambda Age: Age > 71.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) & P(lambda Cholesterol: Cholesterol > 61.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 130.5)                    
                         ))    
    def rule_30(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope > 0.5), 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0)  & P(lambda MaxHR: MaxHR > 130.5) ,  
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5)  , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 1.9) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 261.0) ))    
    def rule_31(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR > 181.5) ))    
    def rule_32(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 126.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 146.0) ))    
    def rule_33(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.5) ))    
    def rule_34(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) & P(lambda MaxHR: MaxHR > 125.5) ,
                        Sex=P(lambda Sex: Sex > 0.5) ,  
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak > 1.6), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 130.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG <= 1.5)   ))    
    def rule_35(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0)  & P(lambda MaxHR: MaxHR <= 130.5)  & P(lambda MaxHR: MaxHR > 98.0) ,
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak <= 2.5), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 130.5) & P(lambda RestingBP: RestingBP > 127.0), 
                        RestingECG=P(lambda RestingECG: RestingECG > 1.5)  
                        ))    
    def rule_36(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age > 56.5) & P(lambda Age: Age <= 72.0) & P(lambda Age: Age <= 59.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 316.0) ,  
                        FastingBS=P(lambda FastingBS: FastingBS > 0.5) ))    
    def rule_37(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) ,
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak <= 0.75) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 142.5) & P(lambda RestingBP: RestingBP > 119.0) ))    
    def rule_38(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 183.0) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5)  ))    
    def rule_39(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope > 0.5), 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) & P(lambda MaxHR: MaxHR > 147.5),
                        Sex=P(lambda Sex: Sex > 0.5) ,  
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5)  , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 1.9) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 261.0)  ))    
    def rule_40(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 112.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 238.5) ))    
    def rule_41(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 183.0) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 255.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 115.0) & P(lambda RestingBP: RestingBP > 131.0) , 
                        Age=P(lambda Age: Age <= 62.0) ))    
    def rule_42(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) ,
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 112.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 238.5) & P(lambda Cholesterol: Cholesterol <= 205.0) , 
                        Age=P(lambda Age: Age <= 49.5) ))    
    def rule_43(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 144.0), 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5)  ))   
    def rule_44(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 2.2) ))    
    def rule_45(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 144.0) & P(lambda MaxHR: MaxHR > 109.0)  , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5) & P(lambda Oldpeak: Oldpeak > 0.9) , 
                        Age=P(lambda Age: Age > 54.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 136.0) ))    
    def rule_46(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age <= 56.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 153.0) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 132.5) ))    
    def rule_47(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 144.0) & P(lambda MaxHR: MaxHR <= 109.0),
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5)  ))    
    def rule_48(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope > 0.5) ,
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) & P(lambda MaxHR: MaxHR <= 147.5) ,   
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 1.9) & P(lambda Oldpeak: Oldpeak <= 0.05) ,  
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 261.0) , 
                        Age=P(lambda Age: Age > 49.5) ))    
    def rule_49(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 149.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 42.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS > 0.5) ))    
    def rule_50(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 144.0) & P(lambda MaxHR: MaxHR > 109.0) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5) , 
                        Age=P(lambda Age: Age <= 54.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 266.0) ))    
    def rule_51(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) ,
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 126.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 146.0) , 
                        Sex=P(lambda Sex: Sex <= 0.5) ))    
    def rule_52(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 152.5) & P(lambda MaxHR: MaxHR <= 175.5) & P(lambda MaxHR: MaxHR <= 158.5), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 231.0) & P(lambda Cholesterol: Cholesterol > 239.0) & P(lambda Cholesterol: Cholesterol <= 272.0) 
                        ))    
    def rule_53(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak <= 0.75) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 142.5) ))    
    def rule_54(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 183.0) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 255.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 115.0) ))    
    def rule_55(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 145.0) , 
                        Age=P(lambda Age: Age <= 65.5) ))    
    def rule_56(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) & P(lambda MaxHR: MaxHR <= 179.5), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 205.0) & P(lambda Cholesterol: Cholesterol <= 226.5), 
                        RestingECG=P(lambda RestingECG: RestingECG > 0.5)  , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 129.0)  ))    
    def rule_57(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age <= 56.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 153.0) ,
                        MaxHR=P(lambda MaxHR: MaxHR <= 132.5) ))    
    def rule_58(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope > 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) & P(lambda MaxHR: MaxHR <= 147.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 1.9) & P(lambda Oldpeak: Oldpeak > 0.05) ,
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 261.0 )& P(lambda Cholesterol: Cholesterol > 244.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 125.0) ))    
    def rule_59(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) ,
                        Age=P(lambda Age: Age <= 56.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 153.0) & P(lambda Cholesterol: Cholesterol > 255.0),
                        RestingBP=P(lambda RestingBP: RestingBP <= 191.0) & P(lambda RestingBP: RestingBP <= 109.0) & P(lambda RestingBP: RestingBP > 107.0) 
                         ))    
    def rule_60(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope <= 0.5), 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5)  , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5)  ))    
    def rule_61(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 149.0) ,
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 42.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        Age=P(lambda Age: Age > 53.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 143.5) ))    
    def rule_62(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age > 56.5) & P(lambda Age: Age <= 72.0) & P(lambda Age: Age <= 59.5) ,  
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 316.0) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG <= 0.5) ))    
    def rule_63(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) ,  
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 112.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 238.5) & P(lambda Cholesterol: Cholesterol > 205.0) ))    
    def rule_64(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) & P(lambda Oldpeak: Oldpeak > 0.15) ,
                        Age=P(lambda Age: Age > 56.5) & P(lambda Age: Age <= 72.0) & P(lambda Age: Age <= 59.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 316.0) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG > 0.5)  , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 168.0) ))    
    def rule_65(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age > 56.5) & P(lambda Age: Age > 72.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 316.0) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 118.5) ))    
    def rule_66(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) ,
                        Age=P(lambda Age: Age > 52.5)& P(lambda Age: Age <= 74.5) ,  
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak <= 1.25) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 308.0) & P(lambda Cholesterol: Cholesterol <= 530.5),
                         ))    
    def rule_67(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 146.0) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 126.0) & P(lambda MaxHR: MaxHR > 135.5) & P(lambda MaxHR: MaxHR > 159.5) & P(lambda MaxHR: MaxHR > 164.0) ))    
    def rule_68(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 149.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 42.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        Age=P(lambda Age: Age <= 53.0) ))    
    def rule_69(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 152.5), 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5)  ))    
    def rule_70(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 205.0) & P(lambda Cholesterol: Cholesterol <= 255.0), 
                        RestingECG=P(lambda RestingECG: RestingECG <= 0.5)  ))    
    def rule_71(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age > 56.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 316.0) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.5) ))    
    def rule_72(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) & P(lambda MaxHR: MaxHR <= 179.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 205.0) & P(lambda Cholesterol: Cholesterol > 226.5), 
                        RestingECG=P(lambda RestingECG: RestingECG > 0.5)  , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 129.0) ))    
    def rule_73(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 205.0) & P(lambda Cholesterol: Cholesterol > 255.0) , 
                        RestingECG=P(lambda RestingECG: RestingECG <= 0.5) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        Age=P(lambda Age: Age > 58.5) ))    
    def rule_74(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 231.0) & P(lambda Cholesterol: Cholesterol > 239.0) & P(lambda Cholesterol: Cholesterol > 272.0) & P(lambda Cholesterol: Cholesterol > 303.5),
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 152.5) & P(lambda MaxHR: MaxHR <= 175.5) & P(lambda MaxHR: MaxHR <= 158.5)  & P(lambda MaxHR: MaxHR <= 155.5)  ))    
    def rule_75(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 172.0) & P(lambda MaxHR: MaxHR <= 183.0) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 255.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 115.0) & P(lambda RestingBP: RestingBP <= 131.0)& P(lambda RestingBP: RestingBP <= 127.5)
                         ))    
    def rule_76(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 144.0) & P(lambda MaxHR: MaxHR > 109.0) & P(lambda MaxHR: MaxHR > 125.0),
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5) & P(lambda Oldpeak: Oldpeak > 0.9 ),
                        Age=P(lambda Age: Age > 54.0)  , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 136.0)  ))    
    def rule_77(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0)  & P(lambda MaxHR: MaxHR <= 144.0) & P(lambda MaxHR: MaxHR > 109.0) & P(lambda MaxHR: MaxHR <= 125.0), 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5) & P(lambda Oldpeak: Oldpeak > 0.9), 
                        Age=P(lambda Age: Age > 54.0)  , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 136.0)  ))    
    def rule_78(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 97.5) & P(lambda MaxHR: MaxHR > 147.5) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 145.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 276.0) ))    
    def rule_79(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0)  & P(lambda MaxHR: MaxHR <= 130.5) ,  
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak > 2.5), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 130.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG > 1.5)  ))    
    def rule_80(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 97.5) & P(lambda MaxHR: MaxHR > 147.5) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 145.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 276.0) ))    
    def rule_81(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 144.0) & P(lambda MaxHR: MaxHR > 109.0) ,  
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5) & P(lambda Oldpeak: Oldpeak <= 0.9) , 
                        Age=P(lambda Age: Age > 54.0)  ))    
    def rule_82(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) & P(lambda MaxHR: MaxHR > 98.0), 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak <= 2.5), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 130.5)  & P(lambda RestingBP: RestingBP <= 127.0) & P(lambda RestingBP: RestingBP > 123.0),
                        RestingECG=P(lambda RestingECG: RestingECG > 1.5)  
                        ))    
    def rule_83(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0)  & P(lambda MaxHR: MaxHR <= 144.0) & P(lambda MaxHR: MaxHR > 109.0) ,
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5) , 
                        Age=P(lambda Age: Age <= 54.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 266.0) & P(lambda Cholesterol: Cholesterol > 316.5) ))    
    def rule_84(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 98.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak <= 2.5), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 130.5)  & P(lambda RestingBP: RestingBP <= 127.0) & P(lambda RestingBP: RestingBP <= 123.0), 
                        RestingECG=P(lambda RestingECG: RestingECG > 1.5)  ))    
    def rule_85(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) ,
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak <= 0.75) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 142.5) & P(lambda RestingBP: RestingBP <= 119.0) ))    
    def rule_86(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0)  & P(lambda MaxHR: MaxHR <= 98.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak <= 2.5), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 130.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG > 1.5)  ))    
    def rule_87(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 145.0) , 
                        Age=P(lambda Age: Age > 65.5) ))   
    def rule_88(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 144.0) & P(lambda MaxHR: MaxHR > 109.0), 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.5)  , 
                        Age=P(lambda Age: Age <= 54.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 266.0) & P(lambda Cholesterol: Cholesterol <= 316.5) ))    
    def rule_89(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) & P(lambda MaxHR: MaxHR > 125.5), 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak <= 1.6), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 130.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG <= 1.5) 
                         ))    
    def rule_90(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 130.5) , 
                        Age=P(lambda Age: Age > 52.5) & P(lambda Age: Age > 71.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 308.0) & P(lambda Cholesterol: Cholesterol <= 61.5) ))    
    def rule_91(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 231.0) & P(lambda Cholesterol: Cholesterol > 239.0) & P(lambda Cholesterol: Cholesterol > 272.0) ,
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 152.5) & P(lambda MaxHR: MaxHR <= 175.5) & P(lambda MaxHR: MaxHR <= 158.5) & P(lambda MaxHR: MaxHR > 155.5) ))    
    def rule_92(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) & P(lambda Age: Age <= 74.5)  , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) & P(lambda Oldpeak: Oldpeak <= 1.25),
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 308.0) & P(lambda Cholesterol: Cholesterol > 530.5) ))    
    def rule_93(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 149.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 42.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        Age=P(lambda Age: Age > 53.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 143.5) ))    
    def rule_94(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age > 56.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 316.0) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.5) ))    
    def rule_95(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age > 56.5) & P(lambda Age: Age > 72.0) ,
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 316.0) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 118.5) ))    
    def rule_96(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) & P(lambda Oldpeak: Oldpeak > 0.15), 
                        RestingBP=P(lambda RestingBP: RestingBP > 122.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 316.0) , 
                        Age=P(lambda Age: Age > 56.5) & P(lambda Age: Age <= 72.0) & P(lambda Age: Age <= 59.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG > 0.5)  , 
                        MaxHR=P(lambda MaxHR: MaxHR > 168.0) ))    
    def rule_97(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age <= 56.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 153.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 191.0) ))    
    def rule_98(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 2.2) , 
                        Age=P(lambda Age: Age <= 56.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 153.0) & P(lambda Cholesterol: Cholesterol <= 255.0), 
                        RestingBP=P(lambda RestingBP: RestingBP <= 191.0) & P(lambda RestingBP: RestingBP <= 109.0) & P(lambda RestingBP: RestingBP > 107.0) , 
                         ))    
    def rule_99(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS > 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 103.0) ))    
    def rule_100(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 126.0) & P(lambda MaxHR: MaxHR > 135.5) & P(lambda MaxHR: MaxHR > 159.5) & P(lambda MaxHR: MaxHR <= 164.0), 
                        RestingBP=P(lambda RestingBP: RestingBP <= 146.0) , 
                        Sex=P(lambda Sex: Sex > 0.5)  ))    
    def rule_101(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.45) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 126.0)& P(lambda MaxHR: MaxHR <= 135.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 146.0) , 
                        Sex=P(lambda Sex: Sex > 0.5)  ))    
    def rule_102(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) & P(lambda MaxHR: MaxHR > 179.5), 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 205.0) , 
                        RestingECG=P(lambda RestingECG: RestingECG > 0.5)  ))    
    def rule_103(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 205.0) & P(lambda Cholesterol: Cholesterol > 255.0) , 
                        RestingECG=P(lambda RestingECG: RestingECG <= 0.5) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        Age=P(lambda Age: Age <= 58.5) ))    
    def rule_104(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 149.0) & P(lambda MaxHR: MaxHR <= 181.5) & P(lambda MaxHR: MaxHR <= 152.0),
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 205.0) ))    
    def rule_105(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 149.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 42.5) , 
                        Age=P(lambda Age: Age > 65.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG > 0.5) ))   
    def rule_106(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope > 1.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 149.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 42.5) , 
                        Age=P(lambda Age: Age > 65.5) , 
                        RestingECG=P(lambda RestingECG: RestingECG <= 0.5) ))   
    def rule_107(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 183.0) & P(lambda MaxHR: MaxHR > 176.5) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 255.0)  ))    
    def rule_108(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 130.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Age=P(lambda Age: Age > 52.5) & P(lambda Age: Age > 74.5) ,
                        Oldpeak=P(lambda Oldpeak: Oldpeak > 0.1) & P(lambda Oldpeak: Oldpeak > 0.75) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 308.0) 
                         ))    
    def rule_109(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 183.0) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5)  , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 255.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 115.0) & P(lambda RestingBP: RestingBP > 131.0) , 
                        Age=P(lambda Age: Age > 62.0) ))    
    def rule_110(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 172.0) & P(lambda MaxHR: MaxHR <= 183.0) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 255.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 115.0) & P(lambda RestingBP: RestingBP <= 131.0) & P(lambda RestingBP: RestingBP > 127.5)
                      ))    
    def rule_111(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 154.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 151.0) ))    
    def rule_112(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 154.5) ,  
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 151.0) , 
                        FastingBS=P(lambda FastingBS: FastingBS > 0.5) ))    
    def rule_113(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 152.5) & P(lambda MaxHR: MaxHR > 175.5),
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 231.0) & P(lambda Cholesterol: Cholesterol > 239.0)  ))    
    def rule_114(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR <= 155.5)  & P(lambda MaxHR: MaxHR > 152.5)  & P(lambda MaxHR: MaxHR <= 175.5) & P(lambda MaxHR: MaxHR <= 158.5),
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 231.0) & P(lambda Cholesterol: Cholesterol > 239.0) & P(lambda Cholesterol: Cholesterol > 272.0) & P(lambda Cholesterol: Cholesterol <= 303.5) ))    
    def rule_115(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR > 151.0) & P(lambda MaxHR: MaxHR > 152.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) ,
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 231.0) & P(lambda Cholesterol: Cholesterol <= 239.0) ))    
    def rule_116(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope > 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) & P(lambda MaxHR: MaxHR <= 147.5) , 
                        Sex=P(lambda Sex: Sex > 0.5)  , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 1.9) & P(lambda Oldpeak: Oldpeak > 0.05) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 261.0) & P(lambda Cholesterol: Cholesterol > 244.0) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 125.0) ))    
    def rule_117(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & P(lambda ST_Slope: ST_Slope > 0.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) &P(lambda MaxHR: MaxHR <= 147.5)  & P(lambda MaxHR: MaxHR > 136.0), 
                        Sex=P(lambda Sex: Sex > 0.5)  , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 1.9) & P(lambda Oldpeak: Oldpeak <= 0.05) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 261.0)   , 
                        Age=P(lambda Age: Age <= 49.5) 
                        ))    
    def rule_118(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) & 
                        P(lambda ST_Slope: ST_Slope > 0.5)  , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5) & P(lambda MaxHR: MaxHR <= 147.5) & P(lambda MaxHR: MaxHR <= 136.0)  , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType > 0.5)  , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 1.9) & P(lambda Oldpeak: Oldpeak <= 0.05) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 261.0)  , 
                        Age=P(lambda Age: Age <= 49.5)  ))    
    def rule_119(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5)  , 
                        Sex=P(lambda Sex: Sex > 0.5) , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 112.0) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) & P(lambda Oldpeak: Oldpeak > 0.2) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol > 96.0) ))    
    def rule_120(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5), 
                        Sex=P(lambda Sex: Sex > 0.5) ,   
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP > 112.0) , 
                        Oldpeak=P(lambda Oldpeak: Oldpeak <= 0.45) & P(lambda Oldpeak: Oldpeak > 0.2) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 96.0) ))    
    def rule_121(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR > 130.5), 
                        Sex=P(lambda Sex: Sex > 0.5)  , 
                        ChestPainType=P(lambda ChestPainType: ChestPainType <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 112.0) , 
                        Cholesterol=P(lambda Cholesterol: Cholesterol <= 238.5) & P(lambda Cholesterol: Cholesterol <= 205.0) , 
                        Age=P(lambda Age: Age > 49.5) ))    
    def rule_122(self):
        global sonuc
        sonuc= "KALP YETMEZLİĞİ RİSKİ YOKTUR." 
    @Rule(Heart_Failure(ST_Slope=P(lambda ST_Slope: ST_Slope <= 1.5) , 
                        MaxHR=P(lambda MaxHR: MaxHR <= 151.0) & P(lambda MaxHR: MaxHR <= 97.5), 
                        Sex=P(lambda Sex: Sex <= 0.5) , 
                        FastingBS=P(lambda FastingBS: FastingBS <= 0.5) , 
                        ExerciseAngina=P(lambda ExerciseAngina: ExerciseAngina <= 0.5) , 
                        RestingBP=P(lambda RestingBP: RestingBP <= 145.0)  ))    
    def rule_123(self):
        global sonuc
        sonuc="KALP YETMEZLİĞİ RİSKİ VARDIR." 


def decision(data):
    try:
        global sonuc
        print(data)
        var_engine = Check_Heart_Failure()
        var_engine.reset()
        var_engine.declare(Heart_Failure(ST_Slope=float(data['ST_Slope']),
                                        ChestPainType=float(data['ChestPainType']),
                                        Oldpeak=float(data['Oldpeak']),
                                        Age=float(data['Age']),
                                        Cholesterol=float(data['Cholesterol']),
                                        RestingBP=float(data['RestingBP']),
                                        Sex=float(data['Sex']),
                                        FastingBS=float(data['FastingBS']),
                                        RestingECG=float(data['RestingECG']),
                                        MaxHR=float(data['MaxHR']),
                                        ExerciseAngina=float(data['ExerciseAngina']),
                                        ))
        var_engine.run()
        return sonuc
    except Exception as e:
        print(e)
    