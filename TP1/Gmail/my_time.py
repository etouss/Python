#my_time.py
import time
def sec_to_hms(sec):
    ''' retourne le temps correspondant en (h,m,s)'''
	heure = nb1 % 3600
	minute = (nb1 -(heure*3600))%60
	seconde =  nb1 -(heure*3600) - (minute*60)
	return (heure, minute, seconde)
    	pass

def hms_to_sec(h, m, s):
    '''retourne le temps correspondant en seconde'''
	return heure*3600+minte*60+seconde	
    	pass

def now():
    ''' utilise le module time pour donner l'heure sous la forme (h, m, s)'''
    return time.strftime("%Y-%m-%d %H:%M:%S",localtime())
    pass

if __name__== "__main__":
    print("ici j'écrirai l'heure")
