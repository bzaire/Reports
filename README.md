# V471TAU

V471Tau is a eclipsing binary system member of the $625\mathrm{Myrs}$ old Hyades open cluster (Perryman et al. 1998). It is composed by a K dwarf MS star and a white dwarf.

The orbital motion of secondary star is given by:
\begin{equation} \label{eq:v_shift}
    V = K\sin\left[\frac{2\pi}{P_\mathrm{rot}}(t - t_o + \phi)\right] + v_\mathrm{rad},
\end{equation} where $K$ is the semi-amplitude, $P_\mathrm{rot}$ is the period of rotation around the primary star (the white dwarf), and $v_\mathrm{rad}$ is the radial velocity of the binary system. In this work we use the ephemeris by Vaccaro et al. (2015), $t_o(\mathrm{min} \; I) = \mathrm{HJED}\; 2445821.898291 + 0.5211833875\mathrm{E}$.

- For different periods read: O'Brien et al. (2001); Kundra \& Hric 2011

## Spectropolarimetric observations of V471Tau 

We used the ESPaDOnS instrument on the Canada France Hawaii Telescope (CFHT) to observe the K-dwarf star. ESPaDOnS collect circularly polarized spectra (Stokes $V$) and intensity spectra (Stokes $I$) covering wavelengths from $370$ to $1,000\mathrm{nm}$ at a resolving power of $65,000$ (ref. --). Data spans in two different epochs: November 2004 (three nights) and December 2005 (four nights). They correspond respectively to a total of 58 and 102 circularly polarized spectra, each one acquired in $200\mathrm{s}$ of observation. 


# Reports

## Rendering the reports:
 go to https://nbviewer.jupyter.org and paste the github link to the notebook.

## Notebooks order:
  1 - search_3d_params.ipynb (https://github.com/bzaire/Reports/blob/master/search_3d_params.ipynb)
      
     > Computes the center of the paraboloid of spot coverage at both epochs. 
  
  2 - compare_chisqs.ipynb (https://github.com/bzaire/Reports/blob/master/compare_chisqs.ipynb)
      
     > Compare results using different reduced chisqs (To compare with Baptiste's approach).

  3 - adjusting_vsin_eqw.ipynb (https://github.com/bzaire/Reports/blob/master/adjusting_vsin_eqw.ipynb)
     
     > Using the orbital parameters found on 1st step we look for the best EQW and Vsin(i) in a recursive way;
     > vsin(i) is chosen to match in both years of observation.  
  
  4 - search_DR.ipynb (https://github.com/bzaire/Reports/blob/master/search_DR.ipynb)
     
     > Fix everything else to find the differential rotation parameters (beta and gamma).
  
