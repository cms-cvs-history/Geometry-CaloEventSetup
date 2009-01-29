# The following comments couldn't be translated into the new config version:

# timing and memory checks

import FWCore.ParameterSet.Config as cms

process = cms.Process("GeometryTest")

# Magnetic field full setup
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

# Geometry - overkill, used for test/completeness 
#            includes Sim, Digi & Reco files as far
#            as I can tell.

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

# Calo geometry service model

process.load("Geometry.CaloEventSetup.CaloGeometryDBReader_cfi")

#process.load("Geometry.CaloEventSetup.CaloGeometry_cff")

#process.load("Geometry.CaloEventSetup.AlignedCaloGeometry_cfi")

#process.load("Geometry.CaloEventSetup.FakeCaloAlignments_cff")

process.load("Geometry.CaloEventSetup.CaloTopology_cfi")

# Ecal TT mapping
process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")


process.load("CondCore.DBCommon.CondDBCommon_cfi")

process.PoolDBESSource = cms.ESSource("PoolDBESSource",
                                      process.CondDBCommon,
                                      loadAll = cms.bool(True),
                                      toGet = cms.VPSet(
    cms.PSet(record = cms.string('PEcalBarrelRcd'   ),tag = cms.string('TEST02')),
    cms.PSet(record = cms.string('PEcalEndcapRcd'   ),tag = cms.string('TEST03')),
    cms.PSet(record = cms.string('PEcalPreshowerRcd'),tag = cms.string('TEST04')),
    cms.PSet(record = cms.string('PHcalRcd'         ),tag = cms.string('TEST05')),
    cms.PSet(record = cms.string('PCaloTowerRcd'    ),tag = cms.string('TEST06')),
    cms.PSet(record = cms.string('PZdcRcd'          ),tag = cms.string('TEST07')),
    cms.PSet(record = cms.string('PCastorRcd'       ),tag = cms.string('TEST08'))
    ),
                                      BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
                                      timetype = cms.untracked.string('runnumber'),
                                      connect = cms.string('sqlite_file:calofile.db')
                                      )

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(4)
)
process.source = cms.Source("EmptySource")

process.etta = cms.EDFilter("dumpEcalTrigTowerMapping")

process.ctgw = cms.EDFilter("testEcalGetWindow")

process.cga = cms.EDAnalyzer("CaloGeometryAnalyzer",
    fullEcalDump = cms.untracked.bool(True)
)

process.mfa = cms.EDFilter("testMagneticField")

process.Timing = cms.Service("Timing")

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")

process.TFileService = cms.Service("TFileService", fileName = cms.string('calogeom.root') )

process.p1 = cms.Path(process.etta*process.ctgw*process.cga*process.mfa)


