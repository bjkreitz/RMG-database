
from torch.quasirandom import SobolEngine

import numpy as np
import matplotlib.pyplot as plt
import os

num_pts = 2000  # the number of points to generate

sobol=SobolEngine(dimension=80,scramble=True,seed=100)

x_sobol=sobol.draw(num_pts)

#Values for surface abstraction beta

Delta_alpha=0.1
Delta_E0=15

alpha_1_ref= 0.84
alpha_2_ref= 0.77
alpha_3_ref= 0.72

E0_1_ref=185.1
E0_2_ref=142.8
E0_3_ref=126.4

Delta_alpha=Delta_alpha-2*x_sobol*Delta_alpha
Delta_E0=Delta_E0-2*x_sobol*Delta_E0

alpha_1=alpha_1_ref+Delta_alpha[:,42]
E0_1=E0_1_ref+Delta_E0[:,43]
alpha_2=alpha_2_ref+Delta_alpha[:,44]
E0_2=E0_2_ref+Delta_E0[:,45]
alpha_3=alpha_3_ref+Delta_alpha[:,46]
E0_3=E0_3_ref+Delta_E0[:,47]

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
                   modified="".join(("alpha =",str(np.round(float(alpha_2[i]),2)), ","))
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
                   modified="".join(("alpha =",str(np.round(float(alpha_3[i]),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_3[i]),2)), ", 'kJ/mol'),"))
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
