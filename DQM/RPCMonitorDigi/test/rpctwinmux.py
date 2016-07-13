import FWCore.ParameterSet.Config as cms

process = cms.Process("RPCDQMTWINMUX")

############# Source File #################

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('file:RPCRecHitProducers.root')
                            )

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

################ Condition #################
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag as gtCustomise
process.GlobalTag = gtCustomise(process.GlobalTag, 'auto:run2_data', '')

############ Geometry ######################
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

############ RAW to DIGI ###################
## process.rpcunpacker = cms.EDFilter("RPCUnpackingModule",
##     InputLabel = cms.InputTag("source"),
##     doSynchro = cms.bool(False)
## )
#process.load("EventFilter.RPCRawToDigi.RPCFrontierCabling_cfi")

############ RecHits #######################
#process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")
#process.rpcRecHits.rpcDigiLabel ='rpcunpacker'
#process.rpcRecHits.rpcDigiLabel = 'muonRPCDigis'

################ DQM #######################
process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")
process.dqmEnv.subSystemFolder = 'RPC'
process.dqmSaver.convention = 'Online'
process.dqmSaver.saveByRun = True
process.dqmSaver.dirName    = '.'

############# RPC PAC #############
process.load("DQM.RPCMonitorDigi.RPCDigiMonitoring_cfi")
process.rpcdigidqm.UseRollInfo = True
process.rpcdigidqm.UseMuon =  False

############# RPC TWINMUX #############
process.load("DQM.RPCMonitorDigi.RPCTwinMuxMonitoring_cfi")
process.rpctwinmuxdqm.UseRollInfo = True
process.rpctwinmuxdqm.UseMuon =  False

############### Output Module ##############
process.out = cms.OutputModule("PoolOutputModule",
   fileName = cms.untracked.string('/tmp/cimmino/RPCDQM.root'),
   outputCommands = cms.untracked.vstring("keep *")
)

############# Message Logger ###############
process.MessageLogger = cms.Service("MessageLogger",
     debugModules = cms.untracked.vstring('*'),
     cout = cms.untracked.PSet( threshold = cms.untracked.string('DEBUG')),
     destinations = cms.untracked.vstring('cout')
)

############# Path ########################
process.p = cms.Path(process.rpcdigidqm*process.rpctwinmuxdqm*process.dqmSaver)

process.e = cms.EndPath(process.out)
