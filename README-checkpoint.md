# Reports

## Rendering the reports:
 go to https://nbviewer.jupyter.org and paste the github link to the notebook.

## Notebooks order:
  1 - choose_caim_stokes_I.ipynb (https://github.com/bzaire/Reports/blob/master/choose_caim_stokes_I.ipynb)
  
     > Search for the chisq value to be aimed when fitting stokes I.
     
  2 - choose_caim_stokes_V.ipynb (https://github.com/bzaire/Reports/blob/master/choose_caim_stokes_V.ipynb)

     > Search for the chisq value to be aimed using stokes V individually.
     
  2 - search_3d_params.ipynb (https://github.com/bzaire/Reports/blob/master/search_3d_params.ipynb)
      
     > Computes the center of the paraboloid of spot coverage at both epochs (use only Stokes I but with all the sub-exposures).  
 
  3 - adjusting_vsin_eqw.ipynb (https://github.com/bzaire/Reports/blob/master/adjusting_vsin_eqw.ipynb)
     
     > Using the orbital parameters found on 1st step we look for the best EQW and Vsin(i) in a recursive way;
     > vsin(i) is chosen to match in both years of observation.  
  
  4 - search_DR.ipynb (https://github.com/bzaire/Reports/blob/master/search_DR.ipynb)
     
     > Fix everything else to find the differential rotation parameters (beta and gamma).
  
