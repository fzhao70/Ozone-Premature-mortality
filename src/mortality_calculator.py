# Caluation of mortality due to Ozone
# fzhao70
#
# disease reference (y0) :
# WHO methods and data sources for global causes of death 2000-2016. \
# Global Health Estimates Technical Paper WHO/HIS/IER/GHE/2018.3. \
# Geneva: World Health Organization; 2018.
# ug/m3 -> ppb
# 2.00 : STP European Union" Conditions at 20°C (EU standard) 
#
# AMDA8 100 ug/m3 is a Threshold given by WHO
# For China other thresholds:
#   Ozone Threshold : AMDA8  26.7 ppb (- 31.1 ppb) Turner et al. 2016
#   Ozone Threshold : 6mMDA1 33.3 pbb (- 41.9 ppb) Jerrett et al. 2009
# AMDA8 (annual average daily maximum 8-h ozone concentration)
# 6mMDA1 (average daily maximum 1-h ozone concentration from April to September)

import numpy as np

def mort_R(c, pop, region):
    """ Respiratory 
    persons/yr 2016 data
    WHO database 2016
    China: 1411415
        Respiratory infectious 177.5
        177.3 Lower respiratory infections	
        0.2 Upper respiratory infections	
        0.0 Otitis media	
        Respiratory disease 938.2
        895.4 COPD
        24.3 Asthma
        18.6 Other 
    US: 322180
        Respiratory infectious 66.4
        66.2 Lower respiratory infections	
        0.2 Upper respiratory infections	
        0.0 Otitis media	
        Respiratory disease 246.9
        193.2 COPD
        4.2 Asthma
        49.6 Other 
    """
    if region == 'china':
        y0 = (938.2 + 177.5) / (1411415) # persons/yr 2016 data WHO
    elif region == 'us':
        y0 = (66.4 + 246.9) / (322180) # persons/yr 2016 data WHO

    #beta = np.log(1.04) / (20 / 2.0) # Warm Season Only  Lipsett et al. 2011
    beta = np.log(1.11) / (20 / 2.0) # Lipsett et al. 2011

    if c > (100 / 2.0): 
        rr = np.exp(beta * (c - (100 / 2.0)))
    else:
        rr = 1.0
    mort = y0 * ((rr - 1) / rr) * pop

    return mort

def mort_C(c, pop, region):
    """ Cardiovascular
    WHO database 2016
    China: 1411415
        Cardiovascular disease 4475.7
        85.0 Rheumatic heart disease
        276.5 Hypertensive heart disease
        1927.8 Ischaemic heart disease
        2018.0 Stroke
        37.9 Cardiomyopathy, myocarditis, endocarditis
        130.4 Other circulatory diseases
    US: 322180
        Cardiovascular disease 837.2
        3.7 Rheumatic heart disease
        46.5 Hypertensive heart disease
        500.3 Ischaemic heart disease
        147.3 Stroke
        32.5 Cardiomyopathy, myocarditis, endocarditis
        107.0 Other circulatory diseases
    """
    if region == 'china':
        y0 = (4475.7) / (1411415) # persons/yr 2016 data WHO
    elif region == 'us':
        y0 = (837.2) / (322180) # persons/yr 2016 data WHO

    #beta = np.abs(np.log(0.98)) / (20 / 2.0) # Warm Season Only Jerrett et al. 2009
    beta = np.log(1.02) / (20 / 2.0) # Kreski et al. 2009 Smith et al. 2009

    if c > (100 / 2.0): 
        rr = np.exp(beta * (c - (100 / 2.0)))
    else:
        rr = 1.0

    mort = y0 * ((rr - 1) / rr) * pop

    return mort

def mort_L(c, pop, region):
    """ Lung Cancer
    WHO database 2016
    China: 1411415
        Lung Cancer 637.7
    US: 322180
        Lung Cancer 84.7
    """
    if region == 'china':
        y0 = (637.7) / (1411415) # persons/yr 2016 data WHO
    elif region == 'us':
        y0 = (84.7) / (322180) # persons/yr 2016 data WHO

    #beta = np.log(0.97) / (20 / 2.0) # Krewski et al. 2009 
    #beta = np.log(0.93) / (20 / 2.0) # Jerrett et al. 2013 
    beta = np.abs(np.log(0.96)) / (20 / 2.0) # Turner et al. 2016 

    if c > (100 / 2.0): 
        rr = np.exp(beta * (c - (100 / 2.0)))
    else:
        rr = 1.0

    mort = y0 * ((rr - 1) / rr) * pop

    return mort
