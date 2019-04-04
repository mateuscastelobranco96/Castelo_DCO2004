#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:18:05 2019

@author: mateuscastelobranco
"""
import numpy as np
import scipy.io.wavfile as wv 
import os
import matplotlib.pyplot as plt

soundFile = '/home/mateuscastelobranco/DCO2004_2019/MATERIAL/HD_03_MATLAB/Flauta.wav' # Especifica do local e nome do arquivo de áudio
dFa,vtSom_flauta = wv.read(soundFile)  

soundFile1 = '/home/mateuscastelobranco/DCO2004_2019/MATERIAL/HD_03_MATLAB/Violino.wav' # Especifica do local e nome do arquivo de áudio
dFa1,vtSom_violino = wv.read(soundFile1) 

lfft = 1000
## Construção do single-sided amplitude spectrum.
flauta_fft = np.fft.fft(vtSom_flauta,lfft)/lfft                               # Cálculo da FFT via função do Matlab
violino_fft = np.fft.fft(vtSom_violino,lfft)/lfft 
freq1 = np.arange(0,dFa/2,dFa/lfft)              # Definição do eixo das frequências unilateral
flauta_uni = flauta_fft[0:lfft//2]                                    # Coleta da FFT unilateral
violino_uni = violino_fft[0:lfft//2]

vm=max(np.abs(flauta_uni));   #para normalização
vm1=max(np.abs(violino_uni)); #para normalização

plt.figure(1,[10,7])
plt.subplot(211)
plt.plot(freq1,np.abs(flauta_uni)/vm)                              # Plotagem do espectro unilateral M(f)
plt.title('Espectro  do Sinal da Flauta')                             # Configuração do título do gráfico 
#plt.xlabel('Frequencia (Hz)')                               # Configuração do eixo x do gráfico 
plt.ylabel('|M(f)|')                                         # Configuração do eixo y do gráfico  
plt.grid()
plt.axis([0,5000,0,1.2])

plt.subplot(212)
plt.plot(freq1,np.abs(violino_uni)/vm1)  
plt.title('Espectro  do Sinal do Violino')                             # Configuração do título do gráfico 
plt.xlabel('Frequencia (Hz)')                               # Configuração do eixo x do gráfico 
plt.ylabel('|M(f)|')                                         # Configuração do eixo y do gráfico  
plt.grid()                                                   # Adiona o grid  
plt.axis([0,5000,0,1.2])  


