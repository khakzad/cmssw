import FWCore.ParameterSet.Config as cms

#Track selector
from Validation.RecoMuon.selectors_cff import *

#TrackAssociation
from SimTracker.TrackAssociation.TrackAssociatorByChi2_cfi import *
import SimTracker.TrackAssociation.TrackAssociatorByHits_cfi
import SimTracker.TrackAssociation.TrackAssociatorByPosition_cfi

TrackAssociatorByHits = SimTracker.TrackAssociation.TrackAssociatorByHits_cfi.TrackAssociatorByHits.clone()

OnlineTrackAssociatorByHits = SimTracker.TrackAssociation.TrackAssociatorByHits_cfi.TrackAssociatorByHits.clone()
OnlineTrackAssociatorByHits.ComponentName = 'OnlineTrackAssociatorByHits'
OnlineTrackAssociatorByHits.UseGrouped = False
OnlineTrackAssociatorByHits.UseSplitting = False
OnlineTrackAssociatorByHits.ThreeHitTracksAreSpecial = False

TrackAssociatorByPosDeltaR = SimTracker.TrackAssociation.TrackAssociatorByPosition_cfi.TrackAssociatorByPosition.clone()
TrackAssociatorByPosDeltaR.ComponentName = 'TrackAssociatorByDeltaR'
TrackAssociatorByPosDeltaR.method = cms.string('momdr')
TrackAssociatorByPosDeltaR.QCut = cms.double(0.5)
TrackAssociatorByPosDeltaR.ConsiderAllSimHits = cms.bool(True)
    

#
# Associators for Full Sim + Reco:
#

tpToTkmuTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByHits'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('generalTracks')
)

tpToStaTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('standAloneMuons','')
#    label_tr = cms.InputTag('muonSta')
)

tpToStaUpdTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('standAloneMuons','UpdatedAtVtx')
#    label_tr = cms.InputTag('muonSta')
)

tpToGlbTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('globalMuons')
#    label_tr = cms.InputTag('muonGlb')
)

tpToStaSETTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('standAloneSETMuons','')
)

tpToStaSETUpdTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('standAloneSETMuons','UpdatedAtVtx')
)

tpToGlbSETTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('globalSETMuons')
)

tpToTevFirstTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('tevMuons','firstHit')
)

tpToTevPickyTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('tevMuons','picky')
)

tpToL2TrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('hltL2Muons','')
)

tpToL2UpdTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('hltL2Muons','UpdatedAtVtx')
)

tpToL3TrackAssociation = cms.EDProducer("TrackAssociatorEDProducer",
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('hltL3Muons')
)

tpToL3TkTrackTrackAssociation = cms.EDProducer("TrackAssociatorEDProducer",
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('OnlineTrackAssociatorByHits'),
    label_tp = cms.InputTag('mergedtruth','MergedTrackTruth'),
    label_tr = cms.InputTag('hltL3TkTracksFromL2','')
)

tpToL3L2TrackTrackAssociation = cms.EDProducer("TrackAssociatorEDProducer",
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('OnlineTrackAssociatorByHits'),
    label_tp = cms.InputTag('mergedtruth','MergedTrackTruth'),
    label_tr = cms.InputTag('hltL3Muons:L2Seeded')
)



#MuonAssociation
import SimMuon.MCTruth.MuonAssociatorByHits_cfi

tpToTkMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToStaMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToStaUpdMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToGlbMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToStaSETMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToStaSETUpdMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToGlbSETMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToTevFirstMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToTevPickyMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToL3TkMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToL2MuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToL2UpdMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToL3MuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()

tpToTkMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToTkMuonAssociation.tracksTag = 'generalTracks'
tpToTkMuonAssociation.UseTracker = True
tpToTkMuonAssociation.UseMuon = False

tpToStaMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToStaMuonAssociation.tracksTag = 'standAloneMuons'
tpToStaMuonAssociation.UseTracker = False
tpToStaMuonAssociation.UseMuon = True

tpToStaUpdMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToStaUpdMuonAssociation.tracksTag = 'standAloneMuons:UpdatedAtVtx'
tpToStaUpdMuonAssociation.UseTracker = False
tpToStaUpdMuonAssociation.UseMuon = True

tpToGlbMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToGlbMuonAssociation.tracksTag = 'globalMuons'
tpToGlbMuonAssociation.UseTracker = True
tpToGlbMuonAssociation.UseMuon = True

tpToStaSETMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToStaSETMuonAssociation.tracksTag = 'standAloneSETMuons'
tpToStaSETMuonAssociation.UseTracker = False
tpToStaSETMuonAssociation.UseMuon = True

tpToStaSETUpdMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToStaSETUpdMuonAssociation.tracksTag = 'standAloneSETMuons:UpdatedAtVtx'
tpToStaSETUpdMuonAssociation.UseTracker = False
tpToStaSETUpdMuonAssociation.UseMuon = True

tpToGlbSETMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToGlbSETMuonAssociation.tracksTag = 'globalSETMuons'
tpToGlbSETMuonAssociation.UseTracker = True
tpToGlbSETMuonAssociation.UseMuon = True

tpToTevFirstMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToTevFirstMuonAssociation.tracksTag = 'tevMuons:firstHit'
tpToTevFirstMuonAssociation.UseTracker = True
tpToTevFirstMuonAssociation.UseMuon = True

tpToTevPickyMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToTevPickyMuonAssociation.tracksTag = 'tevMuons:picky'
tpToTevPickyMuonAssociation.UseTracker = True
tpToTevPickyMuonAssociation.UseMuon = True

tpToL3TkMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToL3TkMuonAssociation.tracksTag = 'hltL3TkTracksFromL2'
tpToL3TkMuonAssociation.DTrechitTag = 'hltDt1DRecHits'
tpToL3TkMuonAssociation.UseTracker = True
tpToL3TkMuonAssociation.UseMuon = False
tpToL3TkMuonAssociation.ignoreMissingTrackCollection = True
tpToL3TkMuonAssociation.UseSplitting = False
tpToL3TkMuonAssociation.UseGrouped = False

tpToL2MuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToL2MuonAssociation.tracksTag = 'hltL2Muons'
tpToL2MuonAssociation.DTrechitTag = 'hltDt1DRecHits'
tpToL2MuonAssociation.UseTracker = False
tpToL2MuonAssociation.UseMuon = True
tpToL2MuonAssociation.ignoreMissingTrackCollection = True

tpToL2UpdMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToL2UpdMuonAssociation.tracksTag = 'hltL2Muons:UpdatedAtVtx'
tpToL2UpdMuonAssociation.DTrechitTag = 'hltDt1DRecHits'
tpToL2UpdMuonAssociation.UseTracker = False
tpToL2UpdMuonAssociation.UseMuon = True
tpToL2UpdMuonAssociation.ignoreMissingTrackCollection = True

tpToL3MuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToL3MuonAssociation.tracksTag = 'hltL3Muons'
tpToL3MuonAssociation.DTrechitTag = 'hltDt1DRecHits'
tpToL3MuonAssociation.UseTracker = True
tpToL3MuonAssociation.UseMuon = True
tpToL3MuonAssociation.ignoreMissingTrackCollection = True
tpToL3MuonAssociation.UseSplitting = False
tpToL3MuonAssociation.UseGrouped = False

#
# Associators for cosmics:
#

tpToTkCosmicTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByHits'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('ctfWithMaterialTracksP5LHCNavigation')
)

tpToStaCosmicTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('cosmicMuons')
)

tpToGlbCosmicTrackAssociation = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('globalCosmicMuons')
)

tpToTkCosmicMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToStaCosmicMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
tpToGlbCosmicMuonAssociation = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()

tpToTkCosmicMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToTkCosmicMuonAssociation.tracksTag = 'ctfWithMaterialTracksP5LHCNavigation'
tpToTkCosmicMuonAssociation.UseTracker = True
tpToTkCosmicMuonAssociation.UseMuon = False

tpToStaCosmicMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToStaCosmicMuonAssociation.tracksTag = 'cosmicMuons'
tpToStaCosmicMuonAssociation.UseTracker = False
tpToStaCosmicMuonAssociation.UseMuon = True

tpToGlbCosmicMuonAssociation.tpTag = 'mergedtruth:MergedTrackTruth'
tpToGlbCosmicMuonAssociation.tracksTag = 'globalCosmicMuons'
tpToGlbCosmicMuonAssociation.UseTracker = True
tpToGlbCosmicMuonAssociation.UseMuon = True


#
# The full-sim association sequences
#

