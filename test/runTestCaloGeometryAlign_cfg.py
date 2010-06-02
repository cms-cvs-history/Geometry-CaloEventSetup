
import FWCore.ParameterSet.Config as cms

process = cms.Process("GeometryTest")

process.load("Configuration.StandardSequences.MagneticField_38T_cff")

process.load('Configuration/StandardSequences/GeometryDB_cff')

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MC_37Y_V4::All' 

process.load("Geometry.CaloEventSetup.CaloGeometryDBReader_cfi")

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(4) )


process.etta = cms.EDAnalyzer("dumpEcalTrigTowerMapping")

process.ctgw = cms.EDAnalyzer("testEcalGetWindow")

process.cga = cms.EDAnalyzer("CaloGeometryAnalyzer",
                             fullEcalDump = cms.untracked.bool(True)
                             )

process.mfa = cms.EDAnalyzer("testMagneticField")


process.EcalBarrelGeometryFromDBEP.applyAlignment = True
process.EcalEndcapGeometryFromDBEP.applyAlignment = True
process.EcalPreshowerGeometryFromDBEP.applyAlignment = True
process.load("Geometry.CaloEventSetup.TestCaloAlignments_cff")

process.Timing = cms.Service("Timing")

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('calogeom.root')
                                   )

process.p1 = cms.Path(process.etta*process.ctgw*process.cga*process.mfa)


