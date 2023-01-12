
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

alpha_1_ref=0.84
alpha_2_ref= 0.51
alpha_3_ref= 0.58
alpha_4_ref= 0.57
alpha_5_ref= 0.57
alpha_6_ref= 0.57
alpha_7_ref= 0.57
alpha_8_ref= 0.72
alpha_9_ref= 0.57
alpha_10_ref= 0.57

E0_1_ref=185.1
E0_2_ref=97.5
E0_3_ref=117.7
E0_4_ref=75.25
E0_5_ref=75.25
E0_6_ref=75.25
E0_7_ref=75.25
E0_8_ref=126.39
E0_9_ref=75.25
E0_10_ref=75.25

Delta_alpha=Delta_alpha-2*x_sobol*Delta_alpha
Delta_E0=Delta_E0-2*x_sobol*Delta_E0

alpha_1=alpha_1_ref+Delta_alpha[:,48]
E0_1=E0_1_ref+Delta_E0[:,49]
alpha_2=alpha_2_ref+Delta_alpha[:,50]
E0_2=E0_2_ref+Delta_E0[:,51]
alpha_3=alpha_3_ref+Delta_alpha[:,52]
E0_3=E0_3_ref+Delta_E0[:,53]
alpha_4=alpha_4_ref+Delta_alpha[:,54]
E0_4=E0_4_ref+Delta_E0[:,53]
alpha_5=alpha_5_ref+Delta_alpha[:,54]
E0_5=E0_5_ref+Delta_E0[:,55]
alpha_6=alpha_6_ref+Delta_alpha[:,54]
E0_6=E0_6_ref+Delta_E0[:,55]
alpha_7=alpha_7_ref+Delta_alpha[:,54]
E0_7=E0_7_ref+Delta_E0[:,55]
alpha_8=alpha_8_ref+Delta_alpha[:,56]
E0_8=E0_8_ref+Delta_E0[:,57]
alpha_9=alpha_9_ref+Delta_alpha[:,54]
E0_9=E0_9_ref+Delta_E0[:,55]
alpha_10=alpha_10_ref+Delta_alpha[:,54]
E0_10=E0_10_ref+Delta_E0[:,55]

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
              elif "    index = 10" in line:  
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
      if "    index = 10" in line:
          old=line.strip()
          new_line=line.replace(old,old)
          new_file_content += new_line   
          for line in s:
              if line.startswith("        alpha ="):
                   old=line.strip()
                   modified="".join(("alpha =",str(np.round(float(alpha_10[i]),2)), ","))
                   new_line=line.replace(old,modified)
                   new_file_content += new_line
              elif line.startswith("        E0 = ("):     
                   old=line.strip()
                   modified="".join(("E0 = (",str(np.round(float(E0_10[i]),2)), ", 'kJ/mol'),"))
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
