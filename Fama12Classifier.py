def industry_classification_Fama12(sic_code):
    if sic_code >= 100 and sic_code <= 999:
        classification = '1 Consumer Nondurables -- Food, Tobacco, Textiles, Apparel, Leather, Toys'
    elif sic_code >= 2000 and sic_code <= 2399:
        classification = '1 Consumer Nondurables -- Food, Tobacco, Textiles, Apparel, Leather, Toys'
    elif sic_code >= 2700 and sic_code <= 2749:
        classification = '1 Consumer Nondurables -- Food, Tobacco, Textiles, Apparel, Leather, Toys'
    elif sic_code >= 2770 and sic_code <= 2799:
        classification = '1 Consumer Nondurables -- Food, Tobacco, Textiles, Apparel, Leather, Toys'
    elif sic_code >= 3100 and sic_code <= 3199:
        classification = '1 Consumer Nondurables -- Food, Tobacco, Textiles, Apparel, Leather, Toys'
    elif sic_code >= 3940 and sic_code <= 3989:
        classification = '1 Consumer Nondurables -- Food, Tobacco, Textiles, Apparel, Leather, Toys'
    elif sic_code >= 2500 and sic_code <= 2519:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code >= 2590 and sic_code <= 2599:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code >= 3630 and sic_code <= 3659:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code >= 3710 and sic_code <= 3711:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code == 3714:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code == 3716: 
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code >= 3750 and sic_code <= 3751:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code == 3792:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code >= 3900 and sic_code <= 3939:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code >= 3990 and sic_code <= 3999:
        classification = '2 Consumer Durables -- Cars, TVs, Furniture, Household Appliances'
    elif sic_code >= 2520 and sic_code <= 2589:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 2600 and sic_code <= 2699:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 2750 and sic_code <= 2769:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3000 and sic_code <= 3099:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3200 and sic_code <= 3569:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3580 and sic_code <= 3629:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3700 and sic_code <= 3709:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3712 and sic_code <= 3713:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code == 3715:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3717 and sic_code <= 3749:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3752 and sic_code <= 3791:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3793 and sic_code <= 3799:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3830 and sic_code <= 3839:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 3860 and sic_code <= 3899:
        classification = '3 Manufacturing -- Machinery, Trucks, Planes, Off Furn, Paper, Com Printing'
    elif sic_code >= 1200 and sic_code <= 1399:
        classification = '4 Energy -- Oil, Gas, and Coal Extraction and Products'
    elif sic_code >= 2900 and sic_code <= 2999:
        classification = '4 Energy -- Oil, Gas, and Coal Extraction and Products'
    elif sic_code >= 2800 and sic_code <= 2829:
        classification = '5 Chemicals -- Chemicals and Allied Products'
    elif sic_code >= 2840 and sic_code <= 2899:
        classification = '5 Chemicals -- Chemicals and Allied Products'
    elif sic_code >= 3570 and sic_code <= 3579:
        classification = '6 Business Equipment -- Computers, Software, and Electronic Equipment'
    elif sic_code >= 3660 and sic_code <= 3692:
        classification = '6 Business Equipment -- Computers, Software, and Electronic Equipment'
    elif sic_code >= 3694 and sic_code <= 3699:
        classification = '6 Business Equipment -- Computers, Software, and Electronic Equipment'
    elif sic_code >= 3810 and sic_code <= 3829:
        classification = '6 Business Equipment -- Computers, Software, and Electronic Equipment'
    elif sic_code >= 7370 and sic_code <= 7379:
        classification = '6 Business Equipment -- Computers, Software, and Electronic Equipment'
    elif sic_code >= 4800 and sic_code <= 4899:
        classification = '7 Telecom -- Telephone and Television Transmission'
    elif sic_code >= 4900 and sic_code <= 4949:
        classification = '8 Utilities'
    elif sic_code >= 5000 and sic_code <= 5999:
        classification = '9 Shops -- Wholesale, Retail, and Some Services (Laundries, Repair Shops)'
    elif sic_code >= 7200 and sic_code <= 7299:
        classification = '9 Shops -- Wholesale, Retail, and Some Services (Laundries, Repair Shops)'
    elif sic_code >= 7600 and sic_code <= 7699:
        classification = '9 Shops -- Wholesale, Retail, and Some Services (Laundries, Repair Shops)'
    elif sic_code >= 2830 and sic_code <= 2839:
        classification = '10 Healthcare -- Healthcare, Medical Equipment, and Drugs'
    elif sic_code == 3693:
        classification = '10 Healthcare -- Healthcare, Medical Equipment, and Drugs'
    elif sic_code >= 3840 and sic_code <= 3859:
        classification = '10 Healthcare -- Healthcare, Medical Equipment, and Drugs'
    elif sic_code >= 8000 and sic_code <= 8099:
        classification = '10 Healthcare -- Healthcare, Medical Equipment, and Drugs'
    elif sic_code >= 8000 and sic_code <= 8099:
        classification = '11 Finance -- Money, Banking, Insurance, Real Estate'
    else:
        classification = '12 Other -- Mines, Constr, BldMt, Trans, Hotels, Bus Serv, Entertainment'
      
    return classification