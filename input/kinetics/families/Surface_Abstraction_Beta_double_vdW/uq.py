
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

alpha_1_ref=0.68
alpha_2_ref= 0.68
alpha_3_ref= 0.02
alpha_4_ref= 0.68
alpha_5_ref= 0.68

E0_1_ref=106.1
E0_2_ref=106.1
E0_3_ref=1.9
E0_4_ref=106.1
E0_5_ref=106.1

Delta_alpha=Delta_alpha-2*x_sobol*Delta_alpha
Delta_E0=Delta_E0-2*x_sobol*Delta_E0

alpha_1=alpha_1_ref+Delta_alpha[:,10]
E0_1=E0_1_ref+Delta_E0[:,11]
alpha_2=alpha_2_ref+Delta_alpha[:,10]
E0_2=E0_2_ref+Delta_E0[:,11]
alpha_3=alpha_3_ref+Delta_alpha[:,12]
E0_3=E0_3_ref+Delta_E0[:,13]
for i in range(num_pts):
    if E0_3[i]<0:
      E0_3[i]=0
    else:
      E0_3[i]=E0_3[i]
      
for i in range(num_pts):
    if alpha_3[i]<0:
      alpha_3[i]=0
    else:
      alpha_3[i]=alpha_3[i]
      
alpha_4=alpha_4_ref+Delta_alpha[:,10]
E0_4=E0_4_ref+Delta_E0[:,11]
alpha_5=alpha_5_ref+Delta_alpha[:,10]
E0_5=E0_5_ref+Delta_E0[:,11]

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
                   modified="".join(("alpha =",str(np.round(float(alpha_4[i]),2)), ","))
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
                   modified="".join(("alpha =",str(np.round(float(alpha_5[i]),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_5[i]),2)), ", 'kJ/mol'),"))
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
