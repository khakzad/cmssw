import FWCore.ParameterSet.Config as cms

from L1Trigger.L1TGlobal.PrescalesVetos_cff import *

L1TGlobalPrescalesVetosOnlineProd = cms.ESProducer("L1TGlobalPrescalesVetosOnlineProd",
    onlineAuthentication = cms.string('.'),
    forceGeneration = cms.bool(False),
    onlineDB = cms.string('oracle://CMS_OMDS_LB/CMS_TRG_R'),
    xmlModel = cms.int32(2017)
)
