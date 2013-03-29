import FWCore.ParameterSet.Config as cms

process = cms.Process("GeometryTest")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
#process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = autoCond['mc']

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(4)
)

process.PoolDBESSourceGeometry = cms.ESSource("PoolDBESSource",
                                              process.CondDBSetup,
                                              timetype = cms.string('runnumber'),
                                              toGet = cms.VPSet(
    cms.PSet(record = cms.string('PEcalEndcapRcd'),          tag = cms.string('EERECO_Geometry_newTag'))
    ),
                                              connect = cms.string('sqlite_file:EERECO_Geometry.db')
                                              )

process.es_prefer_geometry = cms.ESPrefer( "PoolDBESSource", "PoolDBESSourceGeometry" )

process.etta = cms.EDAnalyzer("dumpEcalTrigTowerMapping")

process.ctgw = cms.EDAnalyzer("testEcalGetWindow")

process.cga = cms.EDAnalyzer("CaloGeometryAnalyzer",
                             fullEcalDump = cms.untracked.bool(True)
                             )

process.mfa = cms.EDAnalyzer("testMagneticField")

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('calogeom.root')
                                   )

#process.p1 = cms.Path(process.etta*process.ctgw*process.cga*process.mfa) #etta crashes
process.p1 = cms.Path(process.ctgw*process.cga*process.mfa)