muonAssociation_seq = cms.Sequence(
    tpToTkMuonAssociation
    +tpToStaMuonAssociation+tpToStaUpdMuonAssociation+tpToGlbMuonAssociation
    +tpToTkmuTrackAssociation
#    +tpToTkmuTrackAssociation+tpToStaTrackAssociation+tpToStaUpdTrackAssociation+tpToGlbTrackAssociation
)
muonAssociationTEV_seq = cms.Sequence((
    tpToTevFirstMuonAssociation+tpToTevPickyMuonAssociation)
#    +(tpToTevFirstTrackAssociation+tpToTevPickyTrackAssociation))
)
muonAssociationSET_seq = cms.Sequence(
    (tpToStaSETMuonAssociation+tpToStaSETUpdMuonAssociation+tpToGlbSETMuonAssociation)
#    +(tpToStaSETTrackAssociation+tpToStaSETUpdTrackAssociation+tpToGlbSETTrackAssociation)
)
muonAssociationCosmic_seq = cms.Sequence(
    (tpToTkCosmicMuonAssociation+tpToStaCosmicMuonAssociation+tpToGlbCosmicMuonAssociation)
#    +(tpToTkCosmicTrackAssociation+tpToStaCosmicTrackAssociation+tpToGlbCosmicTrackAssociation)
)
muonAssociationHLT_seq = cms.Sequence(
    (tpToL2MuonAssociation+tpToL2UpdMuonAssociation+tpToL3MuonAssociation+tpToL3TkMuonAssociation)
#    +(tpToL2TrackAssociation+tpToL2UpdTrackAssociation+tpToL3TrackAssociation+tpToL3TkTrackTrackAssociation)
)


#
# Associators for Fast Sim
#

tpToTkmuTrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByHits'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('generalTracks')
)

tpToStaTrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('standAloneMuons','')
)

tpToStaUpdTrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('standAloneMuons','UpdatedAtVtx')
)

tpToGlbTrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('globalMuons')
)

tpToTevFirstTrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('tevMuons','firstHit')
)

tpToTevPickyTrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('tevMuons','picky')
)

tpToL2TrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('hltL2Muons','')
)

tpToL2UpdTrackAssociationFS = cms.EDProducer('TrackAssociatorEDProducer',
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('hltL2Muons','UpdatedAtVtx')
)

tpToL3TrackAssociationFS = cms.EDProducer("TrackAssociatorEDProducer",
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('TrackAssociatorByDeltaR'),
    label_tp = cms.InputTag('mergedtruth', 'MergedTrackTruth'),
    label_tr = cms.InputTag('hltL3Muons')
)

tpToL3TkTrackTrackAssociationFS = cms.EDProducer("TrackAssociatorEDProducer",
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('OnlineTrackAssociatorByHits'),
    label_tp = cms.InputTag('mergedtruth','MergedTrackTruth'),
    label_tr = cms.InputTag('hltL3TkTracksFromL2','')
)

tpToL3L2TrackTrackAssociationFS = cms.EDProducer("TrackAssociatorEDProducer",
    ignoremissingtrackcollection=cms.untracked.bool(True),
    associator = cms.string('OnlineTrackAssociatorByHits'),
    label_tp = cms.InputTag('mergedtruth','MergedTrackTruth'),
    label_tr = cms.InputTag('hltL3Muons:L2Seeded')
)


#MuonAssociation
import SimMuon.MCTruth.MuonAssociatorByHits_cfi

baseMuonAssociatorFS = SimMuon.MCTruth.MuonAssociatorByHits_cfi.muonAssociatorByHits.clone()
baseMuonAssociatorFS.tpTag = 'mergedtruth:MergedTrackTruth'
baseMuonAssociatorFS.UseTracker = True
baseMuonAssociatorFS.UseMuon = True
baseMuonAssociatorFS.simtracksTag = "famosSimHits"
baseMuonAssociatorFS.DTsimhitsTag  = "MuonSimHits:MuonDTHits"
baseMuonAssociatorFS.CSCsimHitsTag = "MuonSimHits:MuonCSCHits"
baseMuonAssociatorFS.RPCsimhitsTag = "MuonSimHits:MuonRPCHits"
baseMuonAssociatorFS.simtracksXFTag = "mix:famosSimHits"
baseMuonAssociatorFS.DTsimhitsXFTag  = "mix:MuonSimHitsMuonDTHits"
baseMuonAssociatorFS.CSCsimHitsXFTag = "mix:MuonSimHitsMuonCSCHits"
baseMuonAssociatorFS.RPCsimhitsXFTag = "mix:MuonSimHitsMuonRPCHits"
baseMuonAssociatorFS.ROUList = ['famosSimHitsTrackerHits']


