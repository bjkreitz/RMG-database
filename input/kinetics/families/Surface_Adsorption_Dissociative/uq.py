
from torch.quasirandom import SobolEngine

import numpy as np
import matplotlib.pyplot as plt
import os

num_pts = 2000  # the number of points to generate

sobol=SobolEngine(dimension=80,scramble=True,seed=100)

x_sobol=sobol.draw(num_pts)

#Values for surface abstraction

Delta_alpha=0.1
Delta_E0=15

alpha_1_ref=0.69
alpha_2_ref= 0
alpha_3_ref= 0
alpha_4_ref= 0
alpha_5_ref= 0
alpha_6_ref=0.69
alpha_7_ref= 0.69
alpha_8_ref= 0.76
alpha_9_ref=0.69 

E0_1_ref=107.9
E0_2_ref=3.8
E0_3_ref=58
E0_4_ref=42.7
E0_5_ref=33.6
E0_6_ref=107.9
E0_7_ref=107.9
E0_8_ref=107.1
E0_9_ref=107.9

Delta_alpha=Delta_alpha-2*x_sobol*Delta_alpha
Delta_E0=Delta_E0-2*x_sobol*Delta_E0

alpha_1=alpha_1_ref+Delta_alpha[:,58]
E0_1=E0_1_ref+Delta_E0[:,59]
alpha_2=alpha_2_ref
E0_2=E0_2_ref+Delta_E0[:,60]
for i in range(num_pts):
    if E0_2[i]<0:
      E0_2[i]=0
    else:
      E0_2[i]=E0_2[i]
alpha_3=alpha_3_ref
E0_3=E0_3_ref+Delta_E0[:,61]
alpha_4=alpha_4_ref
E0_4=E0_4_ref+Delta_E0[:,61]
alpha_5=alpha_5_ref
E0_5=E0_5_ref+Delta_E0[:,61]
alpha_6=alpha_6_ref+Delta_alpha[:,58]
E0_6=E0_6_ref+Delta_E0[:,59]
alpha_7=alpha_7_ref+Delta_alpha[:,58]
E0_7=E0_7_ref+Delta_E0[:,59]
alpha_8=alpha_8_ref+Delta_alpha[:,62]
E0_8=E0_8_ref+Delta_E0[:,63]
alpha_9=alpha_9_ref+Delta_alpha[:,58]
E0_9=E0_9_ref+Delta_E0[:,59]

Name='rules_'

for i in range(num_pts):
    file="".join((Name,str(i),".py"))
    s=open("rules.py",'r')
    new_file_content=""    
    for line in s:
      if "    index = 1" in line:   
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_1[i]),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line 
              elif line.startswith("        E0 = ("):
                  old=line.strip()
                  modified="".join(("E0 = (",str(np.round(float(E0_1[i]),2)), ", 'kJ/mol'),"))
                  new_line=line.replace(old,modified)
                  new_file_content += new_line      
              elif "    index = 2" in line:  
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
    s=open(file,'r')
    new_file_content=""    
    for line in s:                   
      if "    index = 2" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_2),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_2[i]),2)), ", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line      
              elif "    index = 3" in line:  
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
    
    s=open(file,'r')
    new_file_content=""    
    for line in s:                   
      if "    index = 3" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_3),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_3[i]),2)), ", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line      
              elif "    index = 4" in line:  
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
    
    s=open(file,'r')
    new_file_content=""    
    for line in s:                   
      if "    index = 4" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_4),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_4[i]),2)), ", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line      
              elif "    index = 5" in line:  
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
    
    s=open(file,'r')
    new_file_content=""    
    for line in s:                   
      if "    index = 5" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_5),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_5[i]),2)), ", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line      
              elif "    index = 6" in line:  
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
    
    s=open(file,'r')
    new_file_content=""    
    for line in s:                   
      if "    index = 6" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_6[i]),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_6[i]),2)), ", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line      
              elif "    index = 7" in line:  
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
    
    s=open(file,'r')
    new_file_content=""    
    for line in s:                   
      if "    index = 7" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_7[i]),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_7[i]),2)), ", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line      
              elif "    index = 8" in line:  
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
    
    s=open(file,'r')
    new_file_content=""    
    for line in s:                   
      if "    index = 8" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_8[i]),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_8[i]),2)), ", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line      
              elif "    index = 9" in line:  
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

    
    s=open(file,'r')
    new_file_content=""    
    for line in s:                   
      if "    index = 9" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_9[i]),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_9[i]),2)), ", 'kJ/mol'),"))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line                         
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
