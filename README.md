mcm2019 certifications

The certification are stored as instances of Cert_text defined in cert.py transformed from jpg format of certifications by tesseract-ocr.

The participants names has been anonymized, only last names are stored.

To load the dataset, run command "pickle.load('anony.s','rb')"

A simple lookup script is provided as proc.py, the arguments are  
	--name  str	//participant name  
	--school str	//school name  
	--award  str	//award type   
	--control	 int   //control number  
	--print-cert action='store_true'//print each cert that satisfies the request   
	--file str //dataset name,default='anony.s'  
 
All arguments should be in lower case.

The calibrate_sc function is used to fix some common mistakes by tesseract-ocr.

