import system

def uk_clothes_system():
    s = System("UK Clothes")

    imports         = s.add_process("Imports", 1461)
    uk_production   = s.add_process("UK Production", 177)
    arising         = s.add_process("Arisings", Process.UNKNOWN_SIZE)
    consumption     = s.add_process("Consumption", Process.UNKNOWN_SIZE)
    collected       = s.add_process("Collected", 594)
    residual_waste  = s.add_process("Residual Waste", Process.UNKNOWN_SIZE)
    unnacounted     = s.add_process("Unnacounted", Process.UNKNOWN_SIZE)
    new_exports     = s.add_process("New Exports", 249)
    reused_uk       = s.add_process("Reused UK", Process.UNKNOWN_SIZE)
    used_exports    = s.add_process("Used Exports", Process.UNKNOWN_SIZE)
    incineration    = s.add_process("Incineration", Process.UNKNOWN_SIZE)
    landfill        = s.add_process("Landfill", Process.UNKNOWN_SIZE)
    other_treatment = s.add_process("Other Treatment", Process.UNKNOWN_SIZE)
    disposed_non_uk = s.add_process("Disposed Non-UK", Process.UNKNOWN_SIZE)
    downcycled      = s.add_process("Downcycled", Process.UNKNOWN_SIZE)
    reused_non_uk   = s.add_process("Reused Non-UK", Process.UNKNOWN_SIZE)

    s.add_flow(imports, arisings, imports.size * 0.8, False)  # so False means this data is a proportion?
    s.add_flow(imports, disposed_non_uk, imports.size * 0.2, False)
    s.add_flow(uk_production, arisings, 0.8, False)
    s.add_flow(uk_production, residual_waste, 0.2, False)
    s.add_flow(consumption, reused_uk, 72, True)  # and True means this data is a mass?
    s.add_flow(consumption, KB_waste, 245, True)
    s.add_flow(consumption, HWRC, 91, True)
    s.add_flow(collected, reused_uk, 0.32, False)
    s.add_flow(collected, used_exports, 0.6, False)
    s.add_flow(collected, downcycled, 0.03, False)
    s.add_flow(collected, residual_waste, 0.05, False)
    s.add_flow(used_exports, reused_non_uk, 0.6, False)
    s.add_flow(used_exports, disposed_non_uk, 0.4, False)
    s.add_flow(residual_waste, incineration, 0.76, False)
    s.add_flow(residual_waste, landfill, 0.19, False)
    s.add_flow(residual_waste, other_treatment, 0.05, False)
        # ...
    collection_flow = s.add_flow(arisings, collected, 594, False)
    s.split_flow(arisings, collected, ["Charity Shops", "Textile Banks", "Other Collection"], [285, 220, collection_flow.amount - (285 + 220)], False)

    return s
