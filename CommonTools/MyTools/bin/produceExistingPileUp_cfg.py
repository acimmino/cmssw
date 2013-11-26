import os

import FWCore.ParameterSet.Config as cms

from CommonTools.MyTools.existingPileUp_cff import *

process = cms.PSet(
  # pile-up distribution
  pileUpDistribution = cms.vdouble( *pileUp_Fall11 )
  # output file
, outputFile = cms.string( 'file:%s/src/CommonTools/MyTools/data/pileUpFileMC_Fall11.root'%( os.getenv( "CMSSW_BASE" ) ) )
)