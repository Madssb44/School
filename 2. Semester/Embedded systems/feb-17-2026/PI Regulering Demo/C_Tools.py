
###################################################################################################
# Brief         Calculates Gain (A) and Offset (B) for a linear equation: y = Ax + B
#               Insert two sets of x and y values
#
# Param[in]     fX_low, fX_high: The two known X-values
#               fY_low, fY_high: The two known Y-values
# Return        fGain:          Gain factor (A)
#               fOffset:        Offset value (B)
#
# Warning       None
###################################################################################################
def C_Tools_TwoSimultaneousParameters( fX_low, fX_high, fY_low, fY_high):
    fRetVal_Gain = 1
    fRetVal_Offset = 0
    
    # If the two measured values are the same, it does not make sense to calculate Gain and Offset
    # Simply set Gain = 1 and Offset = 0 (set as default values above)
    if fX_low != fX_high:
        # Beregn x og y vha
        fRetVal_Gain = (fY_low - fY_high) / (fX_low - fX_high)
        fRetVal_Offset = (fX_low * fY_high - fY_low * fX_high) / (fX_low - fX_high)
    
    return fRetVal_Gain, fRetVal_Offset
