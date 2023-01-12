import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

num_pts=2

name='reactions'

for k in range(num_pts):
    file="".join((name,'_',str(k),".py"))
    s=open('reactions.py','r')
    
####### OCX + OX <=> CO2X + Pt ######  
    new_file_content=""    
    for line in s:
      if "    index = 2," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/O-CO-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 3," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### h-C2H4X + Pt <=> h-C2H3X + HX ######  
# BEEF data
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 5," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/h2cch-h-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 6," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### h-C2H3X <=> CHX + CH2X ######  
# BEEF data
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 6," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/hc-ch2-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 7," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CH2X + CH2X  <=> h-C2H4X ######  
# BEEF data
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 7," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/h2c-ch2-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 8," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()    
    
####### CHCH3X + Pt + Pt  <=>  h-C2H3X + HX ######  
# BEEF data
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 8," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/hcch2-h-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 9," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### CHCH3X + Pt  <=> CCH3X + HX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 9," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CH3C-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 10," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### h-C2H3X + Pt <=> h-C2H2X + HX ######  
# BEEF data 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 10," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/hcch-h-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 11," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### h-C2H2X <=> CHX + CHX ######  
# BEEF data 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 11," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/hc-ch-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 12," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CCH2X + HX <=> h-C2H3X######
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 12," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CH2C-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 13," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### C2H5X + Pt + Pt <=> h-C2H4X + HX ######  
# BEEF data 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 13," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/h2cch2-h-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 14," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

    
####### h-C2H2X + Pt <=> h-C2HX + HX ######  
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 14," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CHC-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 15," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### h-CCH2X + Pt <=>  h-C2HX + HX ######  
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 15," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CCH-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 16," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### h-C2HX <=> CHX + CX ######  
# BEEF data 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 16," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/hc-c-diss-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 17," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CHCH3X + Pt <=> h-C2H4X ######  
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 17," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CHCH3-CH2CH2-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 18," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CCH3X + Pt <=> h-C2H3X######  
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 18," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CH2CH-CCH3-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 19," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CCH2X + Pt <=> h-C2H2X###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 19," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CHCH-CCH2-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 20," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### OCX + Pt <=> CX + OX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 20," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/C-O-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 21," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CHX + OX <=> HCXO + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 21," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/HC-O-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 22," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### OCX + HX <=> HCXO + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 22," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/H-CO-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 23," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### OCX + HX <=> CXOH + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 23," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CO-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 24," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CXOH + Pt <=> CX + HOX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 24," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/C-OH-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 25," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

####### CH3X + Pt <=> CH2X + HX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 25," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CH2-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 26," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CH2X + Pt <=> CHX + HX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 26," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CH-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 27," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CHX + Pt <=> CX + HX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 27," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/C-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 28," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### OCX + HOX <=> CXOOH + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 28," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CO-OH-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 29," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### H2OX + Pt <=> HOX + HX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 29," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/HO-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 30," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### OX + HX <=> HOX + Pt ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 30," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/O-H-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 31," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CH2CH3X + Pt <=> CH2X + CH3X ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 31," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/CH2-CH3-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 32," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    
####### CXOOH + OX <=> CO2X + HOX ###### 
    s=open(file,'r')
    new_file_content=""    
    for line in s:
      if "    index = 32," in line:   
          old=line.strip()
          
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        Ea="):
                   old=line.strip()
                   data=pd.read_csv('ensembles/COOH-O-bee.txt', sep="\t", header=0)
                   perturbation=data.iloc[k,1]
                   bits=line.split("(")
                   correction=float(bits[1].split(",")[0])+perturbation
                   modified="".join(('Ea=(', str(np.round(correction,2)),", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line   
              elif "    index = 33," in line:  
                   old=line.strip()
                   new_line=line.replace(old,old)
                   new_file_content += new_line    
                   break    
              else:
                    old=line.strip()
                    new_line=line.replace(old,old)
                    new_file_content += new_line     
      else:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line                
                   
    s.close()
    writing_file = open(file, "w")
    writing_file.write(new_file_content)
    writing_file.close()
