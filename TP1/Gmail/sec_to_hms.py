def sec_to_hms(nb1):
	heure = nb1 % 3600
	minute = (nb1 -(heure*3600))%60
	seconde =  nb1 -(heure*3600) - (minute*60)
	return (heure, minute, seconde)
