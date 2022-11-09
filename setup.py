import system

def uk_clothes_system():
    s = System("UK Clothes")

    imports         = s.add_process("Imports", 1461)
    uk_production   = s.add_process("UK Production", 117)
    arising         = s.add_process("Arisings", 1312)
    consumption     = s.add_process("Consumption", 1063)
    collected       = s.add_process("Collected", 594)
    residual_waste  = s.add_process("Residual Waste", 401)
    unnacounted     = s.add_process("Unnacounted", Process.UNKNOWN_SIZE)
    new_exports     = s.add_process("New Exports", 249)
    reused_uk       = s.add_process("Reused UK", 249)
    used_exports    = s.add_process("Used Exports", 357)
    incineration    = s.add_process("Incineration", Process.UNKNOWN_SIZE)
    landfill        = s.add_process("Landfill", Process.UNKNOWN_SIZE)
    other_treatment = s.add_process("Other Treatment", Process.UNKNOWN_SIZE)
    disposed_non_uk = s.add_process("Disposed Non-UK", 435)
    downcycled      = s.add_process("Downcycled", 18)
    reused_non_uk   = s.add_process("Reused Non-UK", 18)

    s.add_flow(imports, arisings, imports.size * 0.8, False)
    s.add_flow(imports, disposed_non_uk, imports.size * 0.2, False)
    s.add_flow(uk_production, arisings, 0, False) # How much is this? I don't actually have any of these numbers
    # ...
    collection_flow = s.add_flow(arisings, collected, 594, False)
    s.split_flow(arisings, collected, ["Charity Shops", "Textile Banks", "Other Collection"], [285, 220, collection_flow.amount - (285 + 220)], False)

    return s
