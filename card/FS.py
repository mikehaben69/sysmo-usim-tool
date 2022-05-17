# -*- coding: UTF-8 -*-
"""
card: Library adapted to request (U)SIM cards and other types of telco cards.
Copyright (C) 2010 Benoit Michau

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

#################################
# 3GPP SIM and USIM File-System #
# see TS 51.11 for SIM          #
# see TS 31.102 for USIM        #
#################################

# (U)SIM file-system dictionnaries
# (absolut_file_address) : 'file_name'

SIM_FS = {
(0x3F, 0x00) : 'MF',
(0x2F, 0xE2) : 'EF_ICCID',
(0x2F, 0x05) : 'EF_PL',
(0x7F, 0x23) : 'DF_FP-CTS',
(0x7F, 0x22) : 'DF_IS-41',
(0x7F, 0x10) : 'DF_TELECOM',
(0x7F, 0x10, 0x6F, 0x3A) : 'EF_ADN',
(0x7F, 0x10, 0x6F, 0x3B) : 'EF_FDN',
(0x7F, 0x10, 0x6F, 0x3C) : 'EF_SMS',
(0x7F, 0x10, 0x6F, 0x3D) : 'EF_CCP',
(0x7F, 0x10, 0x6F, 0x40) : 'EF_MSISDN',
(0x7F, 0x10, 0x6F, 0x42) : 'EF_SMSP',
(0x7F, 0x10, 0x6F, 0x43) : 'EF_SMSS',
(0x7F, 0x10, 0x6F, 0x44) : 'EF_LND',
(0x7F, 0x10, 0x6F, 0x47) : 'EF_SMSR',
(0x7F, 0x10, 0x6F, 0x49) : 'EF_SDN',
(0x7F, 0x10, 0x6F, 0x4A) : 'EF_EXT1',
(0x7F, 0x10, 0x6F, 0x4B) : 'EF_EXT2',
(0x7F, 0x10, 0x6F, 0x4C) : 'EF_EXT3',
(0x7F, 0x10, 0x6F, 0x4D) : 'EF_BDN',
(0x7F, 0x10, 0x6F, 0x4E) : 'EF_EXT4',
(0x7F, 0x10, 0x6F, 0x58) : 'EF_CMI',
(0x7F, 0x10, 0x6F, 0x4F) : 'EF_ECCP',
(0x7F, 0x10, 0x5F, 0x50) : 'DF_GRAPHICS',
(0x7F, 0x10, 0x5F, 0x50, 0x4F, 0x20) : 'EF_IMG',
(0x7F, 0x20) : 'DF_GSM',
(0x7F, 0x20, 0x5F, 0x3C) : 'DF_MExE',
(0x7F, 0x20, 0x5F, 0x3C, 0x4F, 0x40) : 'EF_MExE-ST',
(0x7F, 0x20, 0x5F, 0x3C, 0x4F, 0x41) : 'EF_ORPK',
(0x7F, 0x20, 0x5F, 0x3C, 0x4F, 0x42) : 'EF_ARPK',
(0x7F, 0x20, 0x5F, 0x3C, 0x4F, 0x43) : 'EF_TPRPK',
(0x7F, 0x20, 0x5F, 0x30) : 'DF_IRIDIUM',
(0x7F, 0x20, 0x5F, 0x31) : 'DF_GLOBALSTAR',
(0x7F, 0x20, 0x5F, 0x32) : 'DF_ICO',
(0x7F, 0x20, 0x5F, 0x33) : 'DF_ACeS',
(0x7F, 0x20, 0x5F, 0x40) : 'DF_EIA/TIA-553',
(0x7F, 0x20, 0x5F, 0x60) : 'DF_CTS',
(0x7F, 0x20, 0x5F, 0x70) : 'DF_SoLSA',
(0x7F, 0x20, 0x5F, 0x70, 0x4F, 0x30) : 'EF_SAI',
(0x7F, 0x20, 0x5F, 0x70, 0x4F, 0x31) : 'EF_SLL',
(0x7F, 0x20, 0x6F, 0x05) : 'EF_LP',
(0x7F, 0x20, 0x6F, 0x07) : 'EF_IMSI',
(0x7F, 0x20, 0x6F, 0x20) : 'EF_Kc',
(0x7F, 0x20, 0x6F, 0x2C) : 'EF_DCK',
(0x7F, 0x20, 0x6F, 0x30) : 'EF_PLMNsel',
(0x7F, 0x20, 0x6F, 0x31) : 'EF_HPLMN',
(0x7F, 0x20, 0x6F, 0x32) : 'EF_CNL',
(0x7F, 0x20, 0x6F, 0x37) : 'EF_ACMmax',
(0x7F, 0x20, 0x6F, 0x38) : 'EF_SST',
(0x7F, 0x20, 0x6F, 0x39) : 'EF_ACM',
(0x7F, 0x20, 0x6F, 0x3E) : 'EF_GID1',
(0x7F, 0x20, 0x6F, 0x3F) : 'EF_GID2',
(0x7F, 0x20, 0x6F, 0x41) : 'EF_PUCT',
(0x7F, 0x20, 0x6F, 0x45) : 'EF_CBMI',
(0x7F, 0x20, 0x6F, 0x46) : 'EF_SPN',
(0x7F, 0x20, 0x6F, 0x48) : 'EF_CBMID',
(0x7F, 0x20, 0x6F, 0x74) : 'EF_BCCH',
(0x7F, 0x20, 0x6F, 0x78) : 'EF_ACC',
(0x7F, 0x20, 0x6F, 0x7B) : 'EF_FPLMN',
(0x7F, 0x20, 0x6F, 0x7E) : 'EF_LOCI',
(0x7F, 0x20, 0x6F, 0xAD) : 'EF_AD',
(0x7F, 0x20, 0x6F, 0xAE) : 'EF_PHASE',
(0x7F, 0x20, 0x6F, 0xB1) : 'EF_VGCS',
(0x7F, 0x20, 0x6F, 0xB2) : 'EF_VGCSS',
(0x7F, 0x20, 0x6F, 0xB3) : 'EF_VBS',
(0x7F, 0x20, 0x6F, 0xB4) : 'EF_VBSS',
(0x7F, 0x20, 0x6F, 0xB5) : 'EF_eMLPP',
(0x7F, 0x20, 0x6F, 0xB6) : 'EF_AAeM',
(0x7F, 0x20, 0x6F, 0xB7) : 'EF_ECC',
(0x7F, 0x20, 0x6F, 0x50) : 'EF_CBMIR',
(0x7F, 0x20, 0x6F, 0x51) : 'EF_NIA',
(0x7F, 0x20, 0x6F, 0x52) : 'EF_KcGPRS',
(0x7F, 0x20, 0x6F, 0x53) : 'EF_LOCIGPRS',
(0x7F, 0x20, 0x6F, 0x54) : 'EF_SUME',
(0x7F, 0x20, 0x6F, 0x60) : 'EF_PLMNwAcT',
(0x7F, 0x20, 0x6F, 0x61) : 'EF_OPLMNwAcT',
(0x7F, 0x20, 0x6F, 0x62) : 'EF_HPLMNAcT',
(0x7F, 0x20, 0x6F, 0x63) : 'EF_CPBCCH',
(0x7F, 0x20, 0x6F, 0x64) : 'EF_INVSCAN',
(0x7F, 0x20, 0x6F, 0xC5) : 'EF_PNN',
(0x7F, 0x20, 0x6F, 0xC6) : 'EF_OPL',
(0x7F, 0x20, 0x6F, 0xC7) : 'EF_MBDN',
(0x7F, 0x20, 0x6F, 0xC8) : 'EF_EXT6',
(0x7F, 0x20, 0x6F, 0xC9) : 'EF_MBI',
(0x7F, 0x20, 0x6F, 0xCA) : 'EF_MWIS',
(0x7F, 0x20, 0x6F, 0xCB) : 'EF_CFIS',
(0x7F, 0x20, 0x6F, 0xCC) : 'EF_EXT7',
(0x7F, 0x20, 0x6F, 0xCD) : 'EF_SPDI',
(0x7F, 0x20, 0x6F, 0xCE) : 'EF_MMSN',
(0x7F, 0x20, 0x6F, 0xCF) : 'EF_EXT8',
(0x7F, 0x20, 0x6F, 0xD0) : 'EF_MMSICP',
(0x7F, 0x20, 0x6F, 0xD1) : 'EF_MMSUP',
(0x7F, 0x20, 0x6F, 0xD2) : 'EF_MMSUCP',
}

USIM_FS = {
(0x3F, 0x00) : 'MF',
(0x2F, 0x00) : 'EF_DIR',
(0x2F, 0x05) : 'EF_PL',
(0x2F, 0x06) : 'EF_ARR',
(0x2F, 0xE2) : 'EF_ICCID',
(0x7F, 0x20) : 'DF_GSM',
(0x7F, 0x10) : 'DF_TELECOM',
(0x7F, 0x10, 0x6F, 0x06) : 'EF_ARR',
(0x7F, 0x10, 0x6F, 0x3A) : 'EF_ADN',
(0x7F, 0x10, 0x6F, 0x3B) : 'EF_FDN',
(0x7F, 0x10, 0x6F, 0x3C) : 'EF_SMS',
(0x7F, 0x10, 0x6F, 0x4F) : 'EF_ECCP',
(0x7F, 0x10, 0x6F, 0x40) : 'EF_MSISDN',
(0x7F, 0x10, 0x6F, 0x42) : 'EF_SMSP',
(0x7F, 0x10, 0x6F, 0x43) : 'EF_SMSS',
(0x7F, 0x10, 0x6F, 0x44) : 'EF_LND',
(0x7F, 0x10, 0x6F, 0x47) : 'EF_SMSR',
(0x7F, 0x10, 0x6F, 0x49) : 'EF_SDN',
(0x7F, 0x10, 0x6F, 0x4A) : 'EF_EXT1',
(0x7F, 0x10, 0x6F, 0x4B) : 'EF_EXT2',
(0x7F, 0x10, 0x6F, 0x4C) : 'EF_EXT3',
(0x7F, 0x10, 0x6F, 0x4D) : 'EF_BDN',
(0x7F, 0x10, 0x6F, 0x4E) : 'EF_EXT4',
(0x7F, 0x10, 0x6F, 0x53) : 'EF_RMA',
(0x7F, 0x10, 0x6F, 0x54) : 'EF_SUME',
(0x7F, 0x10, 0x5F, 0x50) : 'DF_GRAPHICS',
(0x7F, 0x10, 0x5F, 0x50, 0x4F, 0x20) : 'EF_IMG',
#(0x7F, 0x10, 0x5F, 0x50, 0x4F, 0xXX) : 'EF_IIDFn',
(0x5F, 0x3A) : 'DF_PHONEBOOK',
(0x5F, 0x3A, 0x4F, 0x30) : 'EF_PBR',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_IAP',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_ADN',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_EXT1',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_PBC',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_GRP',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_AAS',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_GAS',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_ANR',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_SNE',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_CCP1',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_UID',
(0x5F, 0x3A, 0x4F, 0x22) : 'EF_PSC',
(0x5F, 0x3A, 0x4F, 0x23) : 'EF_CC',
(0x5F, 0x3A, 0x4F, 0x24) : 'EF_PUID',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_EMAIL',
(0x5F, 0x3B) : 'DF_MULTIMEDIA',
(0x5F, 0x3B, 0x4F, 0x47) : 'EF_MML',
(0x5F, 0x3B, 0x4F, 0x48) : 'EF_MMDF',
}

# this MF_FS is a trick that concatenate SIM_FS and USIM_FS
# useful when bruteforcing the FS under MF whatever the type of card selected
MF_FS = {
(0x3F, 0x00) : 'MF',
(0x2F, 0x00) : 'EF_DIR',
(0x2F, 0x05) : 'EF_ELP',
(0x2F, 0x06) : 'EF_ARR',
(0x2F, 0xE2) : 'EF_ICCID',
(0x5F, 0x3A) : 'DF_PHONEBOOK',
(0x5F, 0x3A, 0x4F, 0x30) : 'EF_PBR',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_IAP',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_ADN',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_EXT1',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_PBC',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_GRP',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_AAS',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_GAS',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_ANR',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_SNE',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_CCP1',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_UID',
(0x5F, 0x3A, 0x4F, 0x22) : 'EF_PSC',
(0x5F, 0x3A, 0x4F, 0x23) : 'EF_CC',
(0x5F, 0x3A, 0x4F, 0x24) : 'EF_PUID',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_EMAIL',
(0x5F, 0x3B) : 'DF_MULTIMEDIA',
(0x5F, 0x3B, 0x4F, 0x47) : 'EF_MML',
(0x5F, 0x3B, 0x4F, 0x48) : 'EF_MMDF',
(0x7F, 0x10) : 'DF_TELECOM',
(0x7F, 0x10, 0x6F, 0x06) : 'EF_ARR',
(0x7F, 0x10, 0x6F, 0x3A) : 'EF_ADN',
(0x7F, 0x10, 0x6F, 0x3B) : 'EF_FDN',
(0x7F, 0x10, 0x6F, 0x3C) : 'EF_SMS',
(0x7F, 0x10, 0x6F, 0x3D) : 'EF_CCP',
(0x7F, 0x10, 0x6F, 0x40) : 'EF_MSISDN',
(0x7F, 0x10, 0x6F, 0x42) : 'EF_SMSP',
(0x7F, 0x10, 0x6F, 0x43) : 'EF_SMSS',
(0x7F, 0x10, 0x6F, 0x44) : 'EF_LND',
(0x7F, 0x10, 0x6F, 0x47) : 'EF_SMSR',
(0x7F, 0x10, 0x6F, 0x49) : 'EF_SDN',
(0x7F, 0x10, 0x6F, 0x4A) : 'EF_EXT1',
(0x7F, 0x10, 0x6F, 0x4B) : 'EF_EXT2',
(0x7F, 0x10, 0x6F, 0x4C) : 'EF_EXT3',
(0x7F, 0x10, 0x6F, 0x4D) : 'EF_BDN',
(0x7F, 0x10, 0x6F, 0x4E) : 'EF_EXT4',
(0x7F, 0x10, 0x6F, 0x4F) : 'EF_ECCP',
(0x7F, 0x10, 0x5F, 0x50) : 'DF_GRAPHICS',
(0x7F, 0x10, 0x5F, 0x50, 0x4F, 0x20) : 'EF_IMG',
(0x7F, 0x10, 0x6F, 0x53) : 'EF_RMA',
(0x7F, 0x10, 0x6F, 0x54) : 'EF_SUME',
(0x7F, 0x10, 0x6F, 0x58) : 'EF_CMI',
(0x7F, 0x20) : 'DF_GSM',
(0x7F, 0x20, 0x5F, 0x3C) : 'DF_MExE',
(0x7F, 0x20, 0x5F, 0x3C, 0x4F, 0x40) : 'EF_MExE-ST',
(0x7F, 0x20, 0x5F, 0x3C, 0x4F, 0x41) : 'EF_ORPK',
(0x7F, 0x20, 0x5F, 0x3C, 0x4F, 0x42) : 'EF_ARPK',
(0x7F, 0x20, 0x5F, 0x3C, 0x4F, 0x43) : 'EF_TPRPK',
(0x7F, 0x20, 0x5F, 0x30) : 'DF_IRIDIUM',
(0x7F, 0x20, 0x5F, 0x31) : 'DF_GLOBALSTAR',
(0x7F, 0x20, 0x5F, 0x32) : 'DF_ICO',
(0x7F, 0x20, 0x5F, 0x33) : 'DF_ACeS',
(0x7F, 0x20, 0x5F, 0x40) : 'DF_EIA/TIA-553',
(0x7F, 0x20, 0x5F, 0x60) : 'DF_CTS',
(0x7F, 0x20, 0x5F, 0x70) : 'DF_SoLSA',
(0x7F, 0x20, 0x5F, 0x70, 0x4F, 0x30) : 'EF_SAI',
(0x7F, 0x20, 0x5F, 0x70, 0x4F, 0x31) : 'EF_SLL',
(0x7F, 0x20, 0x6F, 0x05) : 'EF_LP',
(0x7F, 0x20, 0x6F, 0x07) : 'EF_IMSI',
(0x7F, 0x20, 0x6F, 0x20) : 'EF_Kc',
(0x7F, 0x20, 0x6F, 0x2C) : 'EF_DCK',
(0x7F, 0x20, 0x6F, 0x30) : 'EF_PLMNsel',
(0x7F, 0x20, 0x6F, 0x31) : 'EF_HPLMN',
(0x7F, 0x20, 0x6F, 0x32) : 'EF_CNL',
(0x7F, 0x20, 0x6F, 0x37) : 'EF_ACMmax',
(0x7F, 0x20, 0x6F, 0x38) : 'EF_SST',
(0x7F, 0x20, 0x6F, 0x39) : 'EF_ACM',
(0x7F, 0x20, 0x6F, 0x3E) : 'EF_GID1',
(0x7F, 0x20, 0x6F, 0x3F) : 'EF_GID2',
(0x7F, 0x20, 0x6F, 0x41) : 'EF_PUCT',
(0x7F, 0x20, 0x6F, 0x45) : 'EF_CBMI',
(0x7F, 0x20, 0x6F, 0x46) : 'EF_SPN',
(0x7F, 0x20, 0x6F, 0x48) : 'EF_CBMID',
(0x7F, 0x20, 0x6F, 0x74) : 'EF_BCCH',
(0x7F, 0x20, 0x6F, 0x78) : 'EF_ACC',
(0x7F, 0x20, 0x6F, 0x7B) : 'EF_FPLMN',
(0x7F, 0x20, 0x6F, 0x7E) : 'EF_LOCI',
(0x7F, 0x20, 0x6F, 0xAD) : 'EF_AD',
(0x7F, 0x20, 0x6F, 0xAE) : 'EF_PHASE',
(0x7F, 0x20, 0x6F, 0xB1) : 'EF_VGCS',
(0x7F, 0x20, 0x6F, 0xB2) : 'EF_VGCSS',
(0x7F, 0x20, 0x6F, 0xB3) : 'EF_VBS',
(0x7F, 0x20, 0x6F, 0xB4) : 'EF_VBSS',
(0x7F, 0x20, 0x6F, 0xB5) : 'EF_eMLPP',
(0x7F, 0x20, 0x6F, 0xB6) : 'EF_AAeM',
(0x7F, 0x20, 0x6F, 0xB7) : 'EF_ECC',
(0x7F, 0x20, 0x6F, 0x50) : 'EF_CBMIR',
(0x7F, 0x20, 0x6F, 0x51) : 'EF_NIA',
(0x7F, 0x20, 0x6F, 0x52) : 'EF_KcGPRS',
(0x7F, 0x20, 0x6F, 0x53) : 'EF_LOCIGPRS',
(0x7F, 0x20, 0x6F, 0x54) : 'EF_SUME',
(0x7F, 0x20, 0x6F, 0x60) : 'EF_PLMNwAcT',
(0x7F, 0x20, 0x6F, 0x61) : 'EF_OPLMNwAcT',
(0x7F, 0x20, 0x6F, 0x62) : 'EF_HPLMNAcT',
(0x7F, 0x20, 0x6F, 0x63) : 'EF_CPBCCH',
(0x7F, 0x20, 0x6F, 0x64) : 'EF_INVSCAN',
(0x7F, 0x20, 0x6F, 0xC5) : 'EF_PNN',
(0x7F, 0x20, 0x6F, 0xC6) : 'EF_OPL',
(0x7F, 0x20, 0x6F, 0xC7) : 'EF_MBDN',
(0x7F, 0x20, 0x6F, 0xC8) : 'EF_EXT6',
(0x7F, 0x20, 0x6F, 0xC9) : 'EF_MBI',
(0x7F, 0x20, 0x6F, 0xCA) : 'EF_MWIS',
(0x7F, 0x20, 0x6F, 0xCB) : 'EF_CFIS',
(0x7F, 0x20, 0x6F, 0xCC) : 'EF_EXT7',
(0x7F, 0x20, 0x6F, 0xCD) : 'EF_SPDI',
(0x7F, 0x20, 0x6F, 0xCE) : 'EF_MMSN',
(0x7F, 0x20, 0x6F, 0xCF) : 'EF_EXT8',
(0x7F, 0x20, 0x6F, 0xD0) : 'EF_MMSICP',
(0x7F, 0x20, 0x6F, 0xD1) : 'EF_MMSUP',
(0x7F, 0x20, 0x6F, 0xD2) : 'EF_MMSUCP',
(0x7F, 0x23) : 'DF_FP-CTS',
(0x7F, 0x22) : 'DF_IS-41',
}

USIM_app_FS = {
(0x5F, 0x40) : 'DF_WLAN',
(0x5F, 0x40, 0x4F, 0x41) : 'EF_Pseudo',
(0x5F, 0x40, 0x4F, 0x42) : 'EF_UPLMNWLAN',
(0x5F, 0x40, 0x4F, 0x43) : 'EF_0PLMNWLAN',
(0x5F, 0x40, 0x4F, 0x44) : 'EF_USSIDL',
(0x5F, 0x40, 0x4F, 0x45) : 'EF_OSSIDL',
(0x5F, 0x40, 0x4F, 0x46) : 'EF_WRI',
(0x5F, 0x70) : 'DF_SoLSA',
(0x5F, 0x70, 0x4F, 0x30) : 'EF_SAI',
(0x5F, 0x70, 0x4F, 0x31) : 'EF_SLL',
(0x5F, 0x3C) : 'DF_MExE',
(0x5F, 0x3C, 0x4F, 0x40) : 'EF_MExE-ST',
(0x5F, 0x3C, 0x4F, 0x41) : 'EF_ORPK',
(0x5F, 0x3C, 0x4F, 0x42) : 'EF_ARPK',
(0x5F, 0x3C, 0x4F, 0x43) : 'EF_TPRK',
#(0x5F, 0x3C, 0x4F, 0xXX) : 'EF_TKCDF',
(0x5F, 0x3B) : 'DF_GSM-ACCESS',
(0x5F, 0x3B, 0x4F, 0x20) : 'EF_Kc',
(0x5F, 0x3B, 0x4F, 0x52) : 'EF_KcGPRS',
(0x5F, 0x3B, 0x4F, 0x63) : 'EF_CPBCCH',
(0x5F, 0x3B, 0x4F, 0x64) : 'EF_invSCAN',
(0x5F, 0x3A) : 'DF_PHONEBOOK',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_UID',
(0x5F, 0x3A, 0x4F, 0x22) : 'EF_PSC',
(0x5F, 0x3A, 0x4F, 0x23) : 'EF_CC',
(0x5F, 0x3A, 0x4F, 0x24) : 'EF_PUID',
(0x5F, 0x3A, 0x4F, 0x30) : 'EF_PBR',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_CCP1',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_IAP',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_ADN',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_EXT1',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_PBC',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_GRP',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_AAS',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_GAS',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_ANR',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_SNE',
#(0x5F, 0x3A, 0x4F, 0xXX) : 'EF_EMAIL',
(0x5F, 0xC0) : 'DF_5GS',  # NR-5G data
(0x5F, 0xC0, 0x4F, 0x01) : 'EF_5GS3GPPLOCI',
(0x5F, 0xC0, 0x4F, 0x02) : 'EF_5GSN3GPPLOCI',
(0x5F, 0xC0, 0x4F, 0x03) : 'EF_5GS3GPPNSC',
(0x5F, 0xC0, 0x4F, 0x04) : 'EF_5GS3NGPPNSC',
(0x5F, 0xC0, 0x4F, 0x05) : 'EF_5GAUTHKEYS',
(0x5F, 0xC0, 0x4F, 0x06) : 'EF_UAC_AIC',
(0x5F, 0xC0, 0x4F, 0x07) : 'EF_SUCI_Calc_Info',
(0x6F, 0x05) : 'EF_LI',
(0x6F, 0x06) : 'EF_ARR',
(0x6F, 0x07) : 'EF_IMSI',
(0x6F, 0x08) : 'EF_Keys',
(0x6F, 0x09) : 'EF_KeysPS',
(0x6F, 0x2C) : 'EF_DCK',
(0x6F, 0x31) : 'EF_HPLMN',
(0x6F, 0x32) : 'EF_CNL',
(0x6F, 0x37) : 'EF_ACMmax',
(0x6F, 0x38) : 'EF_UST',
(0x6F, 0x39) : 'EF_ACM',
(0x6F, 0x3B) : 'EF_FDN',
(0x6F, 0x3C) : 'EF_SMS',
(0x6F, 0x3E) : 'EF_GID1',
(0x6F, 0x3F) : 'EF_GID2',
(0x6F, 0x40) : 'EF_MSISDN',
(0x6F, 0x41) : 'EF_PUCT',
(0x6F, 0x42) : 'EF_SMSP',
(0x6F, 0x43) : 'EF_SMSS',
(0x6F, 0x45) : 'EF_CBMI',
(0x6F, 0x46) : 'EF_SPN',
(0x6F, 0x47) : 'EF_SMSR',
(0x6F, 0x48) : 'EF_CBMID',
(0x6F, 0x49) : 'EF_SDN',
(0x6F, 0x4B) : 'EF_EXT2',
(0x6F, 0x4C) : 'EF_EXT3',
(0x6F, 0x4D) : 'EF_BDN',
(0x6F, 0x4E) : 'EF_EXT5',
(0x6F, 0x50) : 'EF_CBMIR',
(0x6F, 0x55) : 'EF_EXT4',
(0x6F, 0x56) : 'EF_EST',
(0x6F, 0x57) : 'EF_ACL',
(0x6F, 0x58) : 'EF_CMI',
(0x6F, 0x5B) : 'EF_START-HFN',
(0x6F, 0x5C) : 'EF_THRESHOLD',
(0x6F, 0x60) : 'EF_PLMNwAcT',
(0x6F, 0x61) : 'EF_OPLMNwAcT',
(0x6F, 0x62) : 'EF_HPLMNwAcT',
(0x6F, 0xD9) : 'EF_EHPLMN',
(0x6F, 0x73) : 'EF_PSLOCI',
(0x6F, 0x78) : 'EF_ACC',
(0x6F, 0x7B) : 'EF_FPLMN',
(0x6F, 0x7E) : 'EF_LOCI',
(0x6F, 0x80) : 'EF_ICI',
(0x6F, 0x81) : 'EF_OCI',
(0x6F, 0x82) : 'EF_ICT',
(0x6F, 0x83) : 'EF_OCT',
(0x6F, 0xAD) : 'EF_AD',
(0x6F, 0xB5) : 'EF_eMLPP',
(0x6F, 0xB6) : 'EF_AAeM',
(0x6F, 0xB7) : 'EF_ECC',
(0x6F, 0xC3) : 'EF_Hiddenkey',
(0x6F, 0xC4) : 'EF_NETPAR',
(0x6F, 0xC5) : 'EF_PNN',
(0x6F, 0xC6) : 'EF_OPL',
(0x6F, 0xC7) : 'EF_MBDN',
(0x6F, 0xC8) : 'EF_EXT6',
(0x6F, 0xC9) : 'EF_MBI',
(0x6F, 0xCA) : 'EF_MWIS',
(0x6F, 0xCB) : 'EF_CFIS',
(0x6F, 0xCC) : 'EF_EXT7',
(0x6F, 0xCD) : 'EF_SPDI',
(0x6F, 0xCE) : 'EF_MMSN',
(0x6F, 0xCF) : 'EF_EXT8',
(0x6F, 0xD0) : 'EF_MMSICP',
(0x6F, 0xD1) : 'EF_MMSUP',
(0x6F, 0xD2) : 'EF_MMSUCP',
(0x6F, 0xD3) : 'EF_NIA',
(0x6F, 0x4F) : 'EF_CCP2',
(0x6F, 0xB1) : 'EF_VGCS',
(0x6F, 0xB2) : 'EF_VGCSS',
(0x6F, 0xB3) : 'EF_VBS',
(0x6F, 0xB4) : 'EF_VBSS',
(0x6F, 0xD4) : 'EF_VGCSCA',
(0x6F, 0xD5) : 'EF_VBSCA',
(0x6F, 0xD6) : 'EF_GBAP',
(0x6F, 0xD7) : 'EF_MSK',
(0x6F, 0xD8) : 'EF_MUK',
(0x6F, 0xDA) : 'EF_GBANL',
(0x6F, 0xDB) : 'EF_EHPLMNPI',
(0x6F, 0xDC) : 'EF_LRPLMNSI',
(0x6F, 0xDD) : 'EF_NAFKCA',
(0x6F, 0xDE) : 'EF_SPNI',
(0x6F, 0xDF) : 'EF_PNNI',
}

# Actually, those DF can be under MF, ADF_USIM or DF_TELECOM:
DF_PHONEBOOK = {
(0x5F, 0x3A) : 'DF_PHONEBOOK',
(0x5F, 0x3A, 0x4F) : 'EF_UID',
(0x5F, 0x3A, 0x4F, 0x22) : 'EF_PSC',
(0x5F, 0x3A, 0x4F, 0x23) : 'EF_CC',
(0x5F, 0x3A, 0x4F, 0x24) : 'EF_PUID',
(0x5F, 0x3A, 0x4F, 0x30) : 'EF_PBR',
(0x5F, 0x3A, 0x4F) : 'EF_CCP1',
(0x5F, 0x3A, 0x4F) : 'EF_IAP',
(0x5F, 0x3A, 0x4F) : 'EF_ADN',
(0x5F, 0x3A, 0x4F) : 'EF_EXT1',
(0x5F, 0x3A, 0x4F) : 'EF_PBC',
(0x5F, 0x3A, 0x4F) : 'EF_GRP',
(0x5F, 0x3A, 0x4F) : 'EF_AAS',
(0x5F, 0x3A, 0x4F) : 'EF_GAS',
(0x5F, 0x3A, 0x4F) : 'EF_ANR',
(0x5F, 0x3A, 0x4F) : 'EF_SNE',
(0x5F, 0x3A, 0x4F) : 'EF_EMAIL',
}

DF_GRAPHICS = {
(0x5F, 0x50) : 'DF_GRAPHICS',
(0x5F, 0x50, 0x4F, 0x20) : 'EF_IMG',
}

DF_MULTIMEDIA = {
(0x5F, 0x3B) : 'DF_MULTIMEDIA',
(0x5F, 0x3B, 0x4F, 0x47) : 'EF_MML',
(0x5F, 0x3B, 0x4F, 0x48) : 'EF_MMDF',
}
