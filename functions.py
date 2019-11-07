
#This function adds 11 new features to the NYC emissions benchmarking dataframe. It matches load breakdowns for DOE reference buildings to the type according to the NYC data. "building_type" is the DOE reference building type. Any feature with "gas" included is expressing the percentage of gas load is attributable to that source. Any feature with "elec" included is expressing the percentage of electricity load attributable to that source. The "Elec_percent_total" feature expresses what percentage of building energy load is attributed to electricity consumption. 
def category(row):
    row['building_type'] = None
    row['gas_heat'] = 0
    row['gas_water'] = 0
    row['gas_equip'] = 0
    row['elec_heat'] = 0
    row['elec_lighting'] = 0
    row['elec_equipment'] = 0
    row['elec_fans'] = 0
    row['elec_ref'] = 0 
    row['elec_cool'] = 0
    row['elec_percent_total'] = 0
    building_type = None
    gas_heat = 0
    gas_water = 0
    gas_equip = 0
    elec_heat = 0
    elec_lighting = 0
    elec_equipment = 0
    elec_fans = 0
    elec_ref = 0 
    elec_cool = 0
    elec_percent_total = 0
    if (row['Primary Property Type - Self Selected'] == 'Multifamily Housing' or row['Primary Property Type - Self Selected'] == 'Residence Hall/Dormitory' or row['Primary Property Type - Self Selected'] == 'Senior Care Community' or row['Primary Property Type - Self Selected'] == 'Residential Care Facility' or row['Primary Property Type - Self Selected'] == 'Other - Lodging/Residential') and row['Year Built'] >= 1980:
        building_type = 'residential'
        gas_heat = 1184.65 / 1469.31 
        gas_water = 284.66 / 1469.31
        gas_equip = 0 
        elec_heat = 2.42 / 985.79
        elec_lighting = (101.09 + 448.20) / 985.79
        elec_equipment = 448.20 / 985.79
        elec_fans = 69.45 / 985.79
        elec_ref = 0 
        elec_cool = 135.53 / 985.79
        elec_percent_total = 985.79 / (1469.31 +985.79)

    elif row['Primary Property Type - Self Selected'] == 'K-12 School' and row['Year Built'] >= 1980:
        building_type = 'primary school'
        gas_heat = 1449.30 / 1857.81 
        gas_water = 174.17 / 1857.81
        gas_equip = 234.34 / 1857.81
        elec_heat =  0
        elec_cool = 418.34 / 3879.32
        elec_lighting = (165.23 + 1850.87) / 3879.32
        elec_equipment = (1230.23 + 1.50) / 3879.32
        elec_fans = 143.81 / 3879.32
        elec_ref = 69.35 / 3879.32
        elec_percent_total = 3879.32 / (3879.32 + 1857.81)
        
    elif (row['Primary Property Type - Self Selected'] == 'College/University' or row['Primary Property Type - Self Selected'] == 'Other - Education') and row['Year Built'] >= 1980:
        building_type = 'secondary education'
        gas_heat = 6906.37 / 7696.50 
        gas_water = 436.74 / 7696.50
        gas_equip = 353.39 / 7696.50
        elec_heat =  0 
        elec_cool = 5305.92 / 13272.97
        elec_lighting = (343.58 + 4096.48) / 13272.97
        elec_equipment = (2277.82 + 26.43) / 13272.97
        elec_fans = 1083.49 / 13272.97
        elec_ref = 139.25 / 13272.97
        elec_percent_total = 13272.97 / (13272.97 + 7696.50)
        
    elif row['Primary Property Type - Self Selected'] == 'Hotel' and row['Largest Property Use Type - Gross Floor Area (ftå_)'] <= 50000 and row['Year Built'] >= 1980:
        building_type = 'small hotel'
        gas_heat = 362.60 / 944.50 
        gas_water = 392.43 / 944.50
        gas_equip = 189.48 / 944.50
        elec_heat =  58.19 / 2778.25 
        elec_cool = 438.78 / 2778.25
        elec_lighting = (980.34 + 262.69) / 2778.25
        elec_equipment = (812.22 + 1.71) / 2778.25
        elec_fans = 224.32 / 2778.25
        elec_ref = 0 / 2778.25
        elec_percent_total = 2778.25 / (2778.25 + 944.50)
        
    elif (row['Primary Property Type - Self Selected'] == 'Office' or row['Primary Property Type - Self Selected'] == 'Medical Office' or row['Primary Property Type - Self Selected'] == 'Financial Office') and row['Largest Property Use Type - Gross Floor Area (ftå_)'] <= 60000 and row['Year Built'] >= 1980:
        building_type = 'small office building'
        gas_heat = 121.63 / 155.91 
        gas_water = 34.28 / 155.91
        gas_equip = 0 / 155.91
        elec_heat =  561.87 / 3388.81 
        elec_cool = 454.20 / 3388.81
        elec_lighting = (279.73 + 951.62) / 3388.81
        elec_equipment = (1066.52) / 3388.81
        elec_fans = 74.60 / 3388.81
        elec_ref = 0 / 3388.81
        elec_percent_total = 3388.81 / (3388.81 + 155.91)
        
    elif row['Primary Property Type - Self Selected'] == 'Retail Store' and row['Year Built'] >= 1980:
        building_type = 'retail'
        gas_heat = 1115.55 / 1115.55 
        gas_water = 0 / 1115.55
        gas_equip = 0 / 1115.55
        elec_heat =  4.30 / 1838.47 
        elec_cool = 161.65 / 1838.47
        elec_lighting = (971.08 + 157.00) / 1838.47
        elec_equipment = (198.81) / 1838.47
        elec_fans = 345.62 / 1838.47
        elec_ref = 0 / 1838.47
        elec_percent_total = 1838.47 / (1838.47 + 1115.55)
    
    elif (row['Primary Property Type - Self Selected'] == 'Other - Mall' or row['Primary Property Type - Self Selected'] == 'Strip Mall' or row['Primary Property Type - Self Selected'] == 'Enclosed Mall') and row['Year Built'] >= 1980:
        building_type = 'mall'
        gas_heat = 1123.78 / 1123.78 
        gas_water = 0 / 1123.78
        gas_equip = 0 / 1123.78
        elec_heat =  0 / 1819.41 
        elec_cool = 159.45 / 1819.41
        elec_lighting = (212.03 + 1053.00) / 1819.41
        elec_equipment = (149.32) / 1819.41
        elec_fans = 245.60 / 1819.41
        elec_ref = 0 / 1819.41
        elec_percent_total = 1819.41 / (1819.41 + 1123.78)
    
    elif row['Primary Property Type - Self Selected'] == 'Office' and row['Largest Property Use Type - Gross Floor Area (ftå_)'] >= 60000 and row['Year Built'] >= 1980:
        building_type = 'large office'
        gas_heat = 5152.85 / 5380.04 
        gas_water = 227.18 / 5380.04
        gas_equip = 0 / 5380.04
        elec_heat =  0 / 28195.37 
        elec_cool = 6298.57 / 28195.37
        elec_lighting = (8454.49 + 967.50) / 28195.37
        elec_equipment = (8383.98 + 1895.08 + 932.41 + 610.30) / 28195.37
        elec_fans = 653.05 / 28195.37
        elec_ref = 0 / 28195.37
        elec_percent_total = 28195.37 / (28195.37 + 5380.04)
        
    elif (row['Primary Property Type - Self Selected'] == 'Hospital (General Medical & Surgical)' or row['Primary Property Type - Self Selected'] == 'Other - Specialty Hospital') and row['Year Built'] >+ 1980:
        building_type = 'hospital / medical'
        gas_heat = 12467.27 / 14542.51 
        gas_water = 716.82 / 14542.51
        gas_equip = 1358.42 / 14542.51
        elec_heat =  0 / 45755.70 
        elec_cool = 20316.91 / 45755.70
        elec_lighting = (8375.01 + 327.34) / 45755.70
        elec_equipment = (6541.81 + 2499.45 + 1563.02 + 1089.74) / 45755.70
        elec_fans = 3551.80 / 45755.70
        elec_ref = (185.15 + 1305.46) / 45755.70
        elec_percent_total = 45755.70 / (45755.70 + 14542.51)
        
    elif row['Primary Property Type - Self Selected'] == 'Hotel' and row['Largest Property Use Type - Gross Floor Area (ftå_)'] >= 50000 and row['Year Built'] >= 1980:
        building_type = 'large hotel'
        gas_heat = 2676.96 / 10585.84 
        gas_water = 6670.23 / 10585.84
        gas_equip = 1238.65 / 10585.84
        elec_heat =  0.21 / 17536.27 
        elec_cool = 10663.56 / 17536.27
        elec_lighting = (2262.19 + 437.07) / 17536.27
        elec_equipment = (1952.18 + 947.54 + 72.15) / 17536.27
        elec_fans = 1129.47 / 17536.27
        elec_ref = 71.89 / 17536.27
        elec_percent_total = 17536.27 / (17536.27 + 10585.84)
        
    elif (row['Primary Property Type - Self Selected'] == 'Non-Refrigerated Warehouse' or row['Primary Property Type - Self Selected'] == 'Distribution Center') and row['Year Built'] >= 1980:
        building_type = 'warehouse'
        gas_heat = 1630.63 / 1630.63 
        gas_water = 0 / 1630.63
        gas_equip = 0 / 1630.63
        elec_heat =  0 / 826.72 
        elec_cool = 26.64 / 826.72
        elec_lighting = (172.12 + 318.82) / 826.72
        elec_equipment = (104.42) / 826.72
        elec_fans = 204.72 / 826.72
        elec_ref = 0 / 826.72
        elec_percent_total = 826.72 / (826.72 + 1630.63)   
        
    elif row['Primary Property Type - Self Selected'] == 'Supermarket/Grocery Store' or row['Primary Property Type - Self Selected'] == 'Refrigerated Warehouse' or row['Primary Property Type - Self Selected'] == 'Wholesale Club/Supe3294.29' and row['Year Built'] >= 1980:
        building_type = 'warehouse'
        gas_heat = 3070.76 / 3294.29 
        gas_water = 24.40 / 3294.29
        gas_equip = 199.13 / 3294.29
        elec_heat =  0 / 7271.72 
        elec_cool = 179.03 / 7271.72
        elec_lighting = (1512.65 + 257.77) / 7271.72
        elec_equipment = (785.69) / 7271.72
        elec_fans = 1057.04 / 7271.72
        elec_ref = 3479.55 / 7271.72
        elec_percent_total = 7271.72 / (7271.72 + 3294.29)
    #pre 1980
    elif (row['Primary Property Type - Self Selected'] == 'Multifamily Housing' or row['Primary Property Type - Self Selected'] == 'Residence Hall/Dormitory' or row['Primary Property Type - Self Selected'] == 'Senior Care Community' or row['Primary Property Type - Self Selected'] == 'Residential Care Facility' or row['Primary Property Type - Self Selected'] == 'Other - Lodging/Residential') and row['Year Built'] < 1980:
        building_type = 'residential'
        gas_heat = 1406.80 / 1691.47 
        gas_water = 284.66 / 1691.47
        gas_equip = 0 
        elec_heat = 4.58 / 1031.69
        elec_lighting = (101.09 + 229.10) / 1031.69
        elec_equipment = 448.20 / 1031.69
        elec_fans = 85.63 / 1031.69
        elec_ref = 0 
        elec_cool = 163.08 / 1031.69
        elec_percent_total = 1031.69 / (11031.69 + 1691.47)

    elif row['Primary Property Type - Self Selected'] == 'K-12 School' and row['Year Built'] < 1980:
        building_type = 'primary school'
        gas_heat = 2324.02 / 4125.35 
        gas_water = 169.83 / 4125.35
        gas_equip = 234.34 / 4125.35
        elec_heat =  0
        elec_cool = 610.96 / 4125.35
        elec_lighting = (165.23 + 1850.87) / 4125.35
        elec_equipment = (1230.23 + 2.72) / 4125.35
        elec_fans = 196.21 / 4125.35
        elec_ref = 69.14 / 4125.35
        elec_percent_total = 4125.35 / (4125.35 + 2728.19)
        
    elif (row['Primary Property Type - Self Selected'] == 'College/University' or row['Primary Property Type - Self Selected'] == 'Other - Education') and row['Year Built'] < 1980:
        building_type = 'secondary education'
        gas_heat = 8062.71 / 8841.93 
        gas_water = 425.83 / 8841.93
        gas_equip = 353.39 / 8841.93
        elec_heat =  0 
        elec_cool = 1631.42 / 10366.19
        elec_lighting = (4096.48 + 343.58) / 10366.19
        elec_equipment = (2277.82 + 12.17) / 10366.19
        elec_fans = 1865.44 / 10366.19
        elec_ref = 139.28 / 10366.19
        elec_percent_total = 10366.19 / (10366.19 +8841.93)
        
    elif row['Primary Property Type - Self Selected'] == 'Hotel' and row['Largest Property Use Type - Gross Floor Area (ftå_)'] <= 50000 and row['Year Built'] < 1980:
        building_type = 'small hotel'
        gas_heat = 0 / 572.11 
        gas_water = 382.63 / 572.11
        gas_equip = 189.48 / 572.11
        elec_heat =  168.10 / 2684.00 
        elec_cool = 399.55 / 2684.00
        elec_lighting = (980.34 + 262.69) / 2684.00
        elec_equipment = (812.22 + 1.71) / 2684.00
        elec_fans = 59.39 / 2684.00
        elec_ref = 0 / 2684.00
        elec_percent_total = 2684.00 / (2684.00 + 572.11)
        
    elif (row['Primary Property Type - Self Selected'] == 'Office' or row['Primary Property Type - Self Selected'] == 'Medical Office' or row['Primary Property Type - Self Selected'] == 'Financial Office') and row['Largest Property Use Type - Gross Floor Area (ftå_)'] < 60000 and row['Year Built'] < 1980:
        building_type = 'small office building'
        gas_heat = 543.60 / 577.04 
        gas_water = 33.44 / 577.04
        gas_equip = 0 / 577.04
        elec_heat =  0 / 3462.73 
        elec_cool = 440.56 / 3462.73
        elec_lighting = (279.73 + 951.62) / 3462.73
        elec_equipment = (1066.52) / 3462.73
        elec_fans = 724.04 / 3462.73
        elec_ref = 0 / 3462.73
        elec_percent_total = 3462.73 / (3462.73 + 577.04)
        
    elif row['Primary Property Type - Self Selected'] == 'Retail Store' and row['Year Built'] < 1980:
        building_type = 'retail'
        gas_heat = 1115.55 / 1215.27 
        gas_water = 0 / 1215.27
        gas_equip = 0 / 1215.27
        elec_heat =  6.12 / 1959.40 
        elec_cool = 204.79 / 1959.40
        elec_lighting = (971.08 + 157.00) / 1959.40
        elec_equipment = (198.81) / 1959.40
        elec_fans = 421.61 / 1959.40
        elec_ref = 0 / 1959.40
        elec_percent_total = 1959.40 / (1959.40 + 1215.27)
    
    elif (row['Primary Property Type - Self Selected'] == 'Other - Mall' or row['Primary Property Type - Self Selected'] == 'Strip Mall' or row['Primary Property Type - Self Selected'] == 'Enclosed Mall') and row['Year Built'] < 1980:
        building_type = 'mall'
        gas_heat = 1218.69 / 1218.69 
        gas_water = 0 /1218.69
        gas_equip = 0 /1218.69
        elec_heat =  0 / 1922.36 
        elec_cool = 201.09 / 1922.36
        elec_lighting = (212.03 + 1053.00) / 1922.36
        elec_equipment = (149.32) / 1922.36
        elec_fans = 306.91 / 1922.36
        elec_ref = 0 / 1922.36
        elec_percent_total =1922.361 / (1922.36 + 1218.69)
    
    elif row['Primary Property Type - Self Selected'] == 'Office' and row['Largest Property Use Type - Gross Floor Area (ftå_)'] > 60000 and row['Year Built'] < 1980:
        building_type = 'large office'
        gas_heat = 7573.80 / 7795.32 
        gas_water = 221.52 / 7795.32
        gas_equip = 0 / 7795.32
        elec_heat =  0 / 30623.60 
        elec_cool = 8136.08 / 30623.60
        elec_lighting = (8454.49 + 967.50) / 30623.60
        elec_equipment = (1173.77 + 8383.98 + 1895.08 + 792.68) / 30623.60
        elec_fans = 820.02 / 30623.60
        elec_ref = 0 / 30623.60
        elec_percent_total = 30623.60 / (30623.60 + 7795.32)
        
    elif row['Primary Property Type - Self Selected'] == 'Hospital (General Medical & Surgical)' or row['Primary Property Type - Self Selected'] == 'Other - Specialty Hospital' and row['Year Built'] <= 1980:
        building_type = 'hospital / medical'
        gas_heat = 15343.17 / 17400.47 
        gas_water = 698.91 / 17400.47
        gas_equip = 1358.42 / 17400.47
        elec_heat =  0 / 45755.70 
        elec_cool = 20294.21 / 45755.70
        elec_lighting = (8375.01 + 327.34) / 45755.70
        elec_equipment = (6541.81 + 2499.45 + 1647.85 + 1148.03) / 45755.70
        elec_fans = 3899.20 / 45755.70
        elec_ref = (185.15 + 1435.88) / 45755.70
        elec_percent_total = 45755.70 / (45755.70 + 17400.47)
        
    elif row['Primary Property Type - Self Selected'] == 'Hotel' and row['Largest Property Use Type - Gross Floor Area (ftå_)'] >= 50000 and row['Year Built'] <= 1980:
        building_type = 'large hotel'
        gas_heat = 893.77 / 8635.93 
        gas_water = 6503.50 / 8635.93
        gas_equip = 1238.65 / 8635.93
        elec_heat =  1.17 / 16626.82 
        elec_cool = 9580.34 / 16626.82
        elec_lighting = (2262.19 + 437.07) / 16626.82
        elec_equipment = (1952.18 + 947.54 + 67.39) / 16626.82
        elec_fans = 1305.79 / 16626.82
        elec_ref = 73.15 / 16626.82
        elec_percent_total = 16626.82 / (16626.82 + 8635.93)
        
    elif (row['Primary Property Type - Self Selected'] == 'Non-Refrigerated Warehouse' or row['Primary Property Type - Self Selected'] == 'Distribution Center') and row['Year Built'] < 1980:
        building_type = 'warehouse'
        gas_heat = 1832.41 / 1832.41 
        gas_water = 0 / 1832.41
        gas_equip = 0 / 1832.41
        elec_heat =  0 / 826.72 
        elec_cool = 33.69 / 854.76
        elec_lighting = (172.12 + 318.82) / 854.76
        elec_equipment = (104.42) / 854.76
        elec_fans = 225.72 / 854.76
        elec_ref = 0 / 854.76
        elec_percent_total = 854.76 / (854.76 + 1832.41)   
        
    elif (row['Primary Property Type - Self Selected'] == 'Supermarket/Grocery Store' or row['Primary Property Type - Self Selected'] == 'Refrigerated Warehouse' or row['Primary Property Type - Self Selected'] == 'Wholesale Club/Supe3294.29') and row['Year Built'] < 1980:
        building_type = 'Supermarket'
        gas_heat = 3179.84 / 3402.78 
        gas_water = 23.81 / 3402.78
        gas_equip = 199.13 / 3402.78
        elec_heat =  0 / 7375.39 
        elec_cool = 214.48 /  7375.39
        elec_lighting = (1512.65 + 257.77) /  7375.39
        elec_equipment = (785.69) /  7375.39
        elec_fans = 1125.84 /  7375.39
        elec_ref = 3478.97 /  7375.39
        elec_percent_total =  7375.39 / ( 7375.39 + 3402.78)     
    row['building_type'] = building_type
    row['gas_heat'] = gas_heat
    row['gas_water'] = gas_water
    row['gas_equip'] = gas_equip
    row['elec_heat'] = elec_heat
    row['elec_lighting'] = elec_lighting
    row['elec_equipment'] = elec_equipment
    row['elec_fans'] = elec_fans
    row['elec_ref'] = elec_ref 
    row['elec_cool'] = elec_cool
    row['elec_percent_total'] = elec_percent_total
    return row 


#Bins energy star ratings column into "high", "low", "moderate", and "not available" 
def bin_energy_star(row):
    row['ENERGY STAR binned'] = None 
    bin_ = 0
    if row['ENERGY STAR Score'] == None:
        bin_ = 'Not Available' 
    elif row['ENERGY STAR Score'] >= 0 and row['ENERGY STAR Score'] <= 33:
        bin_ = 'Low'
    elif row['ENERGY STAR Score'] > 33 and row['ENERGY STAR Score'] <= 66:
        bin_ = 'Moderate'
    elif row['ENERGY STAR Score'] > 66:
        bin_ = 'High'
    row['ENERGY STAR binned'] = bin_
    return row    
    
        