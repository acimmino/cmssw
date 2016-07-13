import FWCore.ParameterSet.Config as cms

rpctwinmuxdqm = cms.EDAnalyzer("RPCMonitorDigi",
                                   SaveRootFile = cms.untracked.bool(False),
                                   RootFileName = cms.untracked.string('RPCMonitorDigi.root'),
                                   UseRollInfo =  cms.untracked.bool(False),
                                   UseMuon =  cms.untracked.bool(False),
                                   MuonPtCut = cms.untracked.double(3.0),
                                   MuonEtaCut= cms.untracked.double(1.9),
                                   MuonLabel =  cms.InputTag('muons'),
                                   ScalersRawToDigiLabel = cms.InputTag('scalersRawToDigi'),
                                   RPCFolder = cms.untracked.string('RPC'),
                                   GlobalFolder = cms.untracked.string('SummaryHistograms'),
                                   RecHitLabel = cms.InputTag("rpcTwinMuxRecHits"),
                                   
                                   NoiseFolder  = cms.untracked.string("TwinMux"),
                                   MuonFolder = cms.untracked.string("Muon")
                                   )