tpToTkMuonAssociationFS   = baseMuonAssociatorFS.clone()
tpToStaMuonAssociationFS  = baseMuonAssociatorFS.clone()
tpToStaUpdMuonAssociationFS  = baseMuonAssociatorFS.clone()
tpToGlbMuonAssociationFS  = baseMuonAssociatorFS.clone()
tpToTevFirstMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToTevPickyMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToL3TkMuonAssociationFS = baseMuonAssociatorFS.clone()
tpToL2MuonAssociationFS   = baseMuonAssociatorFS.clone()
tpToL2UpdMuonAssociationFS   = baseMuonAssociatorFS.clone()
tpToL3MuonAssociationFS   = baseMuonAssociatorFS.clone()

tpToTkMuonAssociationFS.tracksTag = 'generalTracks'
tpToTkMuonAssociationFS.UseTracker = True
tpToTkMuonAssociationFS.UseMuon = False

tpToStaMuonAssociationFS.tracksTag = 'standAloneMuons'
tpToStaMuonAssociationFS.UseTracker = False
tpToStaMuonAssociationFS.UseMuon = True

tpToStaUpdMuonAssociationFS.tracksTag = 'standAloneMuons:UpdatedAtVtx'
tpToStaUpdMuonAssociationFS.UseTracker = False
tpToStaUpdMuonAssociationFS.UseMuon = True

tpToGlbMuonAssociationFS.tracksTag = 'globalMuons'
tpToGlbMuonAssociationFS.UseTracker = True
tpToGlbMuonAssociationFS.UseMuon = True

tpToTevFirstMuonAssociationFS.tracksTag = 'tevMuons:firstHit'
tpToTevFirstMuonAssociationFS.UseTracker = True
tpToTevFirstMuonAssociationFS.UseMuon = True

tpToTevPickyMuonAssociationFS.tracksTag = 'tevMuons:picky'
tpToTevPickyMuonAssociationFS.UseTracker = True
tpToTevPickyMuonAssociationFS.UseMuon = True

tpToL3TkMuonAssociationFS.tracksTag = 'hltL3TkTracksFromL2'
tpToL3TkMuonAssociationFS.UseTracker = True
tpToL3TkMuonAssociationFS.UseMuon = False
tpToL3TkMuonAssociationFS.ignoreMissingTrackCollection = True
tpToL3TkMuonAssociationFS.UseSplitting = False
tpToL3TkMuonAssociationFS.UseGrouped = False

tpToL2MuonAssociationFS.tracksTag = 'hltL2Muons'
tpToL2MuonAssociationFS.UseTracker = False
tpToL2MuonAssociationFS.UseMuon = True
tpToL2MuonAssociationFS.ignoreMissingTrackCollection = True

tpToL2UpdMuonAssociationFS.tracksTag = 'hltL2Muons:UpdatedAtVtx'
tpToL2UpdMuonAssociationFS.UseTracker = False
tpToL2UpdMuonAssociationFS.UseMuon = True
tpToL2UpdMuonAssociationFS.ignoreMissingTrackCollection = True

tpToL3MuonAssociationFS.tracksTag = 'hltL3Muons'
tpToL3MuonAssociationFS.UseTracker = True
tpToL3MuonAssociationFS.UseMuon = True
tpToL3MuonAssociationFS.ignoreMissingTrackCollection = True
tpToL3MuonAssociationFS.UseSplitting = False
tpToL3MuonAssociationFS.UseGrouped = False



muonAssociationFastSim_seq = cms.Sequence(tpToTkMuonAssociationFS
                                          +tpToStaMuonAssociationFS+tpToStaUpdMuonAssociationFS+tpToGlbMuonAssociationFS
                                          +tpToTevFirstMuonAssociationFS+tpToTevPickyMuonAssociationFS
                                          +tpToTkmuTrackAssociationFS
#                                          +tpToStaTrackAssociationFS+tpToStaUpdTrackAssociationFS+tpToGlbTrackAssociationFS
#                                          +tpToTevFirstTrackAssociationFS+tpToTevPickyTrackAssociationFS
)
muonAssociationHLTFastSim_seq = cms.Sequence(
    tpToL2MuonAssociationFS+tpToL2UpdMuonAssociationFS+tpToL3MuonAssociationFS+tpToL3TkMuonAssociationFS
#    +tpToL2TrackAssociationFS+tpToL2UpdTrackAssociationFS+tpToL3TrackAssociationFS+tpToL3TkTrackTrackAssociationFS
)

