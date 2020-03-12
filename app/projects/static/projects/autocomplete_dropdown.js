function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
}




var plant_ids = ["AMH_Expansion", "ANS_Compound", "ANT_NA5", "ANT_NB", "ANT_AA4", "ANT_AA7", "ANT_Ammonia", "ANT_Anilin", "ANT_Anolon", "ANT_FA", "ANT_HXA", "ANT_MDI", "ANT_MA", "ANT_PO", "ANT_PA", "ANT_PEOL", "ANT_PIB", "ANT_SA", "ANT_Soda", "ANT_SAP", "ANV_Admix", "ALF_System", "ALM_Admix", "ALT_Dispersions", "AUG_Disp", "AUG_Powders", "BAL_Pharma", "BAR_Admix", "BES_B1", "BES_B2", "BGP_Admix", "BIS_Ibuprofen", "BMP_Admix", "BMT_DMTA", "BOX_System", "BRI_Seal", "BRS_Wallcoat", "BSW_WBP", "BSW_PEOL", "BSW_System", "BSW_Ultradur", "BSW_Strobilurin", "BSW_Azol", "BSW_Energy", "BSW_Entsorgung", "BUK_Admix", "BZC_System", "CAB_Powders", "CAG_Admix", "CAL_Polymers", "CHR_PD", "CIE_Admix", "CIK_Admix", "CIN_APG", "CEN_Polymer", "CHA_Polymer", "CLM_System", "CON_Agro", "CON_Dispersion", "CON_Palatal", "CTH_NBC", "DAH_Cellasto", "DEM_Paint", "DEM_Resin", "DEM_Plant1", "DEM_Suvinil", "DEN_Admix", "DMM_Admix", "DUD_System", "DUJ_Admix", "DIL_Mixing", "DME_Catalysts", "ELY_Catalysts", "ERI_Catalysts", "ESE_HVIngr", "EVR_Admix", "FMT_TCPL", "FRE_Acrylates", "FRE_Anolon 1", "FRE_Anone 2", "FRE_Capro1", "FRE_Capro2", "FRE_HDO", "FRE_HA", "FRE_NPG", "FRE_Syngas", "FRE_Util", "GEB_Admix", "GEB_Powder", "GEB_Resin", "GEI_BDO", "GEI_CCU", "GEI_EO", "FRE_Oxo", "FRE_Poly", "FRE_SAP", "GEI_PEOL", "GEI_PVP", "GEI_Pyrrolidon", "GEI_Surf", "GEI_THF", "STF_Admix", "GRL_Dispersion", "GRA_Form", "GEN_Form", "GUA_NaMeth", "GUI_CatalystsE", "GUN_VitB", "GUR_Admix", "HAM_Powders", "HAN_CPP", "HAN_IMI1", "HAN_IMI2", "GUA_Form", "GUA_2EHA", "GUA_Disp", "GUA_Pigment", "HAN_Prowl", "HAN_Pyrroles", "HAR_Mica", "HCM_Admix", "HER_Prod", "HMI_Dispersions", "HMM_Powders", "HOU_System", "HOW_Admix", "HUN_CCN", "HUN_HD", "HUN_LD", "HUT_NBC", "HUZ_PPP", "CHI_BDO", "IND_Catalysts", "JIL_NPG", "KAO_UVAbs", "KMH_Masterbatch", "KNT_Admix", "KRG_Admix", "KRT_Admix", "KUA_2EHA", "KUA_CAA", "KYI_AcidP", "LEU_Comp", "LIV_System", "LU_HPPS_A209", "LU_Finish", "LU_Vitamin", "LU_Waterworks", "LU_AmmoniaUltra", "LU_Trockenbetriebe", "LU_Alkoholate", "LU_Trilon", "LU_Phthalo", "LU_PTHF", "LU_EMCE", "LU_Hydrosulf2", "LU_Acrolein", "LU_B108", "LU_HPPS_B218", "LU_Uviflex", "LU_NitrilN", "LU_NitrilS", "LAT_Admix", "LEM_Cellasto", "LU_Muehle", "LU_Isophytol", "LU_Indol", "LU_Kammer", "LU_Butylacrylate", "LU_Acrylester2", "LU_TMH1", "LU_PluriolS", "LU_PO", "LU_PluriolN", "LU_Hydrosulf1", "LU_Uvinul", "LU_UltramidA2", "LU_Biopoly", "LU_Comp3", "LU_Cdon", "LU_WasteIncin", "LU_IPC", "LU_Dicarbon", "LU_Citral", "LU_SAF", "LU_Geraniol", "LU_Panton", "LU_Phytase", "LU_Carotinoid", "LU_SokalanS", "LU_Ammoniak3", "LU_Ammoniak4", "LU_GasComp", "LU_Budimat", "LU_Netzschwefel", "LU_AMN", "LU_Ammoncarb", "LU_CIP", "LU_Eisenrot", "LU_NPG", "LU_Oppanol", "LU_Formol", "LU_Oxo", "LU_Urea", "LU_AirSep", "LU_CO2", "LU_BF", "LU_Infinergy", "LU_Basonat", "LU_SCF", "LU_Acetylene1", "LU_Syngas", "LU_Imin", "LU_NH4OH", "LU_Methanol", "LU_SAP", "LU_Acrylester3", "LU_AMS", "LU_DEKA", "LU_Hydramin", "LU_Vinylether", "LU_Styropor", "LU_Spez", "LU_Comp5", "LU_Polystyrol", "LU_Traenkharz", "LEM_System", "LU_Capro", "LU_EO", "LU_Lutensol", "LU_Lackharz", "LU_Basoplast", "LU_Styrodur", "LU_PSA", "LU_Adipin", "LU_WM", "LU_Butyl", "LU_Salmiak", "MAL_Alkox", "MAL_PhyOp", "MAL_MPR", "MAN_Dispersion", "LU_Dispersions", "LU_TEDA", "LU_Colorplast", "LU_Monoether", "LU_PEWax", "MCI_Formgiving", "MCI_Irgafos", "MCI_Irganox", "MCI_Tinuvin", "MCI_HALS", "LU_Ultrason", "LU_Power", "MEJ_Admix", "MER_Dispersions", "MID_Daveyville", "MID_EdgarEV", "MID_Gordon", "MID_Toddville", "MIT_System", "MLK_System", "MOD_PO_SM", "MTH_Cibafast", "MTH_BAT_347", "MTH_BAT_369A", "MTH_BAT_369B", "MTH_BAT_447", "MTW_Wallcoat", "MUN_Gx4CC", "MUN_Gx5", "MUN_RC", "MUN_LH", "NAN_CAA", "NAN_Aromatics", "NAN_C4", "NAN_Cracker", "NAN_EBSM", "NAN_Syngas", "NAN_NIS", "NAN_LDPEEVA", "NAN_Power", "NCH_Pigments", "NEW_Finishing", "NEW_Metasheen", "NEW_Synthesis", "NLG_Admix", "NMB_Admix", "NSH_Pesol", "NSK_Admix", "NSN_System", "NWK_Wallcoat", "OLD_Paint", "ORA_System", "NIP_Catalysts", "PEL_Coating", "PEK_OCM", "PEL_Slurry", "PEK_Specialty", "PGD_Comp", "PHO_Admix", "PON_UTS1", "PON_UTS2", "PTA_CrackerC4", "PTA_SABINA", "PUL_HVIngr", "QUI_Clay", "RAY_SAP", "RDK_Admix", "RED_PR", "ROM_Catalysts", "RYN_Admix", "PUE_Lube", "PUE_LS", "SDC_Admix", "SEN_Metals", "SEN_Catalysts", "SEV_Admix", "SHK_DNT", "SHK_MMDI", "SHK_NA", "SHE_Vitamin", "SHEV_AO", "SHI_Cellasto", "SHI_System", "SHMD_PCE", "SHMP_Admix", "SHP_ACR", "SHP_AUX", "SHP_Cellasto", "SHP_Comp", "SHP_System", "SHQI_ElMat", "SMG_Admix", "SNZ_Wood", "SOR_Powders", "SPT_Comp", "STB_Powders", "SHEC_Paint1", "SHP_MCD", "WSH_MPP", "SWI_Admix", "TAR_Disp", "TAR_FFP", "TAR_PDH", "TAR_Resins", "TAR_KM", "VID_Catalysts", "VPR_Admix", "WAS_Alkox", "WHT_Alkox", "WHY_Algae", "WID_PestCtl", "TKA_Enamel", "TOE_System", "TOR_Solvent1", "TPC_Admix", "TUL_Paint", "ULN_AZO", "ULN_Phthalo", "ULP_SpecFoams", "TKA_Resin", "ULS_PEOL", "ULS_PTHF", "WST_Admix", "WTB_Powders", "WME_P1", "WME_P2", "WYA_TPU", "YEO_Aniline", "YEO_CCD", "YEO_DNT", "YEO_HYCO", "WYA_Cellasto", "WYA_EPC", "YEO_MDI", "YEO_MNB", "YEO_TDI", "YKK_TPU", "YOK_Dispersion", "ZIN_PESOL", "ZHJ_Dispersions", "WYA_PEOL", "YEO_System", "BMT_Infra", "CEN_Infrastructure", "BLA_System", "BES_Infra", "ACW_Wallcoat", "DIL_Infra", "DEM_Infra", "GEI_Util", "GRE_Infrastructure", "GUA_Infra", "HAN_Infra", "MAN_Infra", "KUA_Util", "NAN_Utilities", "NEW_Utilities", "MCI_Utilities", "PON_Infra", "PAP_Infra", "PEK_Infra", "SEN_Infra", "PUE_Utilities", "SAV_Catalysts", "ROM_Infra", "WYA_Infra", "YEO_Infra1", "YEO_Infra2", "WME_Utilities", "TKA_Infra", "THA_Infra", "TAR_Infra", "SHP_Utl", "BSW_TDI", "BSW_PESOL", "BSW_Basotect", "BSW_Toluidin", "LU_WaterPur", "LU_SulfAcPl", "LU_SulfAcReg", "LU_Sulfite", "LU_Sulfide", "LU_EDC", "LU_N2OIso", "LU_Xneopor", "LU_HCl", "LU_AlCl", "LU_FeCl", "LU_SPA", "LU_SABMix", "LU_Basonal", "LU_AHSalt", "LU_UltramidBS", "LU_UltramidB1", "LU_Coolants", "LU_SVM", "LU_BDO2", "LU_UltramidB2", "LU_BDO1", "LU_AcetylenePur", "LU_SVA", "LU_NeoporPl", "LU_Basotect", "LU_SM", "LU_EB", "LU_ZwiProDist", "LU_Anthranil", "LU_ThiuramPl", "LU_TamolPl", "LU_BentazonPl", "LU_Sulfonate", "LU_SokalanN", "LU_Oxamin", "LU_EOA", "LU_Keropur", "LU_Keton", "LU_Schwersoda", "LU_IMI", "LU_Xemium", "LU_LysmeralPl", "LU_TBA", "LU_Sicotrans", "LU_Lackfarben", "LU_Heliogen", "LU_Butadiene", "LU_Aromatics", "LU_Formamide", "LU_PropionicAc", "LU_Pentyl", "LU_MIM", "LU_Keten", "LU_FormicAc", "LU_NA", "LU_NSaltsPl", "LU_HOKONA", "LU_NOREIN", "LU_Melamine", "MON_Coater", "GEI_PTHF", "FRE_AAE23", "GEI_MDI", "MON_Acronal", "MON_Latex", "GEI_AcetylenePl", "SHC_THF", "SHC_PTHF", "LAM_EH", "LAM_FR", "LAM_LS", "LAM_MZ", "LAM_Irgafos168", "LAM_Extr", "LAM_MM", "KUA_BDO", "KUA_Syngas", "ANT_IB", "GUA_SintDiv", "ANT_ARO", "ANT_Cracker", "GUA_Trilon", "GUA_Coolants", "ANT_CAR", "NIE_Slurry", "ANT_Alkox", "ANT_CAS", "NIE_Coating", "ANT_EO", "NAN_Oxo", "NAN_PIB", "KUA_Oxo", "NAC_EFKA", "THA_Phenol", "THA_Naphthal", "THA_Coolants", "MAN_MicroN", "MAN_Neozapon", "MAN_Eukesolar", "TRV_Powder", "FIN_MPR", "FIN_Sulfat", "DUS_OrgPast", "DUS_CSulfAPG", "DUS_SpecSulf", "MEA_MPR", "KAN_Sulfat", "KAN_MPR", "LU_Glykol", "KAN_VitE", "KAN_Infra", "FTL_Palusol", "JAC_Sulfat", "JAC_MPR", "BMT_Dicamba", "SHK_TDI", "SHC_Paint2", "MAN_Paint", "MAN_Resin", "WIN_Paint", "CLE_Paint", "CLE_Resin", "GRE_Clearcoat", "PAV_Paint", "WUE_Paint", "CHQ_Anilin", "NAN_GAA", "KAI_Util", "HNG_Util", "JAB_Paint", "NAN_EO", "JAB_Resins", "NAN_Acrylates", "SPA_Form", "NAN_PA", "ANT_HP", "GDJ_ResinEC", "CAY_MPR", "NAN_MA", "NAN_EA", "DUS_Finishing", "NAN_DMA3", "NAN_FA", "ANT_Anondest", "CAY_Sulfat", "RII_Admix", "TRV_Poly", "GDJ_EB", "ILL_P1", "ILL_P2", "ILL_Infra", "MUN_Infra", "SHC_PGM", "WUE_Infra", "DAY_Dispersions", "JAC_Infra", "CAM_Infra", "GRL_Infra", "CON_Infra", "MEA_Photomer", "MEA_Infra", "ZAC_Prod1", "ZAC_Prod2", "WSH_Pilot", "GRF_Microfilt", "RUD_Comp", "LU_WWTP", "PLO_Admix", "SDI_Admix", "MTP_Alkox", "JED_Admix", "SAK_Admix", "NGN_Admix", "ALG_Admix", "ADA_Admix", "ZFR_MPR", "MYS_Admix", "PPC_Admix", "ITA_Admix", "SIT_Admix", "KNO_Admix", "CLL_Prod", "NGO_Admix", "CHW_CSB", "AUK_Admix", "SHZ_Admix", "LAC_Admix", "ROS_Admix", "POO_Admix", "CHQ_MDI", "TAK_Admix", "OOS_Admix", "TBZ_Admix", "BUC_Pigment", "MRK_Admix", "LIM_Admix", "SIC_Prod", "KRS_Admix", "KAW_Admix", "AST_Admix", "CAS_MPR", "KTK_Admix", "KAG_Admix", "TJH_System", "NGY_Admix", "AMM_Admix", "CRK_Prod", "NAC_Monomer", "FUK_Admix", "BPK_Sulfat", "HIR_Admix", "ALL_Admix", "AMS_FFP", "AML_Landscape", "ANT_Amines", "APP_CF", "ATT_Catalysts", "BPK_MPR", "BGP_System", "RUB_System", "BOU_CLA", "BRA_DBR", "CSB_Admix", "CHA_Amnicola", "CIM_MPR", "CIM_Sulfat", "CIN_MPR", "CLY_Admix", "COR_Prod", "DUS_Industry", "DUS_FOH", "DUS_Alkox", "DUS_MPR", "DUS_Silicates", "ELB_Dimoxy", "ELB_Disulfur", "ELB_Fipronil", "DIL_Polym", "GEI_GA", "GEI_TDI", "GEI_Anilin", "GEI_MNB", "GEI_Amines2", "GEI_Amines1", "NGE_DNT", "GRZ_HVIngr", "GDJ_Paint", "GDJ_Utilities", "GUA_MPB", "HUA_UGC", "HNG_Pigments", "KTT_PhyOp", "KTT_MPR", "KUA_PBT", "LER_System", "LU_Kaurit", "LU_Electroly2", "LU_AmmNit", "LU_AgFert", "LU_CatalystsA", "LU_CatalystsB", "LU_CatalystsD", "LU_SCD", "LU_Cracker", "LU_THTPA", "LU_ThionPl", "LU_MSA", "MAA_Micranyl", "MAA_Microlen", "MLC_System", "MAN_Admix", "MAN_Catalysts", "MTH_DSBP", "NAN_PS", "NAC_PAM", "NSH_System", "THA_Comp", "THA_System", "PAP_Plasticizer", "CUC_Admix", "STO_Inoculants", "BSW_Syngas", "BSW_Laromer", "BSW_PBT", "SHC_BPI", "SHJ_APG", "SHJ_Alkox", "SHJ_Defoam", "SHJ_LTRMPR", "SHJ_HTR", "SHJ_Sulfat", "SOM_Inoculants", "SLM_Admix", "STL_PCS", "ULS_System", "VIL_System", "WYA_Resins", "YEO_Ultrason", "ZIN_System", "SJO_AgProd", "CLW_AgProd", "LHM_Innoculants", "DRB_Biofungi", "SDF_Omega3", "LNC_Admix", "POD_Admix", "SGS_Admix", "BOU_Infra", "BSW_Neopolen", "GUA_System", "GUA_Cellasto", "LU_DHDPS", "NSH_Cellasto", "CAM_SAP", "JAC_SprayDry", "GUA_PESOL", "PUD_Admix", "ANT_CapTab", "GUA_Emulsions", "TRO_PCE", "EAF_Admix", "DHK_Admix", "KAI_Admix", "BOU_FaAlc", "MEA_Synlubes", "ZFR_Sulfat", "ZFR_Amid", "LMO_CheAg", "LU_TDI", "LAM_ESCl", "KYI_Conti", "GRZ_Util", "NAC_Infra", "DIL_Dispersions", "BIS_4HAP", "NEL_Admix", "THA_AUX_SP", "ELY_LiB", "CIF_Metals", "LIN_Metals", "KAZ_Admix", "MID_EdgarCC", "LAM_BTZ", "SAS_Inoculants", "YES_Comp", "FRE_Disp", "KEM_SulfAc", "LU_HXA", "ALT_Comp", "GEI_GBL", "GEI_NMP", "NAN_SAP", "TOE_Coatings", "SHJ_Infra", "SIN_EC", "SHC_PA", "DAH_Dispersions", "DAH_PEOL", "DAH_MDI", "DAH_PESOL", "DAH_System", "DAH_Infra", "SIJ_Infra", "NAN_NPG", "MLC_Pesol", "ROM_Metals", "FIN_Infra", "NAI_Admix", "KUA_GAA", "KUA_BA", "ANT_BD", "LAM_OilAd", "KWI_Admix", "MEA_Sulfat", "CAY_Infra", "RDG_FPP", "NAC_tBA", "NAC_PEA", "DUR_Disp", "LOU_Colorants", "NGE_System", "MNT_Form", "CIN_Infra", "LAG_Admix", "PGD_Disp", "SHC_Resin", "TAI_H2SO4", "DUS_Blending", "BGP_Paint", "KAI_Synthesis", "KAI_FormGiv", "THA_AUX_EP", "DAH_Sulfat", "DAH_MPR", "DAH_TTD", "SOO_CAM", "KKY_CAM", "CHH_TPU", "CAM_GAA", "CAM_BA", "DUS_Spray", "GRE_Paste", "GRE_Resin", "SIJ_Irganox", "SIJ_Irgafos", "SIJ_Blends", "SHCC_HD", "SHCC_Coating", "SHCC_Slurry", "GEI_FormicAc", "SHP_Polym", "SHP_Synlube", "JXZ_ElMat", "MAM_INA", "THD_Trilon", "SHC_Catalysts", "MAA_Blending", "MWC_Catalysts", "KYI_Metal", "SPB_Admix", "ANT_Zandvliet", "KUA_2EHAcid", "HNV_Admix", "KOR_THF", "KGP_Admix", "KYI_Infra", "CRM_Admix", "LU_DicarbLsg", "SPG_Admix", "SRS_Coating", "SRS_Slurry", "LU_PAG", "ILL_FP", "YEO_NH4OH", "KND_Admix", "KUA_PIB", "SHJ_MPR", "AUC_SurfTreat", "KUA_Citral", "KUA_Menthol", "MSC_Admix", "WYA_Infinergy", "BSW_Ultramid", "ANT_Util", "BAY_SurfTreat", "JUN_SurfTreat", "SHCH_SurfTreat", "CGC_SurfTreat", "MGL_SurfTreat", "CAN_SurfTreat", "SNS_SurfTreat", "SOI_SurfTreat", "CHC_SurfTreat", "PNE_SurfTreat", "GIU_SurfTreat", "QRE_SurfTreat", "SNC_SurfTreat", "CAC_SurfTreat", "JBT_SurfTreat", "BKS_SurfTreat", "LNG_SurfTreat1", "LNG_SurfTreat2", "BTC_LiB", "SHP_Catalysts", "NAC_MPPN", "EDG_Admix", "JNM_Paint", "RYH_Catalysts", "THD_ACM", "REG_FFP", "MKO_GA", "FRA_GA", "KNA_PSM34", "KNA_PSM5", "SHC_Blends", "SHC_Irgafos", "SHC_Irganox", "PRM_VegSeed", "DAH_Coolants", "BAP_Seed", "DWI_Seed", "LBB_Seed", "LTF_Seed", "STV_Seed", "SHF_Seed", "MLBS_Seed", "LBR_Seed", "CHH_Infinergy", "LEM_TPU", "LEM_Infinergy", "SHP_TPU", "SHP_Infinergy", "GUI_CatalystsN", "LU_PVPMP", "LU_MPPl", "LU_CoviplasPl", "LU_PVPCovi", "LU_PVPLutonal", "LU_LutonalPl", "FRE_PAM", "CVS_Metals", "SHA_Comp", "PAN_Comp", "ULO_Comp", "ULO_PA66", "ULO_ADA", "ROU_Catalysts", "CHM_ADA", "CHM_HMDA", "FRB_PA66", "POT_Comp", "BTS_PA66", "GEL_Isobionics"]
/*initiate the autocomplete function on the "myInput" element, and pass along the array as possible autocomplete values:*/
autocomplete(document.getElementById("id_plant_name"), plant_ids);
